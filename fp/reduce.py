data=[10,20,30,40,50,60,70,80,90,100]

#function which is going to provide an operation to reduce function 
def operation_func(value,instantaneous_value):
    return value+instantaneous_value

def reduce_func(function,data,n=0,instantaneous_value=0):
    if n<len(data):
        instantaneous_value=function(data[n],instantaneous_value)
        n+=1
        return reduce_func(function,data,n,instantaneous_value) #return it is needed here, beacause it returns data from return below
    elif n==len(data):
        return instantaneous_value

