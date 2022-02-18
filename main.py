packages_call = True
cmdlist = ["kill", "echo"]
packages = ["call", "package"]

def kill():
    print("Killing...")
def echo():
    txt = input("text> ")
    print("\"" + txt + "\"")
    cmd()

def cmd():
    command = input("> ")
    if command == "kill":
        kill()
    elif command == "echo":
        echo()
    else:
        print("Command Not Recognised")
        print("Try Again")
        cmd()

cmd()