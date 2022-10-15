import pygame

pygame.init()

"PART A"



def threePlusOne(n):
  "This is a function that calculates the Collatz Conjecture for any given n value and prints a list of every step along the way."
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (3 * n) + 1
            print(n)

