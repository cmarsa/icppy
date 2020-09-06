# 01_linear_search.py

def linear_search(L, x):
    for e in L:
        if e == x:
            return True
    return False


'''
For simplicity, we will use a random access machine as our model of compu-
tation. In a random access machine, steps are executed sequentially, one at a
time. A step is an operation that takes a fixed amount of time, such as binding a
variable to an object, making a comparison, executing an arithmetic operation,
or accessing an object in memory.

In general, there are three broad cases to think about:
* The best-case running time is the running time of the algorithm when the in-
puts are as favorable as possible. I.e., the best-case running time is the mini-
mum running time over all the possible inputs of a given size. For
linearSearch , the best-case running time is independent of the size of L .
* Similarly, the worst-case running time is the maximum running time over all
the possible inputs of a given size. For linearSearch , the worst-case running
time is linear in the size of L .
* By analogy with the definitions of the best-case and worst-case running time,
the average-case (also called expected-case) running time is the average run-
ning time over all possible inputs of a given size. Alternatively, if one has some
a priori information about the distribution of input values (e.g., that 90% of
the time x is in L ), one can take that into account.

People usually focus on the worst case. All engineers share a common article
of faith, Murphy’s Law: If something can go wrong, it will go wrong. The worst-
case provides an upper bound on the running time. This is critical in situations
where there is a time constraint on how long a computation can take. It is not
good enough to know that “most of the time” the air traffic control system warns
of impending collisions before they occur.


'''