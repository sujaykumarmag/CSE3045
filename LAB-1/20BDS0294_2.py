import numpy as np



def parser(eq1):
    list1 = []
    x = []
    for i in range(0,len(eq1)):
        if eq1[i].isdigit():
            if eq1[i-1]=='-':
                list1.append(-1 * int(eq1[i]))
            else:
                list1.append(int(eq1[i]))
        elif eq1[i].isalpha():
            x.append(eq1[i])
    return list1

x = list(input("Enter the First Vector (comma separated) "))
x = parser(x)

y = list(input("Enter the Second Vector (comma separated) "))
y = parser(y)

z = list(input("Enter the Second Vector (comma separated) "))
z = parser(z)

print(x,y,z)

a = np.array([x,y,z],dtype=float)


def det():
    return x[0]*(y[1]*z[2]- z[1]*y[2]) - x[1]*(y[0]*z[2]-z[0]*y[2]) + x[2]*(y[0]*z[1]-z[0]*y[1])

def coplanar():
    if(det()==0):
        return True
    else:
        return False
    
print(coplanar())


