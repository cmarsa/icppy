# Some Important Complexity Classes

Some of the most common instances of Big O are listed below. In each case, n is a
measure of the size of the inputs to the function.
- `O(1)` denotes __constant__ running time.
- `O(log n)` denotes __logarithmic__ running time.
- `O(n)` denotes __linear__ running time.
- `O(n log n)` denotes __log-linear__ running time.
- `O(n^k)` denotes __polynomial__ running time. Notice that k is a constant.
- `O(c^n)` denotes ___exponential___ running time. Here a constant is being raised to a
power based on the size of the input.


## Constant Complexity
This indicates that the asymptotic complexity is independent of the size of the
inputs. There are very few interesting programs in this class, but all programs
have pieces (for example finding out the length of a Python list or multiplying
two floating point numbers) that fit into this class. Constant running time does
not imply that there are no loops or recursive calls in the code, but it does imply
that the number of iterations or recursive calls is independent of the size of the
inputs.

## Logarithmic Complexity
Such functions have a complexity that grows as the log of at least one of the in-
puts. Binary search, for example, is logarithmic in the length of the list being
searched.
We don’t care about the base of the log, since the difference be-
tween using one base and another is merely a constant multiplicative factor. For
example, `O(log 2 (x)) = O(log 2 (10) * log 10 (x))`.

## Exponential Complexity
As we will see later in this book, many important problems are inherently expo-
nential, i.e., solving them completely can require time that is exponential in the
size of the input. This is unfortunate, since it rarely pays to write a program that
has a reasonably high probability of taking exponential time to run.
