# FizzBuzz Game

## Overview

This Python script implements the classic "FizzBuzz" game. In this game, you count numbers from 1 to 99, but instead of saying the number, you say "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, and "Fizz Buzz" if it's divisible by both 3 and 5. If the number is not divisible by 3 or 5, you simply say the number itself.

## Usage

1. Run the script by executing `python fizz_buzz_game.py` in your terminal.
2. You will be prompted to press Enter to start the game.

## Code Description

The script consists of the following components:

### `fizz_buzz` Function

A `fizz_buzz` function is defined, which takes a number as input and returns:
- "Fizz" if the number is divisible by 3.
- "Buzz" if it's divisible by 5.
- "Fizz Buzz" if it's divisible by both 3 and 5.
- The number itself as a string if none of these conditions are met.

### Game Loop

The script uses a `while` loop to play the FizzBuzz game. It continues until the `next` variable reaches 99 (not 100, as chosen in this code).

Inside the loop:
- `next` is incremented by 1.
- The `fizz_buzz` function is called with the current value of `next`, and the result is printed.
- `next` is incremented by 1 again.
- The correct answer for the current number is calculated using the `fizz_buzz` function and stored in the `correct_answer` variable.
- The player is prompted for their move using `input("Your move: \n")`.

If the player's input (`p1`) does not match the correct answer, the correct answer is printed, and the loop is broken using `break`.

If the player correctly identifies the FizzBuzz sequence up to 99, the loop continues until `next` reaches 99, and then it prints "well done" followed by the value of `next`.

## Conclusion

This script is a simple implementation of the FizzBuzz game in Python, and it allows users to test their ability to identify the sequence of Fizz, Buzz, and Fizz Buzz up to the number 99.

Enjoy playing the game!
