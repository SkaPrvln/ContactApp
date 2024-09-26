import json

class Serializer:
    """
    Static class responsible for serializing and deserializing data.
    """

    @staticmethod
    def save_to_file(data, filename):
        """
        Serializes the given data and saves it to a file.

        Args:
            data (dict): The data to serialize.
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
        except IOError as e:
            raise Exception(f"Error saving data to file: {e}")

    @staticmethod
    def load_from_file(filename):
        """
        Loads and deserializes data from a file.

        Args:
            filename (str): The name of the file to load the data from.

        Returns:
            dict: The deserialized data.
        """
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading data from file: {e}")
