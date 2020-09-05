# FixedWithPts.py
from .Mortgage import Mortgage

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100)]
        self.legend = 'Fixed, ' + str(round(r * 100, 2)) + '%, ' + \
                      str(pts) + ' points'
