grades=[8,14,9.5,18,7,12,10,19,5.5]
passed=[]
for num in grades:
  if num > 10:
     print(num)
     passed.append(num)
print(len(passed))

avg=sum(passed)/len(passed) if passed else 0
print(avg)