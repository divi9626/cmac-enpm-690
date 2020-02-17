import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,6.3,0.063)
y = np.sin(x)

train = np.arange(0,6.3,0.09)
test = np.arange(0,6.3,0.21)
o = np.sin(train)
plt.plot(o)

weights = []

# Training
# run for 3 indivisual cells .. 
#dicrete CMAC

for i in range(34):
    
    e = 2*i
    f = 2*i + 1
    g = 2*i + 2
    
      
    
    count = 80
    while count>0:
            
        a = train[e]*0.7
        b = train[f]
        c = train[g]*0.3
        sum = a+b+c
        error = (y[e]) - (sum)
                
        correction = error/1.8
        
        train[e] = correction + train[e]
        train[f] = correction + train[f]
        train[g] = correction + train[g]
        
        count = count - 1
        
    weights.append(sum)
print(weights)
a = len(weights)
print(a)
            
        

plt.plot(weights)       


# Testing 

test_error1 = np.zeros()
test_error2 = np.zeros()

for k in range(len(test)):
  
      # get weights at test indices 
    
    
    y[k]=weights[2*k]
    test_error1[k]=test[k]-y[k]
    test_error2[2*k]=test[k]-y[k]
    
''' plt.plot(weights,label="cmac")
plt.plot(y,label='orig')
plt.legend(loc=4)'''






