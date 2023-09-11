def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0]==4 and s[1]==4

def successors(s):
    x, y, z = s
    
        #empty 8L
    if x>0:
        yield((0,y,z),x)
        
    #empty 8L
    if y>0:
        yield((x,0,z),y)
    
    #empty 8L
    if z>0:
        yield((x,y,0),z)
    
    
    #fill 8L from 5L
    if y>0 and x<8:
        t= min(y, 8-x)
        yield((x+t, y-t,z),t)
    
    #fill 8L from 3L
    if z>0 and x<8:
        t=min(z, 8-x)
        yield((x+t,y,z-t),t)
    
    #fill 5L from 8L
    if x>0 and y<5:
        t=min(x,5-y)
        yield((x-t,y+t,z),t)
        
    #fill 5L from 3L
    if z>0 and y<5:
        t=min(z,5-y)
        yield((x,y+t,z-t),t)
    
     #fill 3L from 8L
    if x>0 and z<3:
        t=min(x,3-z)
        yield((x-t,y,z+t),t)
        
    #fill 3L from 5L
    if y>0 and z<3:
        t=min(y,3-z)
        yield((x,y-t,z+t),t)
    

    
    
    
    
  
    

