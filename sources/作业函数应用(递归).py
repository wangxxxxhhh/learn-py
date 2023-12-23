
def tri_function(n):
    if n <= 0:
        result = 2
    else:
        result = 2 * tri_function(n - 1)
        print(result)
    return result


tri_function(12)