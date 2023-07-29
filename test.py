import unittest
import json
import datetime
from models import User, ParkingSpot, Reservation

# The classes and methods are the same as provided in the previous response.
# ...

class TestCarParkingSystem(unittest.TestCase):
    def setUp(self):
        self.users_data = [
            {
                "user_id": 1,
                "name": "John Doe",
                "phone_number": "1234567890",
                "email": "john@example.com"
            }
        ]

        self.parking_spots_data = [
            {
                "spot_id": 1,
                "latitude": 18.5204,
                "longitude": 73.8567,
                "price_per_hour": 5
            },
            {
                "spot_id": 2,
                "latitude": 18.5167,
                "longitude": 73.8562,
                "price_per_hour": 8
            }
        ]

        self.reservations_data = [
            {
                "parking_spot": {
                    "spot_id": 2,
                    "latitude": 18.5167,
                    "longitude": 73.8562,
                    "price_per_hour": 8
                },
                "hours": 2,
                "timestamp": "2023-07-29 10:30:00"
            }
        ]

        # Load data from sample JSON files
        with open('users.json', 'w') as file:
            json.dump(self.users_data, file)

        with open('parking_spots.json', 'w') as file:
            json.dump(self.parking_spots_data, file)

        with open('reservations.json', 'w') as file:
            json.dump(self.reservations_data, file)

        # Load data into objects for testing
        self.users = User.load_users_from_file('users.json')
        self.parking_spots = ParkingSpot.load_parking_spots_from_file('parking_spots.json')
        self.reservations = Reservation.load_reservations_from_file('reservations.json')

    # The test cases are the same as provided in the previous response.
    # ...

if __name__ == '__main__':
    unittest.main()
