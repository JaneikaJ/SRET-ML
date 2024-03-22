"""
COMPUTING GRADIENT OF A LOSS FUNCTION
"""

#bgd
def grad_W1(x1,x2,y,w1,w2):
    w1new= -2*(y-(w1*x1+w2*x2))*x1
    return(w1new)



def grad_W2(x1,x2,y,w1,w2):
    w2new= -2*(y-(w1*x1+w2*x2))*x2
    return(w2new)

x1=[0,2,1,-2]
x2=[1,1,0,1]
y=[1,9,1,7]
w1=1
w2=3


for a,b,c in zip(x1,x2,y):
    w1_grad=grad_W1(a,b,c,w1,w2)
    w2_grad=grad_W2(a,b,c,w1,w2)


    print("W1 gradient",(a,b),":",w1_grad)
    print("W2 gradient",(a,b),':',w2_grad)
    

#using learning rate

from statistics import mean

def grad_W1(x1,x2,y,w1,w2):
    w1new= -2*(y-(w1*x1+w2*x2))*x1
    return(w1new)

def grad_W2(x1,x2,y,w1,w2):
    w2new= -2*(y-(w1*x1+w2*x2))*x2
    return(w2new)

arr_W1=[]
arr_W2=[]
x1=[0,2,1,-2]
x2=[1,1,0,1]
y=[1,9,1,7]
w1=1
w2=3

for a,b,c in zip(x1,x2,y):
    w1_grad=grad_W1(a,b,c,w1,w2)

    w2_grad=grad_W2(a,b,c,w1,w2)
    arr_W1.append(w1_grad)
    arr_W2.append(w2_grad)

    print(mean(arr_W1))
    w1=w1-0.01*(mean(arr_W1))
    w2=w2-0.01*(mean(arr_W2))

print(arr_W1)
print("Updated weigth:\n","W1 :",w1,"W2 :",w2)

