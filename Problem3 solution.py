inputs = list()

for i in range(5):
    inputs.append(input())

number =1
runaway = True
for i in inputs:
    if i.find('FBI') != -1:
        print(str(number),end=' ')
        runaway = False
    number += 1
if runaway:
    print('HE GOT AWAY!')