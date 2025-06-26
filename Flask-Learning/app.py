'''
⭐) Importing and Initializing Flask 

'''

# Import the Flask class from the flask package 
from flask import Flask


# Create an instance of the Flask class
app = Flask(__name__)


# Define a Route and View Function 
@app.route('/')

# Define a view function associated with the route 
def welcome():
    return "<H1>Welcome to your Flask App<H2>"

    
# Check if the script is run directly 

'''

⭐)  # Run this block of code only if this file is executed directly (like python app.py) — and not when this file is imported into another Python file as a module

'''

if __name__ == '__main__':   

    # Run the Flask application
    app.run(host='0.0.0.0' , port=3000, debug=True)