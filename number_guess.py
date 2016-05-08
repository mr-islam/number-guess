print('Hello!')
print('Please choose a number (in your head) between 1 and 10, and not including them.')

response1 = input('Is your number divisible by 2 (y or n)?')

if response1 == 'y':
    # 2, 4, 6, 8 are possible
    print('yes!')

elif response1 == 'n':
    # 3, 5, 7, 9 are possible
    response2 = input('')

else:
    print('Please restart the script, and answer either y or n')

