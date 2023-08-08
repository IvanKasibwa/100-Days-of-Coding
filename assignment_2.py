#(-P ^ - Q) v (Q ^ -R)

P=True
Q=False
R=True

Group_1=not P or not Q # F or T = T
Group_2=Q and not R # F and F= F 
Conclusion=Group_1 or Group_2 #T or F =T
print("The conclusion is:", Conclusion)