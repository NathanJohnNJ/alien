#!/.env/bin/python3
from time import sleep
from colorama import Back, Fore, Style

dimWhite = Style.RESET_ALL+Fore.WHITE+Style.DIM
brightWhite = Style.RESET_ALL+Fore.WHITE+Style.BRIGHT
normalWhite = Style.RESET_ALL+Fore.WHITE+Style.NORMAL
dimRed = Style.RESET_ALL+Fore.RED+Style.DIM
brightRed = Style.RESET_ALL+Fore.RED+Style.BRIGHT
dimGreen = Style.RESET_ALL+Fore.GREEN+Style.DIM
brightGreen = Style.RESET_ALL+Fore.GREEN+Style.BRIGHT
dimBlue = Style.RESET_ALL+Fore.BLUE+Style.DIM
brightBlue = Style.RESET_ALL+Fore.BLUE+Style.BRIGHT
dimCyan = Style.RESET_ALL+Fore.CYAN+Style.DIM
brightCyan = Style.RESET_ALL+Fore.CYAN+Style.BRIGHT
dimMagenta = Style.RESET_ALL+Fore.MAGENTA+Style.DIM
brightMagenta = Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT
dimYellow = Style.RESET_ALL+Fore.YELLOW+Style.DIM
brightYellow = Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT

lives = 3
startMap = dimWhite+ """: - - : -- :
|      
:     :
|  """+ brightRed +"^" +dimWhite+ """  |
: - - :""" +brightGreen
j1Map = dimWhite+ """: -- : - - :
|          |
:    :     :
|    |     | 
: -- :  """+ brightRed +"V" +dimWhite+ """  : -- :
|               
:    : - - : -- :"""+brightGreen
j12Map =dimWhite+ """: -- : -- :
|         |
:    :    : 
|    |    |
: -- :    : -- :    
|                   
:    : -- : -- : 
|         |         |
: -- :    : -- :    :
     |        """+ brightRed +">" +dimWhite+ """     |
     : -- : -- :    :"""+brightGreen
j121Map =dimWhite+ """: -- : - - :
|          |
:    :     : 
|    |     |
: -- :  """+ brightRed +"V" +dimWhite+ """  : -- :    
|                   
:    : - - : -- : 
|          |         |
: -- :     : -- :    :
     |               |
     : - - : -- :    :"""+brightGreen
j13Map = dimWhite+ """: -- : -- :    :     :    :
|         |    |     |
:    :    :    : - - :    :
|    |    |               |
: -- :    : -- :  """+ brightRed +"^" +dimWhite+ """  : -- :
|                    |
:    : -- : -- : - - :"""+brightGreen
j123Map = dimWhite+ """: -- : -- :    :    :    :
|         |    |     |
:    :    :    : - - :    :
|    |    |               |
: -- :    : -- :  """+ brightRed +"^" +dimWhite+ """  : -- :
|                    |
:    : -- : -- : - - :
                     |
: -- :    : -- :     :
     |               |
: -- : -- : -- :     :"""+brightGreen
j134Map = dimWhite+ """.              . -- . -- . -- . -- .
|              |                   |
:    : -- : -- :    : -- : -- :    :
|   """+ brightRed +"<" +dimWhite+ """               |         |    |
:    : -- : -- : -- :    :    :    :
|         |         |    |    |    |
: -- :    :    :    :    : -- :    :
          |    |    |              |
          : -- :    : -- :    : -- :
          |                   |
          :    : -- : -- : -- :"""+brightGreen
j1234Map = dimWhite+ """.              . -- . -- . -- . -- .
|              |                   |
:    : -- : -- :    : -- : -- :    :
|   """+ brightRed +"<" +dimWhite+ """               |         |    |
:    : -- : -- : -- :    :    :    :
|         |         |    |    |    |
: -- :    :    :    :    : -- :    :
          |    |    |              |
          : -- :    : -- :    : -- :
          |                   |
          :    : -- : -- : -- :
          |         |         |
          : -- :    : -- :    :
               |              |
               : -- : -- :    :
               |              |
               : -- : -- : -- :"""+brightGreen
j12345Map = dimWhite+ """. -- . - - . -- . -- . -- . -- . -- .
|              |                    |
:    : - - : -- :    : -- : -- :    :
|                    |         |    |
:    : - - : -- : -- :    :    :    :
|          |         |    |    |    |
: -- :     :    :    :    : -- :    :
     |     |    |    |              |
     :     : -- :    : -- :    : -- :
     |     |                   |
     :     :    : -- : -- : -- :
     |     |         |         | 
     :  """+ brightRed +"V" +dimWhite+ """  : -- :    : -- :    :
               |              |
  -- : - - :    : -- : -- :    :
               |              |
               : -- : -- : -- :"""+brightGreen
