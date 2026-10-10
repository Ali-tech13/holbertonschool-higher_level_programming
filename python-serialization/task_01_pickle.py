
#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle


class CustomObject:
    """Represent a custom object with personal attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError,
                AttributeError, ImportError, ValueError, TypeError):
            return None
