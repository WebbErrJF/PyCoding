data=[10,5,20,30,40,50,60,70,80,90,100]

#function which is going to provide a condition to main function 

def filter_func(condition,data,filtred_data=[]): # I took advantage of fact, that default arguments are evaluated only one (filtered_data)
    if len(data)>=1:
        if condition(data[0]):
            filtred_data.append(data[0])
            return filter_func(condition,data[1:])
        else:
            return filter_func(condition,data[1:])  
    else:
        output=filtred_data.copy()
        filtred_data.clear()
        return output 

print(filter_func(lambda value: value<50,data))
print(filter_func(lambda value: value<50,data))