j1345Map = dimWhite+ """ . -- . - - . -- . -- . -- . -- . -- .
|                |                   |
:    : - - : - - :    : -- : -- :    :
|                     |         |    |
:    : - - : - - : -- :    :    :    :
|          |          |    |    |    |
: -- :     :     :    :    : -- :    :
     |     |     |    |              |
     :     : - - :    : -- :    : -- :
     |     |                    |     
     :     :     : -- : -- : -- :
     |     |     
     :  """+ brightRed +"V" +dimWhite+ """  : - - :
                 |
: -- : - - :     :"""+brightGreen
fullMap = dimWhite+ """. -- . -- . -- . -- . -- . -- . -- .
|              |                   |
:    : -- : -- :    : -- : -- :    :     """+ brightRed +"*" + brightCyan +"   *" +dimWhite+ """  
|                   |         |    | """+ brightGreen +"*" +dimRed+ """   |  /"""+ brightYellow +"*"+ brightBlue +"  *" +dimWhite+ """ 
:    : -- : -- : -- :    :    :    :  """+ dimRed +"\\  | /  \\ |"+brightYellow +"   *"+ brightCyan +"    *" +dimWhite+ """ 
|         |         |    |    |    |   """+ dimRed +"\\ |/    \\| "+ brightMagenta +"*"+dimRed+"  \\"+ brightGreen +"*" +dimRed+ """ /"""+dimWhite+ """ 
: -- :    :    :    :    : -- :    :   """+dimRed+"  /    """+ brightRed +"*" +dimRed+ " |/ "+ dimRed +"  /\\/ "+dimWhite+ """
|    |    |    |    |              |   """+dimRed+"       | /   / /\\   "+dimWhite+ """
:    :    : -- :    : -- :    : -- : """+brightBlue+" \\"+brightYellow+"e"+brightBlue+"/ "+brightMagenta+" *"+dimRed+"  |/  "+brightBlue+"*"+dimWhite+ """
|    |    |                   |      """+brightBlue+"  I    "+dimRed+"\ |  /"+dimWhite+ """
:    :    :    : -- : -- : -- :    :"""+brightGreen+" _"+brightBlue+"/ \\"+brightGreen+"_"+dimRed+"   \\  /"+dimWhite+ """
|    |    |         |         |    |
:    :    : -- :    : -- :    :    :
|              |              |    |
: -- : -- :    : -- : -- :    :    :
|              |              |    |
:    : -- : -- : -- : -- : -- :    :
|                                  |
: -- : -- : -- : -- : -- : -- : -- :"""+brightGreen
visits = []
#Beginning of game
def title():
    print(Back.RESET + "")
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +" +dimWhite + " ┌─┐┬  ┌─┐┌─┐┌─┐  ┌─┐┌┐┌┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐┬─┐┌─┐ " + dimMagenta + "+")
    print(brightYellow+ "           |" +normalWhite + " │  │  │ │└─┐├┤   ├┤ ││││  │ ││ ││││ │ ├┤ ├┬┘└─┐ " + brightYellow + "|")
    print(dimMagenta+ "           +" +dimWhite + " └─┘┴─┘└─┘└─┘└─┘  └─┘┘└┘└─┘└─┘└─┘┘└┘ ┴ └─┘┴└─└─┘ " + dimMagenta + "+")
    print(brightYellow+ "           |" +normalWhite + "                  ┌─┐ ┌─┐   ┌─┐                  " + brightYellow + "|")
    print(dimMagenta+ "           +" +dimWhite + "                  │ │ ├┤    ├─┤                  " + dimMagenta + "+")
    print(brightYellow+ "           |" +normalWhite + "                  └─┘ └     ┴ ┴                  " + brightYellow + "|")
    print(dimMagenta+ "           +" +dimWhite + "       ┌─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌      ┬┌─┬┌┐┌┌┬┐        " + dimMagenta + "+")
    print(brightYellow+ "           |" +normalWhite + "       ├─┘└┬┘ │ ├─┤│ ││││      ├┴┐││││ ││        " + brightYellow + "|")
    print(dimMagenta+ "           +" +dimWhite + "       ┴   ┴  ┴ ┴ ┴└─┘┘└┘      ┴ ┴┴┘└┘─┴┘       " + dimMagenta + " +")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")
  
