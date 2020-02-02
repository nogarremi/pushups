days = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
    }
months = {
    'january':1,
    'february':2,
    'march':3,
    'april':4,
    'may':5,
    'june':6,
    'july':7,
    'august':8,
    'september':9,
    'october':10,
    'november':11,
    'december':12
    }
abbr = {
    'jan':1,
    'feb':2,
    'mar':3,
    'apr':4,
    'may':5,
    'jun':6,
    'jul':7,
    'aug':8,
    'sept':9,
    'oct':10,
    'nov':11,
    'dec':12
    }

while True:
    total_days = 0
    u_input = input('\'day\' or \'total\' (q to exit): ').lower()

    if (u_input == 'q'):
        print('Goodbye')
        break
    elif u_input not in ['day','total']:
        print('Invalid input. Try again\n')
        continue
    while True:
        month = input('Enter month: ').lower()


        if month in abbr.keys():
            month = abbr[month]
            break
        elif month in months.keys():
            month = months[month]
            break
        elif int(month) in range(1,13):
            break
        elif month not in abbr.keys() and month not in months.keys():
            print('Invalid Month\n')
            continue
        

    while True:
        day = int(input('Enter day: '))
        
        if day < 1:
            pass
        elif month == 2:
            if day <= 28:
                break
        elif month in [4,6,9,11]:
            if day <= 30:
                break
        else:
            if day <= 31:
                break
        
        print('Invalid Day\n')

    for i in range(1,int(month)):
        total_days += days[i]

    total_days += day

    if (u_input == 'day'):
        print('You have ' +  str(total_days) + ' pushups to do today\n')
    elif (u_input == 'total'):
        pushups = int((total_days * (total_days + 1)) / 2)
        print('Total push-ups: ' + str(pushups) + '\n')
