import matplotlib.pyplot as plt
l=[]
p=0
while p<100:
	p=p+1
	for a in range(0,100):
		if a%p==0:
			break
		else:
			l.append(a)			
print l
plt.plot(l,'-ro')
plt.axis([0,7,0,15])
plt.xlabel("Numbers")
plt.ylabel("Prime numbers")
plt.show()
