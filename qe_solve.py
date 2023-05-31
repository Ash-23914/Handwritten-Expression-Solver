import math
def coefficients(str):
    ans = [0,0,0]
    temp = 0
    s = ''
    for i in range(len(str)):
        print(str[i],s) 
        if(str[i] == 'x' and str[i+1] == '2'):
            try:
                temp = int(s)
            except:
                if(s == '-'):
                    temp = -1
                else:
                    temp = 1
            s = ''
            ans[0] = temp
        elif(str[i] == 'x' and str[i+1]!='2'):
            try:
                temp = int(s)
            except:
                if(s == '-'):
                    temp = -1
                else:
                    temp = 1
            s = ''
            ans[1] = temp
        elif(str[i] == '+' or str[i] == '-'):
            s = str[i]
        elif(str[i] == '='):
            continue
        else:
            s += str[i]
    temp = int(s)
    ans[2] = temp
    return ans

def qe_solve(string):
    coeff = coefficients(string)
    print(coeff)
    a,b,c = coeff[0],coeff[1],coeff[2]
    print(a,b,c)
    det = (b*b) - (4*a*c)
    print(det)
    if(det>=0):
        r1 = (-b/(2*a))+(math.sqrt(det))/(2*a)
        r2 = (-b/(2*a))-(math.sqrt(det))/(2*a)
    else:
        r1 = str(-b/2*a) + " + i" + str(math.sqrt(-1*det)/(2*a))
        r2 = str(-b/2*a) + " - i" + str(math.sqrt(-1*det)/(2*a))
    return [r1,r2]


