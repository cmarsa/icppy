# Fixed.py
from .Mortgage import Mortgage

class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r * 100, 2)) + '%'
