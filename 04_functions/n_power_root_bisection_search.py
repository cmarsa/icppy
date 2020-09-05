# n_power_root_bisection_search.py
'''
A specification of a function defines a contract between the implementer of a
function and those who will be writing programs that use the function. We will
refer to the users of a function as its clients. This contract can be thought of as
containing two parts:

* Assumptions: These describe conditions that must be met by clients of the
function. Typically, they describe constraints on the actual parameters. Almost
always, they specify the acceptable set of types for each parameter, and not in-
frequently some constraints on the value of one or more of the parameters.
For example, the first two lines of the docstring of findRoot describe the as-
sumptions that must be satisfied by clients of findRoot .

* Guarantees: These describe conditions that must be met by the function, pro-
vided that it has been called in a way that satisfies the assumptions. The last
two lines of the docstring of findRoot describe the guarantees that the imple-
mentation of the function must meet.

Functions are a way of creating computational elements that we can think of
as primitives. Just as we have the built-in functions max and abs , we would like to
have the equivalent of a built-in function for finding roots and for many other
complex operations. Functions facilitate this by providing decomposition and ab-
straction.

* Decomposition creates structure. It allows us to break a program into parts
that are reasonably self-contained, and that may be reused in different settings.

* Abstraction hides detail. It allows us to use a piece of code as if it were a black
box—that is, something whose interior details we cannot see, don’t need to see,
and shouldn’t even want to see. 26 The essence of abstraction is preserving infor-
mation that is relevant in a given context, and forgetting information that is ir-
relevant in that context. The key to using abstraction effectively in programming
is finding a notion of relevance that is appropriate for both the builder of an ab-
straction and the potential clients of the abstraction. That is the true art of pro-
gramming.
'''
def find_root(x, power, epsilon):
    '''Assumes x and epsilon int or float, power an int,
            epsilon > 0 & power >= 1
       Returns float y such that y**power is withing epsilon of x.
            if such a float does not exist, returns None.
    '''
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    answer = (high + low) / 2.0
    while abs(answer ** power - x) >= epsilon:
        if answer ** power < x:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2.0
    return answer


def test_find_root():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print('testing x:', str(x), 'and power: ', power)
            result = find_root(x, power, epsilon)
            if result == None:
                print('  No root.')
            else:
                print('  ', result ** power, '~=', x)


if __name__ == '__main__':
    test_find_root()