from math import *
size(1500,1000)  
translate(1000,550)  
background(0)
stroke(255)
strokeWeight(0.1)

#Length of each individual line
len = 5    

#FOR A COLOUR GRADIENT    
def g(x):
    r = 255
    g = 0
    b = 0
    pushMatrix()
    while x != 1:
        if x%2==0:
            r+=0
            g+=2
            b+=0
            stroke(r,g,b)
            x=x/2.0

            rotate(pi/20.0) 
            line(0,0,0,-len)
            translate(0,-len)
            
        else:
            
            r+=0
            g+=2
            b+=0
            stroke(r,g,b)
            
            x = (3*x)+1
            rotate(-pi/10.0)  
            line(0,0,0,-len)
            translate(0,-len)
            #a+=1
    popMatrix()

for i in range(1):
    for i in range(1,10000): 
        g(i)
    rotate(pi/2.0) 

#THE EYE OF THE BIRD
#stroke(0) 
#fill(0)   
#circle(0,-50,10) 
    
save('collatzbird.png')
        
