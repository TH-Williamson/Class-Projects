#need to tqke an integer input, and convert it to mm/dd/yyyy AND DD-MM-YYY format
#TH Williamson, intro to programming, Prof. Kurdia


user_day = str(input('Please enter day: '))
user_month = str(input('Please enter month: '))
user_year = str(input('Please enter year: '))


if user_day[0] == 0:
    user_day = '0' + user_day
else:
    user_day = user_day
    
        

#US, Micronesia date format
print('Here is the formatted date:', user_month, end='')
print('/', end='')
print(user_day, end='')
print('/', end='')
print(user_year)

#Rest of world format
print('Here is the formatted date:', user_day, end='')
print('-', end='')
print(user_month, end='')
print('-', end='')
print(user_year)

