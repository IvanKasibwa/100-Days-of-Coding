#(-P ^ - Q) v (Q ^ -R)

P=True
Q=False
R=True

Group_1=not P and not Q # F and T = F
Group_2=Q and not R # F and F= F 
Conclusion=Group_1 or Group_2 #F or F =F
print("The conclusion is:", Conclusion)