def intro():
    print("")
    sleep(1)
    print(brightYellow + "Rules: You have 3 lives to escape this maze")
    sleep(1)
    print("If you pick the wrong direction you will be greeted with a question, If you answer this question wrong you will lose a life and return to the start of the maze.")
    sleep(1)
    print("If you answer correctly you will return to the previous junction with your lives intact")
    print("")
    sleep(1)
    beginning()
    sleep(1)
    print("You've reached a turning point in the road and have a decision to make...")
    sleep(1)
    print("Which way to go...")
    sleep(1)
    print("You look left. The left turn seems to lead you down a pitch black, cold, damp corridor...")
    sleep(1)
    print("You look right. The right turn seems to lead you down a smelly corridor with occasional bursts of steam shooting from cracks in the floor...")
    sleep(1)
    print("You take a moment to consider how steam is trapped under a field of crops without the floor feeling hot. You also wonder who built a corridor in the middle of a field, before making your decision.")
    sleep(2)
    junction1()
  
def aliens():
    print(brightCyan +'                  _____                                         ')
    print('              _.-"     "-._                     _____            ')
    print('             /    ' + brightGreen+')_-_(    '+brightCyan +'\                _.-"     "-._        ')
    print('            /    ' + brightGreen+'(' + brightBlue+' o o ' + brightGreen+') '+brightCyan +'   \              /   ' + brightGreen+' }_-_{  '+brightCyan +'  \       ')
    print('           /      ' + brightGreen+'( o )  '+brightCyan +'    \            /   ' + brightGreen+' { ' + brightBlue+'o o' + brightGreen+' }  '+brightCyan +'  \      ')
    print('          /        ' + brightGreen+'(-)  '+brightCyan +'      \          /     ' + brightGreen+' { o }    '+brightCyan +'  \     ')   
    print('         / '+brightRed +' o   ' + brightGreen+' .-"-"-.  '+brightRed +'  o '+brightCyan +''+brightCyan +' \        /        ' + brightGreen+'{-}   '+brightCyan +'     \    ')  
    print('        / '+brightRed +'  I  ' + brightGreen+' /       \ '+brightRed +'  I '+brightCyan +'  \      /  '+brightRed +'o    ' + brightGreen+'.-"-"-.  '+brightRed +'  o '+brightCyan +' \   ')   
    print('       (   ' + brightGreen+'(_} /\       /\ {_) '+brightCyan +'  )    / '+brightRed +'  I  ' + brightGreen+' /       \  '+brightRed +' I '+brightCyan +'  \  ')  
    print('        \\'+normalWhite +'.__]' + brightGreen+'\/'+normalWhite +'__' + brightGreen+'\\'+normalWhite +'_____' + brightGreen+'/' + normalWhite+'__' + brightGreen+'\/' + normalWhite+'[__.' + brightCyan+'/    (   ' + brightGreen+'(_} /\       /\ {_)   ' + brightCyan+') ')
    print('       ' + normalWhite+'(                         )    ' + brightCyan+'\\' + normalWhite+'.__]' + brightGreen+'\/' + normalWhite+'__' + brightGreen+'\\' + normalWhite+'_____' + brightGreen+'/' + normalWhite+'__' + brightGreen+'\\/' + normalWhite+'[__.' + brightCyan+'/  ') 
    print(normalWhite+'        "-_    '+brightWhite+' O o O o O'+normalWhite+'     _-"    (                         ) ') 
    print('           "--.___________.--"        "-_    '+brightWhite+' O o O o O'+normalWhite+'     _-"  ')
    print('                                         "--.___________.--"     ')
    sleep(2)
  
def beginning():
    aliens()
    print(brightGreen + "'Well that was pointless!' You hear a strange, muffled voice say.")
    sleep(1)
    print("'Drop them back to their dying planet. Looks like we'll need to search another solar system if we want to find the secret to sustainability.'")
    sleep(4)
    print(brightBlue + "'But we didn't try the probe yet!'")
    sleep(1)
    print(".")
    sleep(0.5)
    print("..")
    sleep(0.5)
    print("...")
    sleep(0.5)
    print(brightGreen + """'No, just chuck them out!...
We may as well have some fun with them though. Print our hardest labrynth in one of the crop fields and leave them in the middle. We can watch them try and escape before we go. I should have just enough time before Barbarella gets home from work.'""")
    print(brightCyan + "*Blink, blink, blink*")
    sleep(3)
    print(brightGreen + """You rub your eyes trying to help see in the engulfing darkness. 
A putrid smell fills the air, and your head hurts. 
Clambering to your feet you reach out and feel huge crops surrounding you, but notice a narrow gap. 
Thus, your fight to escape the maze begins.""")
    print(startMap)
    sleep(3)
  
