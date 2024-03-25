class BandNameGenerator():
    def __init__(self) -> None:
        print("Welcome to the Band Name Generator")
        self._city = self._get_valid_input("Which city did you grow up in? ")
        self._pet = self._get_valid_input("What is the name of your first pet?")
    
    def generate_band_name(self):
        print(f"Band Name suggestion: {self._city} {self._pet}")
    
    def _get_valid_input(self, prompt):
        while True:
            user_input = input(prompt)
            if self._is_valid_input(user_input):
                return user_input
            print("Input cannot contain special characters or digits. Please try again.")

    def _is_valid_input(self, text):
        return text.isalpha() and not any(char.isdigit() or char in "!@#$%^&*()[]{};:,./<>?\|`~" for char in text)


BandNameGenerator().generate_band_name()
