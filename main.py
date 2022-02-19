# Packages
global packages_call
packages_call = False

cmdlist = ["kill", "echo", "package"]
packages = ["call"]

def kill():
    print("Killing...")
def echo():
    txt = input("text> ")
    print("\"" + txt + "\"")
    cmd()
def package():
    print("What Package Would You Like To Install?")
    pkg = input("> ")
    if pkg == "call":
        packages_call = True
        print("Call = True")
    cmd()

def cmd():
    command = input("> ")
    if command == "kill":
        kill()
    elif command == "echo":
        echo()
    elif command == "package":
        package()
    elif command == "call":
        if packages_call:
            print("E")
    else:
        print("Command Not Recognised")
        print("Try Again")
        cmd()

cmd()