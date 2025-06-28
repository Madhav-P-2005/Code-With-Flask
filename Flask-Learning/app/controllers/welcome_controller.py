'''

⭐) Modularizing Flask Applications with Blueprints

'''


from flask import  render_template , Blueprint


# Define a new Blueprint named 'welcome
welcome_controller = Blueprint('welcome' , __name__)


# Define the route within the 'welcome' Blueprint
@welcome_controller.route('/')
def welcome():
    name = "Madhav P"
    return render_template('Welcome.html', name=name)