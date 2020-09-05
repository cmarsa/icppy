# nested_scopes.py
'''
Each function defines a new name space, also called a scope. The formal
parameter x and the local variable y that are used in f exist only within the scope
of the definition of f.

Here’s one way to think about this:
1. At top level, i.e., the level of the shell, a symbol table keeps track of all names
defined at that level and their current bindings.

2. When a function is called, a new symbol table (often called a stack frame) is
created. This table keeps track of all names defined within the function (in-
cluding the formal parameters) and their current bindings. If a function is
called from within the function body, yet another stack frame is created.

3. When the function completes, its stack frame goes away.
'''
def f(x):
    def g():
        x = 'abc'
        print('x = ', x)
    def h():
        z = x
        print('z = ', z)
    x = x + 1
    print('x = ', x)
    h()
    g()
    print('x = ', x)
    return g

x = 3
z = f(x)
print('x = ', x)
print('z = ', z)
print(z())