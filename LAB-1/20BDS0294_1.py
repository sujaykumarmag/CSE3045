import numpy as np

def parser(eq1):
    a1 = []
    c1 = 0
    i=0
    while(i<=len(eq1)):
        if eq1[i]=='-':
            a1.append(-float(eq1[i+1]))
            i =i+2
        if eq1[i]=='+':
            a1.append(float(eq1[i+1]))
            i =i+2
        elif eq1[i] == '=':
            if eq1[i+1]=='-':
                c1 = -float(eq1[i+2])
                i =i+2
            else:
                c1 = float(eq1[i+1])
                i =i+2
            break
        elif eq1[i]== "s" or eq1[i]=='t'or eq1[i]=='x' or eq1[i]=='y':
            i = i+1
        else:
            a1.append(float(eq1[i]))
            i = i+1
    return a1,c1



eq1 = input("Enter the First Equation : ")
x1, c1 = parser(eq1)
eq2 = input("Enter the Second Equation : ")
x2,c2 = parser(eq2)

a1 = x1[0]
b1 = x1[1]
a2 = x2[0]
b2 = x2[1]

a = np.array([[a1,b1],[a2,b2]])
b = np.array([c1,c2])

def det():
    return a1*b2 - b1*a2

def adjoint():
    return np.array([[b2,-b1],[-a2,a1]])



a_inv =  adjoint()/det()


res = np.matmul(a_inv,b)


print("s : ",res[0],"t : ",res[1])




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






