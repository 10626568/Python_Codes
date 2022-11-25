class Employee(name, weeklyhours, rate, overtimeRate, weeklytaxcredit):
    def __init__(self):
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
        return gross_pay

    def computeTax(self,grossPay):
        tax_due = 0
        tax_due += grossPay * 0.4
        return tax_due

