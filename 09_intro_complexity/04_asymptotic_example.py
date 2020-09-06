# asymptotic.py
'''
We use something called asymptotic notation to provide a formal way to talk
about the relationship between the running time of an algorithm and the size of
its inputs. The underlying motivation is that almost any algorithm is sufficiently
efficient when run on small inputs. What we typically need to worry about is the
efficiency of the algorithm when run on very large inputs. As a proxy for “very
large,” asymptotic notation describes the complexity of an algorithm as the size
of its inputs approaches infinity.
'''

def asymptotic_example(x):
    '''Assume x is an int > 0'''
    answer = 0
    # loop that takes constant time
    for i in range(0, 1000):
        answer += 1
    print('Number of additions os far', answer)
    # loop that takes time x
    for i in range(0, x):
        answer += 1
    print('Number of additions so far', answer)
    # nested loops take time x**2
    for i in range(0, x):
        for j in range(0, x):
            answer += 1
            answer += 1
    print('Number of additions so far', answer)
    return answer


def test_asymptotic_example():
    for x in range(10, 10000, 1000):
        print(f'===== Running test: x = {x:7d} =====')
        asymptotic_example(x)


if __name__ == '__main__':
    test_asymptotic_example()


'''
If one assumes that each line of code takes one unit of time to execute, the
running time of this function can be described as 1000 + x + 2x² . The constant
1000 corresponds to the number of times the first loop is executed. The term x
corresponds to the number of times the second loop is executed. Finally, the term
2x² corresponds to the time spent executing the two statements in the nested for
loop.

ould probably look for a more efficient algorithm.
This kind of analysis leads us to use the following rules of thumb in describ-
ing the asymptotic complexity of an algorithm:
* If the running time is the sum of multiple terms, keep the one with the largest
growth rate, and drop the others.
* If the remaining term is a product, drop any constants.

The most commonly used asymptotic notation is called “Big O” notation. 54
Big O notation is used to give an upper bound on the asymptotic growth (often
called the order of growth) of a function. For example, the formula f(x) ∈ O(x 2 )
means that the function f grows no faster than the quadratic polynomial x 2 , in an
asymptotic sense.
We, like many computer scientists, will often abuse Big O notation by mak-
ing statements like, “the complexity of f(x) is O(x²) .” By this we mean that in the
worst case f will take O(x²) steps to run. The difference between a function being
“in O(x²) ” and “being O(x²) ” is subtle but important. Saying that f(x) ∈ O(x²) does
not preclude the worst-case running time of f from being considerably less than
O(x²) .
When we say that f(x) is O(x²) , we are implying that x² is both an upper and a
lower bound on the asymptotic worst-case running time. This is called a tight
bound
'''
