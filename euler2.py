def fib():
   a,b = 0,1
   yield a
   yield b
   while 4000000 >= b:
    a,b = b,a+b
    yield b
 

def solve() -> int:
    return sum(filter(lambda x: x % 2 == 0, fib()))