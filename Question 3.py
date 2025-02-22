"""
In Django, signals run in the same database transaction as the caller by default.
This means that if a signal handler modifies the database within the context of a transaction, 
the changes will be committed or rolled back together with the original transaction.
"""
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

# Define a model to trigger a signal
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler that modifies the database
@receiver(post_save, sender=MyModel)
def modify_on_save(sender, instance, **kwargs):
    # This will run in the same transaction as the save call
    print(f"Signal triggered for {instance.name}")
    # Intentionally causing an error to demonstrate transaction rollback
    if instance.name == "Test":
        raise IntegrityError("Intentional error to test rollback")

# A function to test the signal behavior within a transaction
def test_signal_transaction():
    try:
        with transaction.atomic():  # This starts a database transaction
            instance = MyModel.objects.create(name="Test")
            print("Object saved")
    except IntegrityError:
        print("Caught IntegrityError, transaction will be rolled back")

# Call the test function
test_signal_transaction()
