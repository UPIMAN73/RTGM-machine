def thelp():
    print("help")

def tsave():
    print("save")

user_input = ""
commands = {"help":thelp, "save":tsave, "quit":exit}
user_loop = True

try:
    while user_input != "bla":
        user_input = raw_input("> ")
        print(user_input)
        if (user_input in commands):
            commands[user_input]()
        else:
            print("Command does not exist")
            commands.get("help", lambda:"INVALID")()

finally:
    print("GOOD BYE")