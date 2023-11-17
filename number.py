class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        for i in range(2, self.value):
            if self.value % i:
                return False

        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                divisors.append(i)

        return divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        c=0
        while self.value>0:
            a=self.value%10
            self.value //=10
            c+=1
        return c
    
    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        sum = 0
        while self.value>0:
            a = self.value%10
            self.value //=10
            sum+=a
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        while self.value>0:
            a = self.value%10
        pass

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        pass

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        pass

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        pass

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        pass

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass


# Create a new instance of Number
number = Number(30)
print(number.get_divisors())
