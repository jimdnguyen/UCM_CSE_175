import functions.goodbye as bye
import functions.greeting.hello
from classes import calculator
# Import the official module as official


print(functions.greeting.hello.hello('Susan'))
bye.good_bye('Alex')
c = calculator.Multiply()
c.multiply(2)
print(c.get_current())

print(official.hello('Sam'))

