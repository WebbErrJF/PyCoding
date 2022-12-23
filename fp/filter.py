data=[10,5,20,100,30,40,50,60,70,80,90,100]
data2=["K","g","g","w"]

def filter_func(condition,data):
    if len(data)>=1:
        if condition(data[0]):
            return [data[0]] + filter_func(condition,data[1:])
        else:
            return filter_func(condition,data[1:])  
    else:
        return []

print(filter_func(lambda value: value<50,data))
print(filter_func(lambda value: value=="g",data2))

#test1
#test23232323