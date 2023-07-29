# models.py
import json
import datetime

class User:
    def __init__(self, user_id, name, phone_number, email):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.reservations = []

    def reserve_parking_spot(self, parking_spot, hours):
        reservation = Reservation(parking_spot, hours)
        self.reservations.append(reservation)
        return reservation

    @staticmethod
    def load_users_from_file(file_path):
        with open(file_path, 'r') as file:
            users_data = json.load(file)
        return [User(**user_data) for user_data in users_data]

    def save_to_file(self, file_path):
        with open(file_path, 'a') as file:
            json.dump(self.__dict__, file)
            file.write('\n')

class ParkingSpot:
    def __init__(self, spot_id, latitude, longitude, price_per_hour):
        self.spot_id = spot_id
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_hour = price_per_hour


    @staticmethod
    def load_parking_spots_from_file(file_path):
        with open(file_path, 'r') as file:
            parking_spots_data = json.load(file)
        return [ParkingSpot(**spot_data) for spot_data in parking_spots_data]

    def save_to_file(self, file_path):
        with open(file_path, 'a') as file:
            json.dump(self.__dict__, file)
            file.write('\n')

class Reservation:
    def __init__(self, parking_spot, hours):
        self.parking_spot = parking_spot
        self.hours = hours
        self.timestamp = datetime.datetime.now()

    def calculate_total_price(self):
        return self.parking_spot.price_per_hour * self.hours

    def get_parking_spot_details(self):
        return {
            'spot_id': self.parking_spot.spot_id,
            'latitude': self.parking_spot.latitude,
            'longitude': self.parking_spot.longitude,
            'price_per_hour': self.parking_spot.price_per_hour,
            'hours': self.hours,
            'total_price': self.calculate_total_price()
        }

    @staticmethod
    def load_reservations_from_file(file_path):
        with open(file_path, 'r') as file:
            reservations_data = json.load(file)
        return [Reservation(**res_data) for res_data in reservations_data]

    def save_to_file(self, file_path):
        with open(file_path, 'a') as file:
            json.dump(self.__dict__, file)
            file.write('\n')

# Test data
if __name__ == '__main__':
    user = User(user_id=1, name='John Doe', phone_number='1234567890', email='john@example.com')
    parking_spot = ParkingSpot(spot_id=1, latitude=18.5204, longitude=73.8567, price_per_hour=5)
    reservation = user.reserve_parking_spot(parking_spot, hours=3)

    # Save data to files
    User.save_to_file('users.json')
    ParkingSpot.save_to_file('parking_spots.json')
    Reservation.save_to_file('reservations.json')