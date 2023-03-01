def Fibonacci(target):
    resp = 0
    fib = [0,1]
    while (resp <= target):
        if (target == resp):
            return True
        resp = fib[1]+fib[0]
        fib[0] = fib[1]
        fib[1] = resp
    return False


target = 34 #Este valor é o input do sistema

if (Fibonacci(target)) :
    print(f"Valor {target} pertence a fibonacci");
else :
    print(f"Valor {target} NÃO pertence a fibonacci");

