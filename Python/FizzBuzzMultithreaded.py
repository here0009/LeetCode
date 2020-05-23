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
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        for i in range(1,self.n):
            if i % 15 == 0:
                fizzbuzz()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        printFizz()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        printBuzz()
        

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        printFizzBuzz()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        printNumber(i)
