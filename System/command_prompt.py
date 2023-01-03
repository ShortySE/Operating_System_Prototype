import sys

# The commands resemble MS-DOS quite a bit
COMMANDS = ['about', 'open', 'commands', 'shutdown', 'ERASE', 'FORMAT']

# This is the system command prompt or rather a simulation of one
def cd_prompt(username : str):
    cd_running = True
    print("You have now entered the system command prompt")
    while cd_running:
        command = input('cd/'+username+'> ')
        # about returns a string of text about the operating system
        if command == COMMANDS[0]:
            print("This is an operating system simulation primarily inspired by MS-DOS")

        # commands returns a comprehensive set of all the operating system commands
        elif command == COMMANDS[2]:
            print('System commands:')
            print(COMMANDS)

        # shutdown shuts off all system process
        elif command == COMMANDS[3]:
            sys.exit()

        # ERASE is a fail-safe meant to erase every single file present in the user directory
        elif command == COMMANDS[4]:
            print("Erasing all the files present in cd/"+username)

        # FORMAT erases the entire disk including the operating system
        elif command == COMMANDS[5]:
            print("Do you wish to continue? ")
            command = input("Y/N: ")
            if command == 'Y' or command == 'y':
                print("Formatting")
                sys.exit()

            else:
                print("Format terminated")