data=[10,20,30,40,50,60,70,80,90,100]
data2=["a","b","c","d","e"]


def reduce_func(function,data,instantaneous_value=None):
    if len(data)>=1:
        if instantaneous_value is None:
            instantaneous_value=data[0]
            return reduce_func(function,data[1:],instantaneous_value)
        else:
            instantaneous_value=function(data[0],instantaneous_value)
            return reduce_func(function,data[1:],instantaneous_value) #return it is needed here, beacause it returns data from return below
    else:
        return instantaneous_value

print(reduce_func(lambda instantaneous_value, value: value + instantaneous_value,data))
print(reduce_func(lambda instantaneous_value, value: value + instantaneous_value,data2))
