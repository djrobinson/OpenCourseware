balance = float(raw_input("Current outstanding balance: "))
rate = float(raw_input("Annual interest rate: "))
minimum = float(raw_input("Minimum monthly payment rate as a decimal: "))
month = 1

while month <= 12:
  min_pay = round(minimum * balance,2)
  int_paid = round(rate / 12 * balance,2)
  prin_paid = min_pay - int_paid
  balance -= prin_paid

  print("Month: ",month)
  print("Monthly minimum payment: ",min_pay)
  print("Interest paid",int_paid)
  print("Principal paid: ",prin_paid)
  print("Remaining balance: ",balance)
  month = month + 1
