# TwoRate.py
from .Mortgage import Mortgage
from .Mortgage import find_payment

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.next_rate = r / 12
        self.legend = str(teaser_rate * 100) \
                        + '% for ' + str(self.teaser_months) \
                        + ' months, then ' + str(round(r * 100, 2)) + '%'
    
    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.rate = self.next_rate
            self.payment = find_payment(self.outstanding[-1],
                                        self.rate,
                                        self.months - self.teaser_months)
        Mortgage.make_payment(self)