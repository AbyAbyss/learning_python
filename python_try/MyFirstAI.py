aiName = "THinKING_For_a_NaMe"
greetings = ['hi' , 'HI' , 'Hi' , 'HEY' , 'hey' , 'Hey' ,'Hey there','hi there', 'Hey There' , 'Hi There','Hi there', 'HI there', 'HI There','Hello','hello','Hello there','Hello There','hello there']
asking = ['What are you doing?','what are you doing?','Whats up','sup','Sup','wyd','WYD','So, What are you doing?']
yEs = ['yes','YES','Yes','Positive']
nO = ['NO','no','No','naa','na']
print("Hello there")
print("this is my first AI code...and ya its a bit simple\n..okay okay....way to simple...\n\nbut still give it a try..please")
name = input("please enter your name ")
print("\n")
print("\n")
print("Hello",name,"\nMy name is",aiName,"Lets have a fun conversation\n")

print("Starting AI.....")

while True:
    userInput = input(">>>")
    if userInput in greetings:
        print("Hello,",name)
    elif userInput in ['stop','STOP','BYE','bye']:
        print("So soon...was i boring??...ahhh..its okay..\nmy developer will find a way to make me more fun...\n\tSee you",name)
        exit()
    elif userInput in asking:
        print("I am talking to my friend",name,"\nAnd i know evn doing the same..but are you doing any additional work??")
        while True:
            uI = input(">>>")
            if uI in yEs:
                print("What is it, tell me")
                work = input("<<<")
                print("Ohh, cool..\n",name,"are you free to text me??")
                while True:
                    uI2 = input("<<<")
                    if uI2 in yEs:
                        print("That's cool..I am happy to hear that")
                        break
                    elif uI2 in nO:
                        print("What big work you have...Shut and text me nowwww..")
                        break
                    #break    
            elif uI in ['okay','ok','OK','yes','Yes','YES']:
                print("hehehehh..coooool.",aiName,"is happy\n>>> tell something")
                break
            elif uI in nO:
                print("please text know...so bad of you..\n\nbut if you really busy then just say bye or stop")
                break
    else:
        print("I did not understand what you are saying")
