import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError
import time

# Define a model to trigger a signal
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that prints the current thread
@receiver(post_save, sender=MyModel)
def print_thread(sender, instance, **kwargs):
    print(f"Signal triggered for {instance.name} in thread: {threading.current_thread().name}")

# A function to test if the signal runs in the same thread
def test_signal_thread():
    # The print statement in the signal will show which thread it runs in
    instance = MyModel.objects.create(name="Test")
    print(f"Object saved in thread: {threading.current_thread().name}")

# Start the test in a new thread to see the behavior
def run_in_thread():
    thread = threading.Thread(target=test_signal_thread)
    thread.start()
    thread.join()  # Wait for the thread to finish

# Run the test
run_in_thread()