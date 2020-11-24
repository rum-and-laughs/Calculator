# -*- coding: utf-8 -*-


from decimal import Decimal

from calculator import Percentage


class Interests:
    def __init__(self,
                 profits_via_referrals: Decimal,
                 interest_rate: Percentage,):
        self.__interest_rate = interest_rate
        self.__profits_via_referrals = profits_via_referrals

    def calculate(self):
        _profits_via_referrals = self.__profits_via_referrals
        _interest_rate = self.__interest_rate.calculate()
        result = _profits_via_referrals * (Decimal(1) + _interest_rate / Decimal(12))
        return result

