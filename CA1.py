class Employee:
    def __init__(self,name, weeklyhours, rate, overtimeRate, weeklytaxcredit):
        self.name = name
        self.weeklyhours= weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit
        if self.overtimeRate<0:
            print("Invalid Overtime value")
            return

    def computeWeeklyPay (self,hours):
        gross_pay = 0
        gross_pay += (self.rate*hours) + self.weeklytaxcredit
        if gross_pay <0:
            return 0
        return gross_pay

    def computeTax(self,grossPay):
        tax_due = 0
        tax_due += (grossPay * 0.4) - self.weeklytaxcredit
        if tax_due < 0:
            print("Tax value cannot be negative")
            return 0
        return tax_due


e1 = Employee


