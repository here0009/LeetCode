"""
Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.
"""


from threading import Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem = Semaphore()
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n+1, 3):
            if i % 5 != 0:
                self.sem3.acquire()
                printFizz()
                self.sem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n+1, 5):
            if i % 3 != 0:
                self.sem5.acquire()
                printBuzz()
                self.sem.release()
        

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n+1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self.sem.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.sem.acquire()
            if i % 15 == 0:
                self.sem15.release()
            elif i % 5 == 0:
                self.sem5.release()
            elif i % 3 == 0:
                self.sem3.release()
            else:
                printNumber(i)
                self.sem.release()





from threading import Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem = Semaphore()                   # default is 1
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n + 1, 3):
            if i % 5 != 0:
                self.sem3.acquire()
                printFizz()
                self.sem.release()
        

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n + 1, 5):
            if i % 3 != 0:
                self.sem5.acquire()
                printBuzz()
                self.sem.release()
        

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self.sem.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem.acquire()
            if i % 15 == 0:
                self.sem15.release()
            elif i % 5 == 0:
                self.sem5.release()
            elif i % 3 == 0:   
                self.sem3.release()
            else:
                printNumber(i)     
                self.sem.release()