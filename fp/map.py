data=[10,20,30,40,50,60,70,80,90,100]

def map_func(function,data):
    if len(data)>=1:
        return [function(data[0])] + map_func(function,data[1:])
    else:
        return []


print(map_func(lambda value: value+2,data))
print(map_func(lambda value: value*2,data))


