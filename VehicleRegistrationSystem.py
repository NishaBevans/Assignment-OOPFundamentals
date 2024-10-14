class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")


if __name__ == "__main__":
    vehicle1 = Vehicle("ABC123", "Car", "Alice")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")

    print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

    vehicle1.update_owner("Charlie")
    vehicle2.update_owner("Diana")

    print(f"Updated Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Updated Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
