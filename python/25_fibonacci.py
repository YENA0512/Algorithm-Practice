def solution(n):
    answer = 0
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    result = (f[n] % 1234567)
    return result

# another solution
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
    