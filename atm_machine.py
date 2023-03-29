#program that practices logging

import random, logging, sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("formatted.log")
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
log_format = logging.Formatter("[%(asctime)s] - %(message)s")
stream_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

from datetime import datetime

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
    
      if pin != 1234:
        print("Error! Invalid pin. Try again.")
        logger.warning("User entered invalid pin")
      else:
        logger.info("User logged in successfully")
        return None
 
  def deposit(self):
    tran_number = random.randint(10000, 1000000)
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        print("Warning! You entered a negative number to deposit.")
        logger.warning("User entered an invalid number to deposit")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Balance: ${balance}".format(balance=self.balance))
      print("Transaction Info:")
      print("Status: Successful")
      print("Transaction #{tran_number}".format(tran_number=tran_number))
      logger.info("Transaction successful: #{tran_number} ".format(tran_number=tran_number))
    except ValueError:
      print("Error! You entered a non-number value to deposit.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number))
      logger.error("User entered a non-number value to deposit. Transaction #{tran_number}".format(tran_number=tran_number))
 
  def withdraw(self):
    tran_number = number=random.randint(10000, 1000000)
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        print("You withdrew: ${amount}".format( amount=amount))
        logger.info("User withdrew: ${amount}".format( amount=amount))
        logger.info("User balance: ${amount}".format(amount=self.balance))
        print("Transaction Info:")
        print("Status: Successful")
        print("Transaction #{number}".format(number=tran_number))
        logger.info("Withdrawl successful.Transaction #{number}".format(number=tran_number))
      else:
        print("Error! Insufficient balance to complete withdraw.")
        print("Transaction Info:")
        print("Status: Failed")
        print("Transaction #{number}".format(number=tran_number))
        logger.warning("User failed to withdrawal. Transaction #{number}".format(number=tran_number))
    except ValueError:
      print("Error! You entered a non-number value to withdraw.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number=tran_number))
      logger.warning("User failed to withdrawal. Transaction #{number}".format(number=tran_number))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
    logger.info("User ending balance: {balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()