
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Aircraft, Booking
from accounts.forms import UserSignUpForm



class MyViewTestCase(TestCase):
    def test_my_view(self):
        url = reverse('my_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
def test_login(self):
        url = reverse('engineer')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


def test_login(self):
        url = reverse('Planes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



class MyPlaneTests(TestCase):
    def setUp(self):
        Aircraft.objects.create(id="1", currentSpeed="10", model ="Cesna", fuelCapacity=100, timeForInspection="2023-04-26", description="Nice test", image="media/pics/oip.jpg", availability=True)
        Aircraft.objects.create(id="2", currentSpeed="10", model ="Cesna", fuelCapacity=90, timeForInspection="2023-04-25", description="Nice test 2", image="media/pics/oip (1).jpg", availability=True)
    def test_PlaneCreation(self):
        count =Aircraft.objects.count()
        self.assertNotEqual(count, 0)


class BookAircraftViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.aircraft = Aircraft.objects.create(id="3", currentSpeed="10", model ="Cesna", fuelCapacity=100, timeForInspection="2023-04-26", description="Nice test", image="media/pics/oip.jpg", availability=True)
        form_data = {
            'username': 'testuser2',
            'password1': 'NotEasyPassword124^',
            'password2': 'NotEasyPassword124^',
            'email': 'testuser2@example.com',
        }
        form = UserSignUpForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
      
        self.user = form.save()
        print(self.user.username)
        self.url = reverse('book_aircraft')

    def test_anonymous_user_redirected(self):
        """Test that an anonymous user is redirected to the login page."""
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_logged_in_user_can_book_aircraft(self):
        """Test that a logged-in user can book an aircraft."""
        self.client.login(username='testuser2', password='NotEasyPassword124^')

        # Create a booking for the aircraft
        start_time = datetime.now() + timedelta(hours=1)
        end_time = start_time + timedelta(hours=2)
        response = self.client.post(self.url, {
            'aircraft_id': self.aircraft.id,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
        })

        # Check that the booking was created
        booking = Booking.objects.first()
        print(booking)
        print("here here")
        self.assertEqual(booking.aircraft, self.aircraft)
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.status, 'Pending')
        self.assertTrue(self.aircraft.availability)


    def test_missing_required_fields(self):
        """Test that an error is shown when required fields are missing."""
        self.client.login(username='testuser2', password='NotEasyPassword124^')
        response = self.client.post(self.url, {})
        self.assertContains(response, 'Missing required fields')

    # def test_invalid_datetime_format(self):
    #     """Test that an error is shown when an invalid datetime format is provided."""
    #     self.client.login(username='testuser2', password='NotEasyPassword124^')
    #     response = self.client.post(self.url, {
    #         'aircraft_id': self.aircraft.id,
    #         'start_time': 'invalid_datetime',
    #         'end_time': 'invalid_datetime',
    #     })
    #     self.assertContains(response, 'Invalid datetime format')

    def test_end_time_before_start_time(self):
        """Test that an error is shown when the end time is before the start time."""
        self.client.login(username='testuser2', password='NotEasyPassword124^')
        response = self.client.post(self.url, {
            'aircraft_id': self.aircraft.id,
            'start_time': '2023-05-09T12:00:00',
            'end_time': '2023-05-09T11:00:00',
        })
        self.assertContains(response, 'End time must be after start time')

    
