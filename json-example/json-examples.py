import json

def show_menu():
    print('\n---')
    print('Example code snippets menu')
    print('1 - Load data from a JSON file')
    print('2 - Load data from a JSON string')
    print('3 - Write data to a JSON file')
    print('4 - Write data to a JSON string')
    print('5 - Write data to a JSON file with indentation')
    print('S - Stop the program')
    print('---')
    menu_item = input('Select menu item: ')
    print()
    if menu_item not in ['S', 's']:
        if menu_item == '1':
            load_data_from_json_file()
        elif menu_item == '2':
            load_data_from_json_string()
        elif menu_item == '3':
            write_data_to_a_json_file()
        elif menu_item == '4':
            write_data_to_json_string()
        elif menu_item == '5':
            write_data_to_a_json_file_with_indentation()
        else:
            print('Invalid menu selection. Please try again.')
        show_menu()

def load_data_from_json_file():
    # Declare the data dictionary before the with statement,
    # so that we can access it after the file has closed.
    recipes_data = {}
    with open('recipes-original.json') as file:
        recipes_data = json.load(file)
    
    # Iterate through each of the recipes in the "recipes" list in the data
    # and print details of each recipe
    recipes = recipes_data['recipes']
    for recipe in recipes:
        # Get the values of name and serves attributes, assign to variables for printing
        name = recipe['name']
        serves = recipe['serves']
        print(f'---\n{name}, serves: {serves}\n')

        # Prints all of the ingredient children data, from ingredients list
        ingredients = recipe['ingredients']
        for ingredient in ingredients:
            print(f' * {ingredient}')
        print(f'---\n')
    
def load_data_from_json_string():
    # Create a string that has data about countries in JSON format
    data = '{"countries": [' + \
        '{"name": "Estonia", "population_millions": 1.3, "neighbours": ["Latvia", "Russia"]},' + \
        '{"name": "Belarus", "population_millions": 9.5, "neighbours": ["Lithuania", "Latvia", "Poland", "Russia", "Ukraine"]}' + \
        ']}'
    print(f'String to parse as JSON data: {data}')

    # Load the JSON string into a dictionary
    data_dict = json.loads(data)
    print(f"Loaded the JSON data into a dictionary")
    
    countries = data_dict['countries']
    for country in countries:
        # Assign name and population to variables for printing
        name = country['name']
        population = country['population_millions']
        print(f'\nCountry: {name}')
        print(f'Population (in millions): {population}\n')

        # Iterate through the neighbouring countries for the country
        print('Neighbours:')
        neighbours = country['neighbours']
        for neighbour in neighbours:
            print(f'* {neighbour}')
        print('---')

def write_data_to_a_json_file():
    # Create a dictionary of lists for writing to json file
    favourite_recipes = {
        'recipes': [
            {
                'name': 'Nachos',
                'serves': 4,
                'ingredients': [
                    '8 cherry tomatoes', '100g natural corn chips',
                    '2/3 cup Hommus', '1/4 cup fresh parsley'
                ]
            },
            {
                'name': 'Mushroom Risotto',
                'serves': 4,
                'ingredients': [
                    '2 cups mushrooms, sliced', '1 cup Arborio rice',
                    '4 cups vegetable stock', '1 cup grated Parmesan cheese'
                ]
            }
        ]
    }
    number_of_recipes = len(favourite_recipes['recipes'])

    # Open a file and write the dictionary of lists to file in json format
    with open('favourite-recipes.json', 'w') as file:
        json.dump(favourite_recipes, file)
    print(f'Wrote {number_of_recipes} recipes to a json file')

def write_data_to_json_string():
    # Create a dictionary with data for two countries
    countries_data = {
        'countries': [
            {
                'name': 'Latvia',
                'population_in_millions': 1.9,
                'countries': ['Belarus', 'Estonia', 'Lithuania', 'Russia']
            },
            {
                'name': 'Finland',
                'population_in_millions': 5.5,
                'countries': ['Norway', 'Russia', 'Sweden']
            }
        ]
    }
    # Write the countries data to a string in JSON format
    countries_string = json.dumps(countries_data)
    print('String created with json.dumps printed below:\n')
    print(countries_string)

def write_data_to_a_json_file_with_indentation():
    # Open a json file with recipes that has no indentation
    recipe_data = {}
    with open('recipes-no-format.json') as file:
        recipe_data = json.load(file)
    
    # Create a json file and write the recipes data with indentation (note the indent argument)
    with open('recipes-indentation.json', 'w') as file:
        json.dump(recipe_data, file, indent=4)
    print("\nWrote the data to the 'recipes-indentation.json' file, with indent of 4 spaces.\n")

# Mainline of the program
show_menu()