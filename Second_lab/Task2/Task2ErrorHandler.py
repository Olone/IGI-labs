

class ErrorHandler:

    @staticmethod
    def handle_empty_input():
        print("Error: empty string. Please, try again\n")

    @staticmethod
    def handle_invalid_command():
        print("Error: invalid command. Please try again\n")

    @staticmethod
    def handle_unexpected_error():
        print("Unexpected error appeared, you must be very unique user to unlock this achievement"
              "Lucky you!\n")
