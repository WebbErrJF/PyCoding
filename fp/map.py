data=[10,20,30,40,50,60,70,80,90,100]

#function, thats provide what kind of operation will be done in map function
def operation(value):
    return value+2


def map_func(function,data,n=0,output=[]):
    if n<len(data):
        output.append(function(data[n]))
        n+=1
        return map_func(function,data,n) #return it is needed here, beacause it returns data from return below
    elif n==len(data):
        final_output=[]
        for element in output:
            final_output.append(element)
        output.clear()
        n=0
        return final_output

print(map_func(operation,data))
print(map_func(operation,data))
