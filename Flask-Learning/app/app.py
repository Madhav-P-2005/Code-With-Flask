'''
⭐) Importing and Initializing Flask  And  Displaying Dynamic Content with Jinja2 Templates 

'''

# Import the Flask class from the flask package 
from flask import Flask , render_template


'''

⭐) Integrating the Blueprint with the Flask Application


a) Model :-   Represents the data and business logic of the application. We will cover models in more detail in a future lesson.

b) View  :-  Represents the user interface and presentation layer. So far, you have seen views as templates rendered with Jinja2 in Flask.

c) Controller :-  Acts as an intermediary between Model and View. It processes user input, interacts with the Model, and selects the View to display accordingly.

'''

from controllers.welcome_controller import welcome_controller


# Create an instance of the Flask class
app = Flask(__name__)


# Registering the Blueprint
app.register_blueprint(welcome_controller)


# Define a Route and View Function 
@app.route('/')

# Define a view function associated with the route 
def welcome():
    # return "<H1>Welcome to your Flask App<H2>"

    # Render the 'Welcome.html' template from the 'templates' directory
    # return render_template('Welcome.html')


    # Define a variable with some value
    name = "Madhav P"

    # Pass the Variablle to the 'Welcome.html' Template
    return render_template('Welcome.html' , name=name)

    
# Check if the script is run directly 

'''

⭐)  # Run this block of code only if this file is executed directly (like python app.py) — and not when this file is imported into another Python file as a module

'''

if __name__ == '__main__':   

    # Run the Flask application
    app.run(host='0.0.0.0' , port=3000, debug=True)