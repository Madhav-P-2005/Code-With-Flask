'''

⭐) Managing Business Logic with Service Layer :- A service layer is a design pattern used to abstract and encapsulate the business logic of an application. This separation ensures that your controllers remain clean and focused solely on handling HTTP requests and responses, while the service layer handles the actual logic and data processing.

'''

class WelcomeService:
    def __init__(self):
           # Initialize with a predefined list of names
           self.names = ["Alice", "Bob", "Charlie"]

    # Method to return the list of names
    def get_names(self):
        return  self.names 