# import modules
# total = modules.add(50000,600000)
# print(total)

# import must come before your programme
from modules import add
total = add(45,60)

# to rename use (as) example from modules import add as x
# total = x(6,7)
from modules import add as t
total1 =t(6,4)
print(total)
print(total1)
