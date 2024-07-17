from os import system, path
import helper, acronym_finder

def add_acronym_choice():
    system('cls')
    file_name_to_add_acronym = input("In which text file name do you add the acronym? If it doesn't exist, we will create it for you!\n")
    file_path = 'text files/' + file_name_to_add_acronym + '.txt'
    add_more = True
    while(add_more):
        acronym = input('Which acronym do you want to add?\n')
        add_acronym_to_file(file_path, str(acronym).upper())
        add_more = helper.get_user_input_upper_stripped('Do you want to add another one? Y/N') == 'Y'

def add_acronym_to_file(file_path, acronym):
    if path.exists(file_path):
        line_in_file = acronym_finder.find_acronym_in_file(file_path, acronym)
        if line_in_file != None: 
            print(f'Acronym {acronym} already exists:\n{line_in_file}')
            return
    with open(file_path, 'a') as file:
        definition = input(f'What is {acronym} definition?\n').title()
        file.write(acronym + ' - ' + definition + '\n')
        print('Acronym was successfully added.')