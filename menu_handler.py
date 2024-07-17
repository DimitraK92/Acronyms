from os import system
import acronym_finder, acronym_creator

def display_menu():
    system('cls')
    print('Menu\n')
    print('Find an acronym (F)')
    print('Add an acronym (A)')
    print('Exit (E)')
    print()
    print('Please select an option!')
        
def handle_user_option():
    user_choice = input().upper()
    if user_choice == 'F':
        acronym_finder.find_acronym_choice()
        return True
    elif user_choice == 'A':
        acronym_creator.add_acronym_choice()
        return True
    elif user_choice == 'E':
        system('clear')
        return False
    else: 
        if input('Incorrect option. Do you want to try again(T) or exit(E)!\n').capitalize() == 'T':
            return True