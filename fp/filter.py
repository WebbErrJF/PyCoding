data=[10,20,30,40,50,60,70,80,90,100]

#function which is going to provide a condition to main function 
def condition_func(value):
    if value<50:
        return True
    return False

def filter_func(condition,data,n=0,filtred_data=[]): # I took advantage of fact, that default arguments are evaluated only one (filtered_data)
    if condition(data[n]):
        filtred_data.append(data[n])
        if n<len(data)-1:
            n=n+1
            filter_func(condition,data,n)
    else:
        if n<len(data)-1:
            n=n+1
            filter_func(condition,data,n)
        else:
            print(filtred_data)
            n=0
            filtred_data.clear()

filter_func(condition_func,data)