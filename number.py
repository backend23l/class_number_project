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
        a=self.value
        for i in range(2,a+1):
            if a%i==0:
                return False 
                break
            else :
                return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        if self.is_prime():
            for i in range(1, self.value + 1):
                if self.value % i == 0:
                    divisors.append(i)
                else :
                    continue
            return divisors
        else :
            return "Is prime"

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        k=0
        y=self.value
        while y>0:
            k+=1
            y//=10
        return k

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        k=0
        y=self.value
        for i in self.get_digits():
            k+=i
        return k


    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(str(int(self.value))[::-1]))

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
        for i in  self.get_digits():
            if i>x:
                x=i
            else :
                continue
        return x


    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        x=985412512125112
        for i in  self.get_digits():
            if i<x:
                x=i
            else :
                continue
        return x

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum()/self.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        y=self.value
        x=str(int(y))
        return int(str(x[len(x)//2-1])),int(str(x[len(x)//2])) if len(x)%2==0 else int(str(x[len(x)//2]))
            
    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [self.get_min(),self.get_max()]
    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.
        returns: dict
        """
        x=self.get_digits()
        d={}
        for i in range(len(x)):
            d[x[i]]=d.get(x[i],0)+1
        return d


# Create a new instance of Number
number = Number(51)
# print("number ",number.get_number())
# print("number is odd",number.is_odd())
# print("number is even ",number.is_even())
# print("number is prime ",number.is_prime())
# print("number get divisors",number.get_divisors())
# print("number get lenght ",number.get_length())
# print("number get sum ",number.get_sum())
# print("number get reverse ",number.get_reverse())
# print("number is palindrome ",number.is_palindrome())
# print("number get digits ",number.get_digits())
# print("number get max ",number.get_max())
# print("number get min ",number.get_min())
# print("number get average ",number.get_average())
print("number get median",number.get_median())
print("number get range ",number.get_range())
print("number get frequency ",number.get_frequency())