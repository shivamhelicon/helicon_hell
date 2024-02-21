from django.test import TestCase
from .models import Location


class LocationModelTestCase(TestCase):

    def test_location_creation(self):
        location = Location.objects.create(name='Test Location')
        self.assertEqual(location.name, 'Test Location')
        self.assertTrue(location.slug)  # Ensure slug is generated

    def test_location_str_representation(self):
        location = Location.objects.create(name='Test Location')
        self.assertEqual(str(location), 'Test Location')
