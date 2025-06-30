'''

⭐) Modularizing Flask Applications with Blueprints

'''


from flask import  render_template , Blueprint

from services.welcome_service import WelcomeService


# Define a new Blueprint named 'welcome
welcome_controller = Blueprint('welcome' , __name__)

# Create an instance of WelcomeService
welcome_service = WelcomeService()

# Define the route within the 'welcome' Blueprint
@welcome_controller.route('/')
def welcome():

    # name = "Madhav P"

    names = welcome_service.get_names()
    # return render_template('Welcome.html', name=name)
    return render_template('Welcome.html', names = names)