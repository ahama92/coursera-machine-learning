import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class linear_regression():
    def __init__(this):
        this.m=1
        this.x=np.zeros(this.m)
        this.y=np.zeros(this.m)
        this.theta0=0
        this.theta1=0
        
    def hypothesis(this,x):
        return this.theta0+this.theta1*x
        
    def cost(this):
        temp=0
        for i in range(0,this.m):
            temp=temp+(this.hypothesis(this.x[i])-this.y[i])**2
        temp=temp/(2.0*this.m)
        return temp
    
    def update(this,alpha):
        D0,D1=this.gradient()
        this.theta0=this.theta0-alpha*D0
        this.theta1=this.theta1-alpha*D1
        pass
    
    def gradient(this):
        temp=0
        for i in range(0,this.m):
            temp=temp+(this.hypothesis(this.x[i])-this.y[i])
        D0=temp/this.m
        
        temp=0
        for i in range(0,this.m):
            temp=temp+(this.hypothesis(this.x[i])-this.y[i])*this.x[i]
        D1=temp/this.m
        
        return D0,D1
    
    def train(this):
        alpha=0.9
        temp1=this.cost()
        a.update(alpha)
        temp2=this.cost();
        while np.absolute(temp1-temp2)>1e-10:
            temp1=temp2
            a.update(alpha)
            temp2=this.cost()
            
    def animate_train(this,alpha):
        fig,ax=plt.subplots()
        scat=ax.scatter(this.x,this.y)
        x=np.array([0,1])
        y=this.theta0+this.theta1*x
        line=plt.plot(x,y,'r')
        
        ani=animation.FuncAnimation(fig,this.update,interval=10)
        plt.show()
        
    def show(this):
        plt.scatter(this.x,this.y,s=10)
        x=np.array([0,1])
        y=this.theta0+this.theta1*x
        plt.plot(x,y,'r')
        plt.show()

a=linear_regression()
a.m=101
# np.random.seed(0) # Seeding the np.random with a fixed value will cause the method to generate the same random numbers over and over again.
a.x=np.random.rand(a.m,1)
a.y=np.random.rand(1)+np.random.rand(1)*a.x+np.random.rand(a.m,1)/3.0

a.animate_train(0.1)

