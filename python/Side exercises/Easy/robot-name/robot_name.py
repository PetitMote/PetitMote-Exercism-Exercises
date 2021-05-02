import random
import string


def random_robot_name() -> str:
    """Generate a robot name, with 2 letters and 3 digits (XX000)
    """
    random.seed()  # Avoid generating the same name 2 times
    letters = ""
    numbers = ""
    letters = letters.join(random.choices(string.ascii_uppercase, k=2))
    numbers = numbers.join(random.choices(string.digits, k=3))
    return letters + numbers


class Robot:

    names_list = []

    def __init__(self):
        self.generate_name()

    def reset(self):
        """Generate a new name for the robot
        """
        self.names_list.remove(self.name)
        self.generate_name()

    def generate_name(self):
        """Generate a name not already used, and add it to the list of used names
        """
        self.name = random_robot_name()
        while self.name in self.names_list:
            self.name = random_robot_name()
        self.names_list.append(self.name)
