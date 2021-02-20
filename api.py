import requests
import unittest
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/reviews/', methods=['GET'])
def get_reviews():
    reviews = []
    
    url = request.args.get('url')

    try: 
        page = requests.get(url)
    except requests.exceptions.HTTPError as err:
        print ("Http Error:", err)
        
    content = BeautifulSoup(page.content, 'html.parser')
    lender_title = content.find("h1")
    review_dates = content.find_all("p", class_="consumerReviewDate")
    authors = content.find_all("p", class_="consumerName")
    review_texts = content.find_all("p", class_="reviewText")
    review_stars = content.find_all("div", class_="numRec")
    

    for (review_date, review_text, stars, author) in zip(review_dates, review_texts, review_stars, authors):
        reviews.append({"text": review_text.text, "date": review_date.text, "star_rating": stars.text, "author": author.text })

    response = {
        "lender": lender_title.text,
        "reviews": reviews
    }
        
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
