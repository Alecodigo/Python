passwordFile = open('password.txt')
secretPassword = str(passwordFile.read())
print(secretPassword)
print('Enter your password.')
typedPassword = input()
print(type(typedPassword))

print (type(typedPassword),type(secretPassword))
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '123456':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
