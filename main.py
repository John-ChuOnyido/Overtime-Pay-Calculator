#setting a grobal function that is user friendly 
#by accepting input from the user
total_hours = float(input("Enter the total hours you work in a week: "))
#defining a function to calculate the overtime pay and deduction 
#when the worker missed work in the week
def overtime():
  #user input collecting the basic salary of the worker in dollar
  basic_salary = float(input("Enter your basic salary: $"))
  #calculating the hourly pay
  hourly_pay = basic_salary/total_hours
  #user input collecting the total hours the worker worked for the week
  worked_hours = float(input("Enter your worked time for the week: "))
  #checking if the worker worked complete without overtime, missed work or did overtime
  if worked_hours == total_hours:
    print("You didn't do overtime for the week")
  elif worked_hours > total_hours:
    overtime  = worked_hours - total_hours
    overtime_pay = overtime * hourly_pay
    print("Your overtime for the week is ${}".format(overtime_pay))
  elif worked_hours < total_hours:
    noWorkHours = total_hours - worked_hours
    bas_month = worked_hours * hourly_pay
    noWorkPay = basic_salary - bas_month
    print("You miss {}hrs of work".format(noWorkHours), 
          "\nSo your pay for the week is ${}".format(bas_month),
          "\nAnd you Hours of no payment is {}hrs".format(noWorkHours),
          "\nWhich results to ${} deduction from your salary".format(noWorkPay))
#calling the function
overtime()
