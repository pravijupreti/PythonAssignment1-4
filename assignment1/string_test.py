class StringTester:
    def tester(self, givenstring="Too short"):  # Note that 'self' is required
        if len(givenstring) < 10:
            print("Too short")
        else:
            print(givenstring)

if __name__ == "__main__":
    stringTester = StringTester()
    stringTester.tester()  # Call the method on the instance
