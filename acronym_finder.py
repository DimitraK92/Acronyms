from os import system, path
import helper, acronym_creator

def find_acronym_choice():
    system('cls')
    retry = True
    while(retry):
        file_name_to_look = helper.get_user_input_lower_stripped('In which text file name do you want to look at?')
        file_path = 'text files/' + file_name_to_look + '.txt'
        if not path.exists(file_path): 
            print('This file was not found.')
            retry = helper.get_user_input_upper_stripped('Do you want to search for another file? Y/N') == 'Y'
        else:
            look_up_in_file(file_path)
            retry = False

def look_up_in_file(file_path):    
    find_more = True
    acronym_to_add = None
    while(find_more):
        acronym = helper.get_user_input_upper_stripped('What is the acronym you want to find?')
        line_in_file = find_acronym_in_file(file_path, acronym)
        if line_in_file != None: 
            print(line_in_file)
            find_more = helper.get_user_input_upper_stripped('Do you want to find another acronym in the same file? Y/N') == 'Y'
        else:    
            print(f'Acronym: {acronym} does not exist.')
            if helper.get_user_input_upper_stripped('Do you want to add it to the file? Y/N') == 'Y': 
                acronym_to_add = acronym
                break
            else: 
                find_more = helper.get_user_input_upper_stripped('Do you want to find another acronym in the same file? Y/N') == 'Y'
        
    if acronym_to_add != None: 
        acronym_creator.add_acronym_to_file(file_path, acronym_to_add)
        if helper.get_user_input_upper_stripped('Do you want to find another acronym in the same file? Y/N') == 'Y':
            look_up_in_file(file_path)

def find_acronym_in_file(file_path, acronym):
        with open(file_path) as file:
            for line in file: 
                if acronym + ' - ' in line.upper(): return line 