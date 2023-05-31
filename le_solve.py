import numpy as np
def coefficients(str):
    ans = [0,0,0]
    temp = 0
    s = ''
    for c in str:
        if(c == 'x'):
            try:
                temp = int(s)
            except:
                if(s == '-'):
                    temp = -1
                else:
                    temp = 1
            s = ''
            ans[0] = temp
        elif(c == 'y'):
            try:
                temp = int(s)
            except:
                if(s == '-'):
                    temp = -1
                else:
                    temp = 1
            s = ''
            ans[1] = temp
        elif(c == '='):
            continue
        else:
            s += c
    temp = int(s)
    ans[2] = temp
    return ans

def le_solve(eq1,eq2):
    arr1 = coefficients(eq1)
    arr2 = coefficients(eq2)
    print(arr1,arr2)
    a = np.array([
        [arr1[0], arr1[1]],
        [arr2[0], arr2[1]]
        ])
    b = np.array([arr1[2],arr2[2]])
    print(a,b)
    x = np.linalg.solve(a,b)
    print('x = ',x[0], 'y =',x[1])
    return x