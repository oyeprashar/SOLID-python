"""
we've separated the email functionality into its own class, adhering to SRP. Now, if we need to change how emails are sent, we only modify the EmailService class.
"""

# Bad example (violates SRP)
class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        # Save user to database
        print(f"Saving user {self.name} to database")

    def send_email(self, message):
        # Send email to user
        print(f"Sending email to {self.name}: {message}")

# Good example (follows SRP)
class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        # Save user to database
        print(f"Saving user {self.name} to database")

class EmailService:
    @staticmethod
    def send_email(user, message):
        # Send email to user
        print(f"Sending email to {user.name}: {message}")
