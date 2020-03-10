#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) or linear because n is unknown. If we choose n to be 2 the function would run 8 times, however if we choose 10 it runs 1000 times.


b) O(n log n) first part is linear second part is log n


c) O(n) linear input not chosen yet

## Exercise II

## Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

## Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

-The base case would start off at 0 being n - story of the building.

-Then we would say something like:
-if floor is less than or equal to n- story:
    -false  -meaning the egg was not broken
-else:
    -true   - meaning the egg was broken

- sounds like a O(n) runtime but the floor is determined by the input param.    



