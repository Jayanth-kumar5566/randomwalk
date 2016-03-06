import pylab
import numpy as np
import random
import time
class location(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def move(self,dx,dy):
		self.x=self.x+dx
		self.y=self.y+dy
		return(self.x,self.y)
	def getx(self):
		return self.x
	def gety(selfPython):
		return self.y
	def dist(self,other):
		d=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
		return d
	def printloc(self):
		return (self.x,self.y)
		#return(other.x,other.y)
class drunk(object):
	def __init__(self,name,location):
		#location.__init__(self.x,self.y)	
		self.drunk={}
		self.drunk[name]=location
	
	def takestep(self,name):
		l=self.drunk[name]
		
		a=range(-1,1)
		b=range(-1,1)
		dx=random.choice(a)
		dy=random.choice(b)		
		q=location.move(l,dx,dy)
		w=q[0]
		x=q[1]
		e=location(w,x)		
		self.drunk[name]=e
		return w,x	
	def getloc(self,name):
		z=self.drunk[name]
		location.printloc(z)
		
a=location(1,1)
d=drunk("jayanth",a)
#n=int(raw_input("number of steps"))
x=[]
y=[]
def walk(drun,n):
	pylab.ion()
	i=0	
	while i<=n:		
		q=drun.takestep("jayanth")		
		v=drun.getloc("jayanth")
		w=q[0]
		x=q[1]
		pylab.plot(w,x,'o')
		pylab.axis([-25,25,-25,25])
		pylab.draw()		
		time.sleep(0.1)
		i=i+1
	return v
X=walk(d,1000)
b=location(2,2)
print location.dist(a,b)		

			
	
