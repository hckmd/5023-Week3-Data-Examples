def show_menu():
  print('\n---')
  print('Example code snippets menu')
  print('1 - Reading a data file')
  print('2 - Writing to a data file and overwriting contents')
  print('3 - Appending to a data file')
  print('4 - Trying to write to a file opened in read mode (causes an exception)')
  print('S - Stop the program')
  print('---')
  menu_item = input('Select menu item: ')
  print()
  if menu_item not in ['S', 's']:
    if menu_item == '1':
      reading_a_data_file()
    elif menu_item == '2':
      overwriting_data_file_contents()
    elif menu_item == '3':
      appending_to_a_data_file()
    elif menu_item == '4':
      writing_a_file_opened_in_read_mode()
    else:
      print('Invalid menu selection. Please try again.')
    show_menu()

def reading_a_data_file():
    print('Reading from the data.txt file as a string and printing contents.')
    with open('data.txt') as file:
        contents = file.read()
        print('Contents:')
        print(contents)

def overwriting_data_file_contents():
    print('Writing a list of strings with fruit names to data file, overwriting existing contents.')

    # Note that all but 1 fruit names have a \n character, so that they are written on new lines in the data file
    fruit_list = ['Watermelon\n', 'Pear\n', 'Nectarine\n', 'Peach\n', 'Blueberry']
    print(f'fruit list: {fruit_list}')

    # Note the 'w' in the open function, which means it will be opened in writing mode
    with open('data.txt', 'w') as file:
        for fruit in fruit_list:
            file.write(fruit)
    print('Finished writing to the data.txt file')

def appending_to_a_data_file():
    print('Appending a list of strings with fruit names to a data file, without overwriting contents')

    # Note that all but 1 fruit names have a \n character, so that they are written on new lines in the data file
    fruit_list = ['\nPineapple\n', 'Guava\n', 'Apricot\n', 'Grape']
    print(f'fruit list: {fruit_list}')

    # Note that 'a' in the open function, which means will be opened in appending mode
    with open('data.txt', 'a') as file:
        for fruit in fruit_list:
            file.write(fruit)
    print('Finished writing to the data.txt file')

def writing_a_file_opened_in_read_mode():
    print('Trying to write a list of strings to a file opened in read mode, which causes an exception')

    # Note that all but 1 vegetable names have a \n character, so that they are written on new lines in the data file
    vegetable_list = ['carrot\n', 'lettuce\n', 'onion\n']

    # Note that no mode (e.g. 'w') is specified in the open function, so the mode will default to read mode
    with open('data.txt') as file:
        for vegetable in vegetable_list:
            file.write(vegetable)

# Mainline of the program
show_menu()