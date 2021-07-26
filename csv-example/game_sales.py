'''
 Data excerpt has originated from the video games sale data set available from: 
    https://corgis-edu.github.io/corgis/csv/video_games/
'''
import csv
from os import write

def write_data_to_a_csv_file():
    # Create a list of dictionaries 
    game_sales = [
        {'title': 'Bomberman Land Touch!', 'platform': 'Nintendo DS', 'review_score': 78, 'sales_in_millions': 0.04},
        {'title':'Bomberman', 'platform': 'Nintendo DS',  'review_score': 75, 'sales_in_millions': 0.11},
        {'title':'Bomberman Land',  'platform': 'Nintendo Wii', 'review_score': 57, 'sales_in_millions': 0.12},
        {'title':'Bomberman: Act Zero', 'platform': 'Xbox 360', 'review_score': 34, 'sales_in_millions': 0.04}
    ]
    number_of_games = len(game_sales)

    # Open the file and create a DictWriter to write the data to the file
    with open('bomberman_sales.csv', 'w', newline='') as file:
        header_row = ['title', 'platform', 'review_score', 'sales_in_millions']
        writer = csv.DictWriter(file, fieldnames = header_row)
        writer.writeheader()
        writer.writerows(game_sales)

    print(f'Successfully wrote {number_of_games} game sales records to the file.')

def read_data_from_a_csv_file():
    # Create a list that we'll use to access the data after the data file has closed
    game_sales = []

    # Open the file and create a DictReader to read the data from the file
    with open('bomberman_sales.csv') as file:
        reader = csv.DictReader(file)
        # Iterate through each row in the file and add them to the game_sales list
        for row in reader:
            game_sales.append(row)

    # Once the file has closed, iterate through the list of dictionaries with sales data
    for game in game_sales:
        print(game)

print('Writing the sales data to a csv file\n---')
write_data_to_a_csv_file()
print('\n---\n')
print('Reading the sales data from a csv file\n---')
read_data_from_a_csv_file()
print('---')