def map(visits):
    if visits == [1]:
        print(j1Map)
    elif visits == [1, 2]:
        print(j12Map)
    elif visits == [1, 2, 1]:
        print(j121Map)
    elif visits == [1, 3]:
        print(j13Map)
    elif visits == [1, 2, 3]:
        print(j123Map)
    elif visits == [1, 3, 4]:
        print(j134Map)
    elif visits == [1, 2, 3, 4, 5]:
        print(j12345Map)
    elif visits == [1, 2, 3, 4]:
        print(j1234Map)
    elif visits == [1, 3, 4, 5]:
        print(j1345Map)

#Junctions
def junction1():
    global lives
    global visits
    if visits.count(1) == 0:
        visits.insert(1, 1)
        map(visits)
    else:
        if visits.count(2) == 1:
            map([1, 2, 1])
        else:
            map(visits)
    print(brightGreen + "Will you choose left or right?")
    retry = 0
    for retry in range(5):
        choice = str(input())
        if choice.lower() == "left":
            junction3()
            break
        elif choice.lower() == "right":
            junction2()
            break
        else:
            print("Please enter 'left' or 'right'.")
            retry += 1
    else:
        if lives > 1:
            print(brightRed + "You kept making invalid choices, the UFO came back and abducted you again. The aliens removed a life, then returned you to the crop circle.")
            lives -= 1
            junction1()
        elif lives == 1:
            print(brightRed + "You were warned... but you kept making invalid choices, and got trapped in the maze forever. You eventually lost every last shred of life left in your boday and were doomed to haunt the maze for the rest of eternity.")
            death()
          
def junction2():
    global visits
    if visits.count(2) == 0:
        visits.append(2)
        map(visits)
    else:
        map(visits)

    directions=["left","right"]
    print(brightGreen+ "You wander through some snaking turns and find the path splits in two.")
    user_input=""
    while user_input not in directions:
        print("Your options are: Left or Right")
        user_input=input().lower()
        if user_input=="left":
            q1()
        elif user_input=="right":
            q2()
          
def junction3():
    global lives
    global visits
    if visits.count(3) == 0:
        visits.append(3)
        map(visits)
    else:
        map(visits)

    if lives <= 0:
        print(brightRed + "You have no lives left. Game over!")
        sleep(2)
        death()
        return

    directions = ["right", "left"]
    print(brightGreen+ "You run into another junction, which way will you go?")
    print("Take the correct turn and you'll be one step closer to making it out of the maze alive!")
    userInput = ""
    
    while userInput not in directions:
        print("Options:Right/Left")
        userInput = input().lower()
        if userInput == "left":
            print("You take a few steps down the dark corridor and the wall of the maze closes behind you!  You took the wrong turn!")
            q3()
        elif userInput == "right":
            print("You chose the right direction keep going, you are almost out!")
            junction4() 
        else:
            print("That's the wrong way!")
          
def junction4(): 
    global visits
    if visits.count(4) == 0:
        visits.append(4)
        map(visits)
    else:
        map(visits)
    print("You stumble onward, reaching yet another fork in the road. When will this end? You think to yourself.")
    userInput = ""
    print("Options: Right/Left")
    userInput = input(": ")
    if userInput.lower() == "right":
            q4()
    elif userInput.lower() == "left":
            junction5()
    else:
            print("Please enter a valid option.")
      
def junction5():
    global visits
    if visits.count(5) == 0:
        visits.append(5)
        map(visits)
    else:
        map(visits)
    directions = ["right","left"]
    print(brightGreen+ "You arrive at another junction which direction do you choose to take: ")
    user_Input = "".lower()
    while user_Input not in directions:
        print("Options: right/left: ")
        user_Input = input()
        if user_Input == "right":
            q5()
        elif user_Input == "left":
            escape()
        else:
            print("Please enter a valid option. ")

