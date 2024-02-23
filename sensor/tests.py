from django.test import TestCase
from .models import Location
from .models import Sensor


class LocationModelTestCase(TestCase):

    def test_location_creation(self):
        location = Location.objects.create(name='Test Location')
        self.assertEqual(location.name, 'Test Location')
        self.assertTrue(location.slug)  # Ensure slug is generated

    def test_location_str_representation(self):
        location = Location.objects.create(name='Test Location')
        self.assertEqual(str(location), 'Test Location')


class SensorModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location')

    def test_sensor_creation(self):
        sensor = Sensor.objects.create(name='Test Sensor', location=self.location)
        self.assertEqual(sensor.name, 'Test Sensor')
        self.assertEqual(sensor.location, self.location)

    def test_sensor_unique_together(self):
        # Create a sensor with the same name and location
        Sensor.objects.create(name='Test Sensor', location=self.location)

        # Attempt to create another sensor with the same name and location
        with self.assertRaises(Exception):
            Sensor.objects.create(name='Test Sensor', location=self.location)

    def test_sensor_description_optional(self):
        sensor = Sensor.objects.create(name='Test Sensor', location=self.location)
        self.assertIsNone(sensor.description)

    def test_sensor_str_representation(self):
        sensor = Sensor.objects.create(name='Test Sensor', location=self.location)
        expected_str = f'{sensor.name} ({sensor.location})'
        self.assertEqual(str(sensor), expected_str)