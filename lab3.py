n = 100
series = 'sum'



if series == 'fibonacci':
    a=0
    b=1
    for i in range(n):
        a, b = b, a+b
    print a

elif series == 'sum':
    x = (((3 * n ** 2)+(3 * n))/2)
    print x

else:
    print "INVALID STRING, TRY AGAIN PUNY HUMAN"