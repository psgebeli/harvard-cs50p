# Paul Gebeline, Problem Set 8 

'''

INSTRUCTIONS
------------

Suppose that youd like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with 
these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie 
jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with n🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie
jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jars capacity, though, deposit should instead 
raise a ValueError.

withdraw should remove n cookies from the cookie jar. Nom nom nom. If there arent that many cookies in the cookie jar, though, withdraw 
should instead raise a ValueError.

capacity should return the cookie jars capacity.

size should return the number of cookies actually in the cookie jar, initially 0.

Structure your class per the below. You may not alter these methods parameters, but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively 
test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_jar.py

Note that its not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the 
same “state” (i.e., instance variables). To test one method (e.g., withdraw), then, you might need to call another method first 
(e.g., deposit). But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, as with Pythons own mock object library, so that you can 
call just the one method but modify the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!

'''

class Jar:

    # Initialize a jar with a capacity and a size (# of cookies) starting at 0, where a negative capacity raises a value error.
    def __init__(self, capacity=12):
        
        if capacity < 0:
            raise ValueError('Jar cannot contain a negative amount of cookies')
        self.capacity = capacity 
        self.size = 0 
        
    # Strings support multiplication, so '🍪' * n = '🍪🍪🍪🍪🍪...............🍪'
    #                                               |________________________|
    #                                                       n repetitions
    def __str__(self):
        return '🍪' * self.size

    # Method to deposit n cookies
    def deposit(self, n):

        # Increase size by 1 and decrease n by 1 in increments until n is 0 (then we will have added n cookies)
        while n > 0:
            self.size += 1
            n -= 1 
        
        # If there are more cookies than there is space in the jar, raise a value error
        if self.size > self.capacity:
            raise ValueError('Jar cannot sustain this many cookies')
        
        return self.size
    
    # Method to withdraw n cookies
    def withdraw(self, n):
        
        # Decrease size and n by 1 in increments until n is 0 (then we will have withdrawn n cookies)
        while n > 0:
            self.size -= 1 
            n -= 1
        
        # If there are negative cookies after the withdrawal, raise a value error
        if self.size < 0:
            raise ValueError('You desire more cookies than the Jar possesses, oh greedy one.')
        
        s

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity
    
    # Setter for capacity 
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # Getter for size 
    @property
    def size(self):
        return self._size
    
    # Setter for size 
    @size.setter 
    def size(self, size):
        self._size = size 

# Function to test that the class is working as intended
def test():

    jar = Jar(capacity = 10)
    jar.deposit(3)
    print(jar)

test()