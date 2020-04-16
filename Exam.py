# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:16:55 2020

@author: Mariusz
"""
import math
var1 = 7

def var3(var1, var2):
    var0 = var1 + var2
    var1 += 1
    print var1
    global var4
    var4 = 17
    print locals()
    return var0 + var4
    
print var3(var1, var1)
#global_dict = {}
#global_dict[(0)] = 1
#print global_dict["var1"], global_dict["var3"], global_dict["var4"]

class BankAccount:
    def __init__(self, initial_balance):
        """
        Creates an account with the given balance.
        """
        self._balance = initial_balance
        self._fees = 0
        self._FEE = 5
    def deposit(self, amount):
        """
        Deposits the amount into the account.
        """
        self._balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  
        Each withdrawal resulting in a balance of 
        less than 10 dollars (before any fees) also 
        deducts a penalty fee of 5 dollars from the balance.
        """
        if self._balance - amount < 10:
            self._balance -= self._FEE
            self._fees += self._FEE
            
        self._balance -= amount
        

    def get_balance(self):
        """
        Returns the current balance in the account.
        """
        return self._balance

    def get_fees(self):
        """
        Returns the total fees ever deducted from the account.
        """
        return self._fees
    

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

n = 1000
total = 0
for idx in range(1001):
    total += idx**n

print (math.factorial(n))**n > total
print total > n^1000