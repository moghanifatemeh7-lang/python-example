def calc(x):
    perimeter=4*x
    area=x*x
    return perimeter,area
side = int(input())
p,a = calc(side)
print("perimeter:"+str(p))
print("area:"+str(a))