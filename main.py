import argparse
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
import pty
import os
import subprocess
import select
import termios
import struct
import fcntl
import shlex
import webbrowser


app = Flask(__name__ , template_folder=".", static_folder=".", static_url_path="")
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["fd"] = None
app.config["child_pid"] = None
socketio = SocketIO(app)

def set_winsize(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

def read_and_forward_pty_output():
    max_read_bytes = 1024 * 20
    while True:
        socketio.sleep(0.01)
        if app.config["fd"]:
            timeout_sec = 0
            (data_ready, _, _) = select.select([app.config["fd"]], [], [], timeout_sec)
            if data_ready:
                output = os.read(app.config["fd"], max_read_bytes).decode(
                    errors="ignore"
                )
                socketio.emit("pty-output", {"output": output}, namespace="/pty")

@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@socketio.on("pty-input", namespace="/pty")
def pty_input(data):
    """write to the child pty. The pty sees this as if you are typing in a real
    terminal.
    """
    if app.config["fd"]:
        os.write(app.config["fd"], data["input"].encode())

@socketio.on("resize", namespace="/pty")
def resize(data):
    if app.config["fd"]:
        set_winsize(app.config["fd"], data["rows"], data["cols"])

@socketio.on("connect", namespace="/pty")
def connect():
    """new client connected"""
    if app.config["child_pid"]:
        return

    (child_pid, fd) = pty.fork()
    if child_pid == 0:
        subprocess.run(app.config["cmd"])
    else:
        app.config["fd"] = fd
        app.config["child_pid"] = child_pid
        set_winsize(fd, 50, 50)
        # cmd = " ".join(shlex.quote(c) for c in app.config["cmd"])
        socketio.start_background_task(target=read_and_forward_pty_output)

def main():
    parser = argparse.ArgumentParser(
        description=(
            "A fully functional terminal in your browser. "
            "https://github.com/cs01/pyxterm.js"
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-p", "--port", default=5050, type=int
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
    )
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--version", action="store_true")
    parser.add_argument(
        "--command", default="python3"
    )
    parser.add_argument(
        "--cmd-args",
        default="game.py",
    )
    args = parser.parse_args()
    app.config["cmd"] = [args.command] + shlex.split(args.cmd_args)
    webbrowser.open_new_tab(f"http://{args.host}:{args.port}")
    socketio.run(app, debug=args.debug, port=args.port, host=args.host)
    
if __name__ == "__main__":
    main()