#Questions
def q1():
    global lives
    user_options = ["true", "false"]
    print("There are 450 programming languages used in coding.")
    user_input = "".lower()
    while user_input not in user_options:
        print("Options: True/False: ")
        user_input = input()
        if user_input.lower() == "false":
            print("CORRECT! There are actually over 700 programming languages used in coding. You return to the start without losing a life")
            sleep(2)
            junction1()
        elif user_input.lower() == "true":
            lives -= 1
            print(brightRed + f"INCORRECT! There are actually over 700 programming languages used in coding. You have {lives} lives left, ")
            sleep(2)
            print("You return to the start of the maze.")
            if lives <= 0:
                print("You have run out of lives")
                sleep(2)
                death()
            else:
                junction1()
              
def q2():
    global lives
    options=["a","b","c"]
    print(brightGreen + "You find a sign that reads: The world's longest maze is located in Yancheng, China and is "
        "36,000 meters squared in size, What is it's length?") 
    user_input=""
    while user_input not in options:
        print("""
Your options are:
A - 7 km
B - 9 km
C - 15 km
Please enter: A, B or C
    """)
        user_input=input().lower()
        if user_input=="b":
            print("Correct! Hopefully this maze isn't that long.")
            print("You return to the start without losing a life.")
            junction1()
        elif True:
            lives-=1
            print(brightRed + f"Incorrect, you only have {lives} lives left")
            print("You return to the start of the maze.")
            if lives<=0:
                print("You have run out of lives")
                sleep(2)
                death()
            else:
                junction1()
              
def q3():
    print("To go back you'll need to bypass the security system by answering the following question correctly.")
    global lives
    question = "What would a nihilist coder's approach to a morning cup of coffee be?"
    options = [
        "A) Drinking coffee with a sense of purpose, as it is the only thing that matters in life",
        "B) Deciding not to drink coffee because it has no intrinsic value or meaning",
        "C) Drinking an existential blend of coffee, pondering the meaninglessness of life",
        "D) Mixing coding marathons with energy drinks to maximize the futility of existence"
    ]
    print(f"{question}")
    print(options)
    options = ["A", "B", "C", "D"]
    userinput = ""
    while userinput not in options:
        print("Options: A/B/C/D")
        userinput = input().upper()
        if userinput in ["A", "C", "D"]:
            lives -= 1
            print(f"INCORRECT, you only have {lives} lives left, you have gone back to the beginning")
            print("You return to the start of the maze.")
            if lives<=0:
                print("You have run out of lives")
                sleep(2)
                death()
            else:
                visits.remove(3)
                if 2 in visits:
                    visits.remove(2)
                    junction1()
                else:
                    junction1()
        elif userinput == "B":
            print("Correct".upper())
            print("The wall of the maze opens back up and you make your way back to the last junction, you didn't lose any lives")
            junction3()
          
def q4():
    global lives
    print("You must be lost! Before moving ahead, answer me this.. 'True or False: A potato was the first vegetable to be planted on the space shuttle.', if you answer incorrectly you will lose a life'")
    userinput = "".lower()
    print("Options: True/False")
    userinput = input()
    if userinput.lower() == "true":
        print("Correct".upper())
        print("You return to the previous junction without losing a life")
        junction4()
    elif userinput.lower() == "false":
        lives -= 1
        print(brightRed + f"INCORRECT, you only have {lives} lives left")
        print("You return to the start of the maze.")
        if lives<=0:
            print("You have run out of lives")
            sleep(2)
            death()
        else:
            visits.remove(4)
            visits.remove(3)
            if 2 in visits:
                visits.remove(2)
                junction1()
            else:
                junction1()
          
def q5():
    global lives
    user_options = ["true", "false"]
    print("You see a sign that reads 'true or false: A group of jellyfish is called a smack', If you answer incorrectly you will lose a life and be returned to the start of the maze: ")
    user_input = "".lower()
    while user_input not in user_options:
        print("Options: True/False: ")
        user_input = input()
        if user_input == "true":
            print("Correct".upper())
            print("You return to the previous junction with your lives intact")
            junction5()
        elif user_input == "false":
            lives -= 1
            print(brightRed + f"INCORRECT, You only have {lives} lives left, ")
            print("You return to the start of the maze.")
            sleep(2)
            junction1()
            if lives <= 0:
                print("You have run out of lives")
                sleep(2)
                death()
            else:
                visits.remove(5)
                visits.remove(4)
                visits.remove(3)
                if 2 in visits:
                    visits.remove(2)
                    junction1()
                else:
                    junction1()
            
