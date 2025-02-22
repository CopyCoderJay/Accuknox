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
