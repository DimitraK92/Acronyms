from os import system
import signal, menu_handler

def handler(signum, frame):
    system('cls')
    exit(1)

signal.signal(signal.SIGINT, handler)

def main():
    execute = True
    while execute:
        execute = execute_program()

def execute_program():
    menu_handler.display_menu()
    return menu_handler.handle_user_option()

main()
