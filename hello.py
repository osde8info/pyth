from datetime import datetime, date, time

msg = "Hello World"
print(msg)
msg = msg+msg

x = "and %s and %s" % (1, 2)
print(x)
print('and %s and %s' % (1, 2))

name = 'Tushar'
age = 23.23

print(f"Hello, My name is {name} and I'm {age:{1}.{5}} years old.")
print(f'Hello, My name is {name} and I"m {age} years old.')

d = datetime.now()

e = 'Time %s' % d

print(e)
print(e)