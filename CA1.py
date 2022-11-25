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
        if hours > self.weeklyhours:
            self.weeklytaxcredit = hours-self.weeklyhours
        else:
            self.weeklytaxcredit = self.weeklyhours - hours
        gross_pay += (self.rate*self.weeklyhours) + self.weeklytaxcredit
        if gross_pay <0:
            print "Gross pay cannot be negative"
            return 0
        return gross_pay

    def computeTax(self,grossPay):
        tax_due = 0
        tax_due += (grossPay * 0.4) - self.weeklytaxcredit
        if tax_due < 0:
            print("Tax value cannot be negative")
            return 0
        return tax_due


e1 = Employee("Rahul",35,11,15,70)
gross = e1.computeWeeklyPay(39)
print gross
tax = e1.computeTax(gross)
print tax

