def False_position(func, a, b, error_accept):

    def f(x):
        from math import sin, cos, tan, log, e, exp, pi
        return eval(func)

    error = abs((a*f(b) - b*f(a)) / (f(b) - f(a)))
    cnt = 0

    while error > error_accept:

        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

        if f(a)*f(b) >= 0:
            print('No root or multiple root present')
            quit()

        if f(a)*f(c) < 0:
            error = abs(c-b)
            b = c

        elif f(b)*f(c) < 0:
            error = abs(c-a)
            a = c

        else:
            print('Something went wrong.')
            quit()

        cnt += 1

    print(f'After {cnt} iterations the root of the function is {c}')
    print(f'The error is {error}')

False_position('exp(-0.5*x)*(4-x)-2', 0, 1, 0.005)