class Contact:
    """
    Class representing a contact with a name and phone number.

    Attributes:
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
    """

    def __init__(self, name, phone):
        """
        Initializes a Contact instance.

        Args:
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
        """
        self._name = None
        self._phone = None
        self.name = name
        self.phone = phone

    @property
    def name(self):
        """
        str: Returns the name of the contact.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the contact. The name must be at least 3 characters long.

        Args:
            value (str): The name to assign.

        Raises:
            ValueError: If the name is less than 3 characters.
        """
        if not value or len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    @property
    def phone(self):
        """
        str: Returns the phone number of the contact.
        """
        return self._phone

    @phone.setter
    def phone(self, value):
        """
        Sets the phone number of the contact. The phone number must be numeric and at least 5 digits long.

        Args:
            value (str): The phone number to assign.

        Raises:
            ValueError: If the phone number is less than 5 digits or not numeric.
        """
        if not value.isdigit() or len(value) < 5:
            raise ValueError("Phone number must be at least 5 digits long.")
        self._phone = value

    def __str__(self):
        return f"{self.name}: {self.phone}"
