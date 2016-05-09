import time

print('Hello!')
time.sleep(1)  # delays for 2 seconds

print('Please choose a number (in your head) between 1 and 10, but not including them.')
time.sleep(2)

response1 = input('Is your number divisible by 2 (y or n)?')

if response1 == 'y':
    # 2, 4, 6, 8 are possible
    response2 = input('Is your number divisible by 4 (y or n)?')
    if response2 == 'y':
        # 4, 8 are possible
        response3 = input('Is the square root of your number 2 (y or n)?')
        if response3 == 'y':
            print('Your number is 4!')
        elif response3 == 'n':
            print('Your number is 8')
        else:
            print('Please answer only y or n')
    elif response2 == 'n':
        # 2, 6 are possible
        response3 = input('Is your number prime (y or n)?')
        if response3 == 'y':
            print('Your number is 2!')
        if response3 == 'n':
            print('Your number is 6!')
    else:
        print('Please restart the script answering only y or n')

elif response1 == 'n':
    # 3, 5, 7, 9 are possible
    response2 = input('Is your number divisible by 3 (y or n)')
    if response2 == 'y':
        # 3, 9 are possible
        response3 = input('Is your number prime (y or n)?')
        if response3 == 'y':
            print('Your number is 3!')
        if response3 == 'n':
            print('Your number is 4!')

    elif response2 == 'n':
        # 5, 7 are possible
        response3 = input('Is your number divisible by 5 (y or n)?')
        if response3 == 'y':
            print('Your number is 5!')
        if response3 == 'n':
            print('Your number is 7!')
    else:
        print('Please restart the script answering only y or n')

else:
    print('Please restart the script, and answer either y or n')
