# Mortgage.py

def find_payment(loan, r, m):
    '''
    Assumes: loan and r are floats, m an int.
    Returns the monthly payment for a mortgage of size
        loan at a monthly rate of r for m months.
    '''
    return loan*((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage:
    '''
    Abstract class for building different kinds of mortgages.
    '''
    def __init__(self, loan, annual_rate, months):
        '''
        Assumes: loan and annual_rate are floats, months an int
        Creates a new mortgage of size loan, duration months and
        annual rate annual_rate.
        '''
        self.loan = loan
        self.rate = annual_rate / 12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None
    
    def make_payment(self):
        '''Make a payment'''
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def get_total_paid(self):
        '''Returmn the total amoun paid so far'''
        return sum(self.paid)
    
    def __str__(self):
        return self.legend
