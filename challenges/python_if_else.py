N = int(input("Choose a number between 0 and 100..."))
if N % 2 == 0 and N in range(2, 6):
    print('Not Weird')
elif N % 2 == 0 and N in range(6, 21):
    print('Weird')
elif N % 2 == 0 and N > 20: 
    print('Not Weird')
else:
    print('Weird')