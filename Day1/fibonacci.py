# WAP in  python to print fibonacci series and print sum of the series as well as even prime number in the list

def fibonacci(n):
    i = 0
    series = [0,1]
    a ,b = 0 ,1
    while (i < n):
        c = a + b
        series.append(c)
        a = b
        b = c
        i += 1
    
    print(f"fibonacci series upto {n}th term is {series}")
    return series
        

        
    

n = int(input("enter value of nth term ::> "))
fSeries = fibonacci(n)

print("sum of this series is ::> ",sum(fSeries))

print(f"even prime numner in list is ::> {fSeries[3]}")