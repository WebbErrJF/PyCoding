data=[10,20,30,40,50,60,70,80,90,100]

def map_func(function,data,maped_list=[]):
    if len(data)>=1:
        maped_list.append(function(data[0]))
        return map_func(function,data[1:]) #return it is needed here, beacause it returns data from return below
    else:
        output=maped_list.copy()
        maped_list.clear()
        return output


print(map_func(lambda value: value+2,data))
print(map_func(lambda value: value*2,data))


