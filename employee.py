"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name


    
class SalaryContractWithoutCommission(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.monthly_salary = salary

    def get_pay(self):
        return self.monthly_salary
    
    def __str__(self):
        return self.name+ " works on a monthly salary of "+ str(self.monthly_salary)+". Their total pay is "+str(self.get_pay())+"."


class SalaryContractWithCommission(Employee):
    def __init__(self, name, salary, commission_type, commission, num_of_contracts):
        super().__init__(name)
        self.monthly_salary = salary
        self.commission_type = commission_type
        self.commission = commission
        self.num_of_contracts = num_of_contracts
    
    def get_pay(self):
        if self.commission_type == "fixed":
            return self.monthly_salary + self.commission
        elif self.commission_type == "contract":
            return self.monthly_salary + self.commission * self.num_of_contracts
        
    def __str__(self):
        if self.commission_type == "contract":
            # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
            return self.name+ " works on a monthly salary of "+ str(self.monthly_salary)+" and receives a commission for "+ str(self.num_of_contracts) + " contract(s) at "+ str(self.commission)+"/contract. Their total pay is "+str(self.get_pay())+"."
        elif self.commission_type == "fixed":
            # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
            return self.name+ " works on a monthly salary of "+ str(self.monthly_salary)+" and receives a bonus commission of "+ str(self.commission)+". Their total pay is "+str(self.get_pay())+"."


class HourlyContractWithoutCommission(Employee):
    def __init__(self, name, wage, hours):
        super().__init__(name)
        self.hourly_wage = wage
        self.hours = hours

    def get_pay(self):
        return self.hourly_wage * self.hours
    
    def __str__(self):
        return self.name+ " works on a contract of "+ str(self.hours)+" hours at "+ str(self.hourly_wage) +"/hour.  Their total pay is "+str(self.get_pay())+"."

class HourlyContractWithCommission(Employee):
    def __init__(self, name, wage, hours, commission_type, commission, num_of_contracts):
        super().__init__(name)
        self.hourly_wage = wage
        self.hours = hours
        self.commission_type = commission_type
        self.commission = commission
        self.num_of_contracts = num_of_contracts

    def get_pay(self):
        
        if self.commission_type == "contract":
            return self.hourly_wage * self.hours + self.num_of_contracts * self.commission
        elif self.commission_type == "fixed":
            return self.hourly_wage * self.hours + self.commission
        
    def __str__(self):
        if self.commission_type == "contract":
            return self.name+ " works on a contract of "+ str(self.hours)+" hours at "+ str(self.hourly_wage) +"/hour and receives a commission for "+ str(self.num_of_contracts) + " contract(s) at "+ str(self.commission)+"/contract. Their total pay is "+str(self.get_pay())+"."
        elif self.commission_type == "fixed":
            return self.name+ " works on a contract of "+ str(self.hours)+" hours at "+ str(self.hourly_wage) +"/hour and receives a bonus commission of "+ str(self.commission)+". Their total pay is "+str(self.get_pay())+"."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryContractWithoutCommission('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContractWithoutCommission('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractWithCommission('Renee', 3000, "contract" , 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractWithCommission('Jan', 25, 150, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryContractWithCommission('Robbie', 2000, "fixed", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractWithCommission('Ariel', 30, 120, "fixed", 600, 0)
