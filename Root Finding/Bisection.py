def Bisection(func, a, b, error_accept):

    def f(x):
        from math import sin, cos, tan, log, e, exp
        return eval(func)

    error = abs(b-a)
    cnt = 0

    while error > error_accept:
        c = (a+b)/2

        if f(a)*f(b) >= 0:
            print('No root or multiple root present')
            quit()

        elif f(a)*f(c) < 0:
            b = c
            error = abs(b-a)

        elif f(b)*f(c) < 0:
            a = c
            error = abs(b-a)

        else:
            print('Something went wrong.')
            quit()

        cnt += 1

    print(f'After {cnt} iterations the root of the function is {c}')
    print(f'The error is {error}')

Bisection('exp(-0.5*x)*(4-x)-2', 0, 1, 0.005)