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
            weeklytaxcredit = hours - self.weeklyhours
        else:
            weeklytaxcredit = self.weeklyhours - hours
        weeklytaxcredit *= self.overtimeRate
        gross_pay += (self.rate*self.weeklyhours) + weeklytaxcredit
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


ch = "y"
object_list = []
while ch =='yes' or ch =='y':
    Empname = raw_input("Enter your name: ")
    Empweeklyhours = raw_input("Enter your weekly hours: ")
    Emprate = raw_input("Enter your hourly rate: ")
    EmpovertimeRate = raw_input("Enter your overtime rate: ")
    Empweeklytaxcredit = raw_input("Enter your tax credit: ")
    e1 = Employee(Empname,int(Empweeklyhours),int(Emprate),int(EmpovertimeRate),int(Empweeklytaxcredit))
    object_list.append(e1)
    gross = e1.computeWeeklyPay(39)
    print "Gross Pay of " + Empname + " is " + str(gross)
    tax = e1.computeTax(gross)
    print "Calculated Tax value is " + str(tax)
    ch = raw_input("Press yes/y to enter more employees else enter quit/q:  ")
