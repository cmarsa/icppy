# compare_mortgages.py
from Mortgages import Fixed
from Mortgages import FixedWithPts
from Mortgages import TwoRate

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                      var_rate_1, var_rate_2, var_months):
    total_months = years * 12
    fixed_1 = Fixed(amt, fixed_rate, total_months)
    fixed_2 = FixedWithPts(amt, pts_rate, total_months, pts)
    two_rate = TwoRate(amt, var_rate_2, total_months, var_rate_1, var_months)
    morts = [fixed_1, fixed_2, two_rate]
    print('Amount: $' + str(amt))
    for m in range(0, total_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(' Total payments: $' + str(int(m.get_total_paid())))
    

if __name__ == '__main__':
    compare_mortgages(
        amt = 200000,
        years = 30,
        fixed_rate = 0.07,
        pts = 3.25,
        pts_rate = 0.05,
        var_rate_1 = 0.045,
        var_rate_2 = 0.095,
        var_months = 48
    )
