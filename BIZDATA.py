present_year = int(input("Enter today's year: "))
present_month = int(input("Enter today's month: "))
present_date = int(input("Enter today's date: "))

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_date = int(input("Enter birth date: "))

if birth_date>present_date and birth_month>=present_month:
    todays_date = (present_date+30) - birth_date
    todays_month = ((present_month-1)+12) - birth_month
    todays_year = (present_year-1) - birth_year
    print(str(todays_year) + " Years " + str(todays_month) + " Months " +str(todays_date) + " Days ")

elif birth_date>present_date and birth_month<present_month:
    todays_date = (present_date+30) - birth_date
    todays_month = present_month - birth_month
    todays_year = present_year - birth_year
    print(str(todays_year) + " Years " + str(todays_month) + " Months " +str(todays_date) + " Days ")

elif birth_date<present_date and birth_month>present_month:
    todays_date = present_date - birth_date
    todays_month = (present_month+12) - birth_month
    todays_year = (present_year-1) - birth_year
    print(str(todays_year) + " Years " + str(todays_month) + " Months " +str(todays_date) + " Days ")

else:
    
    todays_date = present_date - birth_date
    todays_month = present_month - birth_month
    todays_year = present_year - birth_year
    print(str(todays_year) + " Years " + str(todays_month) + " Months " +str(todays_date) + " Days ")    
