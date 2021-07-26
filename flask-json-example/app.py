from flask import Flask

app = Flask(__name__)

@app.route('/')
def game_sales_data():
    sales_data = {
        'game_sales': [
            {'title': 'Bomberman Land Touch!', 'platform': 'Nintendo DS', 'review_score': 78, 'sales_in_millions': 0.04},
            {'title':'Bomberman', 'platform': 'Nintendo DS',  'review_score': 75, 'sales_in_millions': 0.11},
            {'title':'Bomberman Land',  'platform': 'Nintendo Wii', 'review_score': 57, 'sales_in_millions': 0.12},
            {'title':'Bomberman: Act Zero', 'platform': 'Xbox 360', 'review_score': 34, 'sales_in_millions': 0.04}
        ]
    }
    return sales_data