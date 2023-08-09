#TASK 01
#Convert the following questions into lines of code:-
#A
#(p∨¬q) and q

p=True
q=False
q=False

Group1=p or not q #T or T= T
Group2=Group1 and q #T and T = T
print("TASK 1A: ", Group1)

#B

#(p or q) not (¬q and ¬p)

p=False
q=True

Group_A=p or q # F or T= F
Group_B = not q and not p # F and T= F
Group_C = Group_A and Group_B # F and F =F
print("TASK 1B: ", Group_C)