# Import the necessary modules
from flask import Flask, render_template, request, jsonify

# Importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# App route for index page
@app.route('/')
def home():
    return render_template('index.html')

# Write a route for POST request
@app.route('/app', methods=['POST'])
def review():
    # Extract the customer_review by writing the appropriate 'key' from the JSON data
    review = request.json.get('input_key')  # Replace 'input_key' with the actual key

    # Check if the customer_review is empty, return an error
    if not review:
        return jsonify({'status': 'error', 'message': 'Empty response'})

    # If review is not empty, pass it through the 'predict' function.
    # predict function returns 2 things: sentiment and path of image in static folder
    # Example: Positive , ./static/assets/emoticons/positive.png
    else:
        sentiment, image_path = sa.predict(review)  # Use the returned values from the predict function

        return jsonify({'sentiment': sentiment, 'image_path': image_path})

# Run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