#End of game
def escape():
    print(brightGreen + "Congratulations you have escaped the maze ")
    print(fullMap)
    print("Would you like to restart? ")
    print("Options: Yes/No: ")
    user_Input = "".lower()
    user_Input = input()
    if user_Input == "no":
        print("You choose to forget this ever happened and escape...")
        sleep(2)
        print('"Where am I?"')
        sleep(2)
        credits()
    elif user_Input == "yes":
        # This will restart the game
        print("For some reason you decided to return to the center of the maze")
        sleep(2)
        visits.remove(5)
        visits.remove(4)
        visits.remove(3)
        if 2 in visits:
            visits.remove(2)
            junction1()
        else:
            junction1()
      
def death():
    # This function runs if the player runs out of lives
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +" + dimRed + "           ┌─┐┌─┐┌┬┐┌─┐  ┌─┐┬  ┬┌─┐┬─┐           " + dimMagenta + "+")
    print(brightYellow+ "           |" + dimRed + "           │ ┬├─┤│││├┤   │ │└┐┌┘├┤ ├┬┘           " + brightYellow + "|")
    print(dimMagenta+ "           +" + dimRed + "           └─┘┴ ┴┴ ┴└─┘  └─┘ └┘ └─┘┴└─           " + dimMagenta + "+")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")
    credits()
  
def credits():
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +                             " +dimMagenta+"     .--" +brightMagenta+".----. "+dimMagenta+"     +")
    print(brightYellow+ "           |                            " +dimMagenta+"     / " +brightMagenta+" /      `\\ "+brightYellow+ "   |")
    print(dimMagenta+ "           +" +brightBlue + "      ┌┬┐┌─┐┌┬┐┌─┐  ┌┐ ┬ ┬ " +dimMagenta+"      \\``" +brightMagenta+"\\  .--   \\"+dimMagenta+ "   +")
    print(brightYellow+ "           |" +brightBlue+"      │││├─┤ ││├┤   ├┴┐└┬┘" +dimMagenta+"        \\__" +brightMagenta+"\\/ " +dimMagenta+"\\" +brightMagenta+" \\  :"+brightYellow+ "  "+brightYellow+ " |")
    print(dimMagenta+ "           +" +brightBlue+ "      ┴ ┴┴ ┴─┴┘└─┘  └─┘ ┴  " +dimMagenta+"              ;" +brightMagenta+" ; | "+dimMagenta+ "  +")
    print(brightYellow+ "           |"+ dimRed+"   _                           " +dimMagenta+"         /" +brightMagenta+" /  /  "+brightYellow+ ""+brightYellow+ " |")
    print(dimMagenta+ "           +" + dimRed + "  |\\_\\_ __  __ _  _ __ __   " +dimMagenta+"            \\ " +brightMagenta+"\\  \\  "+dimMagenta+ " +")
    print(brightYellow+ "           |"+dimRed+"  |"+brightBlue+"| |_"+dimRed+"\\"+brightBlue+"__"+dimRed+"\\/\\"+brightBlue+"_"+dimRed+"\\"+brightBlue+"_"+dimRed+"\\\\"+brightBlue+"_"+dimRed+"\\"+brightBlue+"__"+dimRed+"\\"+brightBlue+"___"+dimRed+"\\"+dimMagenta+"      ____   /" +brightMagenta+" :  | "+brightYellow+ "  |")
    print(dimMagenta+ "           +" +dimRed+"  |"+brightBlue+"| __/ _ \\/ _` | '_ ` _  \\ "+dimMagenta+ "   / " +brightMagenta+"  /\\" +dimMagenta+" /" +brightMagenta+" /   :  " +dimMagenta+" +")
    print(brightYellow+ "           |"+dimRed+"  |"+brightBlue+"| |_|  _/ (_| | |"+dimRed+"|"+brightBlue+"| |"+dimRed+"|"+brightBlue+"| | "+dimMagenta+"  /  " +brightMagenta+" /  '--    / "+brightYellow+ "  |")
    print(dimMagenta+ "           +" + brightBlue+ "   \\___\\___|\\__,_|_|"+dimRed+"\\"+brightBlue+"|_|"+dimRed+"\\"+brightBlue+"|_|  "+dimMagenta+" \\'''" +brightMagenta+"\\        /  "+dimMagenta+"  +")
    print(brightYellow+ "           |                       " +dimMagenta+"         \ " +brightMagenta+"  \     .'  " +brightYellow+ "   |")
    print(dimMagenta+ "           +                          " +dimMagenta+"       `--" +brightMagenta+"^----'   " +dimMagenta+ "    +")
    print(brightYellow+ "           |                                                 |")
    print(dimMagenta+ "           +" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+" +brightYellow+"-"+dimMagenta+"+")

#Begin the game
title()
intro()