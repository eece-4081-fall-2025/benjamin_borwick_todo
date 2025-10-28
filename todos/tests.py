from django.test import TestCase
from django.test import TestCase

class TaskCreateViewTests(TestCase):
    def test_get_new_task_form(self):
        resp = self.client.get(reverse('task_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<form')

    def test_post_valid_creates_task_and_redirects(self):
        data = {'title': 'Buy milk', 'notes': '2% at Kroger'}
        resp = self.client.post(reverse('task_create'), data)
        self.assertRedirects(resp, reverse('task_list'))
        from .models import Task
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Buy milk')

    def test_post_invalid_rerenders_with_errors(self):
        data = {'title': '', 'notes': 'oops'}
        resp = self.client.post(reverse('task_create'), data)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "This field is required")
