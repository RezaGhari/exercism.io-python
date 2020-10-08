from random import choices, seed
from string import ascii_uppercase, digits

class Robot:
    """
    Each Robot class instance will be a random 5-character name consisted of two uppercase
    alphabets followed by three digits.
    """
    def __init__(self):
        """
    	By making any instance of Robot class, the reset() method will be called.
        """
        Robot.reset(self)

    def reset(self):
        """
    	By calling reset() method, a random robot name will be generated using
        generate_name() method.
        """
        self.name = self.generate_name()

    def generate_name(self):
        """
        This method firstly seeds the random by the current time
        and returns a random string in the form of the followng examples:
        AB123, CH575, LJ952
        """
        seed()
        return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
    
    def __repr__(self):
        """
        This is optional and not required by the question
        """
        return self.name