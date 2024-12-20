import stdio

total=0.0
count=0

while not stdio.is Empty():
    value=stdio.readfloat()
    total+= value
    count+=1


print('Average is %0.2f'%(total/count))