def my_function(n):
    if n <= 3:
        result = n
    else:
        result = n * my_function(n - 1)
        print(result)
    return result


my_function(10)
