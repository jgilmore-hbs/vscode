#!/usr/bin/env python3
import sys

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    n = 10
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Usage: python fib.py [count]")
            sys.exit(1)
    print(" ".join(str(x) for x in fib(n)))

if __name__ == '__main__':
    main()
