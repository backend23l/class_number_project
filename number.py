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
        k=0
        y=self.value
        while y>0:
            y//=10
        return k

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        k=0
        y=self.value
        while y>0:
            k+=y%10
            y//=10
        return k


    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        x=str(int(self.value))
        return int(str(x[::-1]))

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return True if str(int(self.value))[::-1]==str(int(self.value)) else False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        l=[]
        y=self.value
        while y>0:
            l.append(y%10)
            y//=10
        return l

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        x=-985412512125112
        y=self.value
        while y>0:
            if y%10>x:
                x=y%10
            y//=10
        return x


    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        x=985412512125112
        y=self.value
        while y>0:
            if y%10<x:
                x=y%10
            y//=10
        return x

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        s=0
        k=0
        y=self.value
        while y>0:
            s+=y%10
            k+=1
            y//=10
        return s/k

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        y=self.value
        x=str(int(y))
        if len(x)%2==0:
            return int(str(x[len(x)//2-1])),int(str(x[len(x)//2]))
        else :
            return int(str(x[len(x)//2]))
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
number = Number(123)
print(number.get_median())
