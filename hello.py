print("learn git & python in Linux Mint")

def fun():
    print("hellopython function")
    return

fun()

def multi(nums):
    sum=0
    for num in nums:
        sum=num*num+sum
    return sum

sum=multi([1,2,3])
print(sum)

print(multi((0,1,2)))

nums=[1,2,3,4]

print(multi(nums))

def mul(*nums):
    for i in nums:
        print(i)

mul(1,2,3)
# 传入一个list或者tuple
# 传入多个变量，新组成一个tuple
C="Composite"
D=[1,2,3]
mul('A','c',C,D)