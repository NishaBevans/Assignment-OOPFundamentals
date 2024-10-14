#Task 2: Event Managment System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        self.participant_count += 1  # Increase the count by 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count  # Return the current count


# Demonstration
if __name__ == "__main__":
    # Create an instance of Event
    event = Event("Python Workshop", "2024-10-20")

    # Print initial details
    print(f"Event: {event.name}, Date: {event.date}, Participants: {event.get_participant_count()}")

    # Add participants
    event.add_participant()
    event.add_participant()

    # Get the current participant count
    current_count = event.get_participant_count()
    print(f"Total participants: {current_count}")
