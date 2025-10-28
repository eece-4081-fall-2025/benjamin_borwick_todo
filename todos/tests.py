from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Task
# Create your tests here.
class TaskModelTests(TestCase):
    def test_title_is_required(self):
        # A task should require a title
        t = Task(title="", notes="anything")
        with self.assertRaises(ValidationError):
            t.full_clean()
            