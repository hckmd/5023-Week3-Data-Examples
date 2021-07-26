import xml.etree.ElementTree as ET

# Parse the recipes xml file, making the recipes variable the root of the tree
tree = ET.parse('recipes.xml')
recipes = tree.getroot()

for recipe in recipes:
    # Get the values of name and serves attributes, assign to variables for printing
    name = recipe.attrib['name']
    serves = recipe.attrib['serves']
    print(f'---\n{name}, serves: {serves}\n')

    # Prints all of the ingredient children data, in <ingredients> tag
    ingredients = recipe.findall('ingredients/ingredient')
    print('Ingredients:')
    for ingredient in ingredients:
        print(f' * {ingredient.text}')
    print(f'---\n')
