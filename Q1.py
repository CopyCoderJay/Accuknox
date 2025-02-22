"""
By default, Django signals are executed synchronously. This means that when a signal is triggered, its handler runs immediately, blocking the calling thread until the signal handler finishes executing.

To demonstrate this, we can simulate a delay in the signal handler (for example, using time.sleep()) and observe whether the caller waits for the signal handler to complete before continuing.


"""

import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from threading import current_thread

# Define a model to trigger a signal
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that simulates a delay
@receiver(post_save, sender=MyModel)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal started in thread: {current_thread().name}")
    time.sleep(3)  # Simulate a delay
    print(f"Signal finished in thread: {current_thread().name}")

# A function to test if the signal is synchronous
def test_signal_sync():
    print(f"Object creation started in thread: {current_thread().name}")
    instance = MyModel.objects.create(name="Test")
    print(f"Object creation finished in thread: {current_thread().name}")

# Run the test function
test_signal_sync()
"""
Explanation:
Signal Handler: The signal_handler function is connected to the post_save signal for the MyModel model. It simulates a delay of 3 seconds using time.sleep(3).
Test Function: The test_signal_sync function creates a MyModel instance, triggering the post_save signal. Before and after creating the instance, it prints messages to indicate the start and end of the object creation process.
Thread Information: The current_thread().name is printed both in the signal handler and in the main test function to confirm the thread in which the code is executing.
"""
