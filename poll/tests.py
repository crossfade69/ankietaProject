from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse
from .models import Poll

class AccessTests(TestCase):
    def setUp(self):
        # Create a poll for testing
        self.poll = Poll.objects.create(is_active=True)

    def test_access_without_code_redirects(self):
        response = self.client.get(reverse('vote'))
        self.assertRedirects(response, reverse('access'))

    def test_access_with_code_allows_entry(self):
        # Set the session flag indicating the user has entered the code
        self.client.session['has_entered_code'] = True
        self.client.session.save()

        response = self.client.get(reverse('vote'))
        print(response.status_code)  # Print the actual status code for debugging
        print(response.content)      # Print the response content for debugging
        location_header = response.headers.get('Location')
        print(location_header)  # Print the Location header for debugging

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/vote.html')
class PollStateTests(TestCase):
    def setUp(self):
        # Create a poll for testing
        self.poll = Poll.objects.create(is_active=True)

    def test_inactive_poll_displays_not_ready_page(self):
        self.client.session['has_entered_code'] = True
        self.client.session.save()

        # Set the poll as inactive
        self.poll.is_active = False
        self.poll.save()

        response = self.client.get(reverse('vote'))
        self.assertTemplateUsed(response, 'poll/notready.html')

class VoteSubmissionTests(TestCase):
    def setUp(self):
        # Create a poll for testing
        self.poll = Poll.objects.create(is_active=True)

    def test_vote_submission_increases_option_count(self):
        self.client.session['has_entered_code'] = True
        self.client.session.save()

        # Simulate a POST request with a selected option
        response = self.client.post(reverse('vote'), {'poll': 'option_a'})
        self.assertRedirects(response, reverse('thankyou'))

        # Reload the poll from the database to get the updated counts
        self.poll.refresh_from_db()

        # Assert that the count for 'option_a' has increased
        self.assertEqual(self.poll.option_a_count, 1)

    def test_invalid_form_option_returns_error(self):
        self.client.session['has_entered_code'] = True
        self.client.session.save()

        # Simulate a POST request with an invalid option
        response = self.client.post(reverse('vote'), {'poll': 'invalid_option'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid form option')