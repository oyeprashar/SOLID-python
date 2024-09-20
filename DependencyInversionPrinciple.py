"""
In this example, the NotificationManager depends on the abstract Notifier interface, not on concrete implementations. 
This makes it easy to add new notification methods without changing the NotificationManager class.
"""

from abc import ABC, abstractmethod

# Good example (follows DIP)
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Sending email: {message}")

class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_notification(self, message):
        self.notifier.notify(message)

# Usage
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

manager = NotificationManager(email_notifier)
manager.send_notification("Hello via email")

manager = NotificationManager(sms_notifier)
manager.send_notification("Hello via SMS")
