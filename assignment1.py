#((P ∨ Q) ∧ R) v ((P ∧ R) ∨ (Q ∧ R))

P=True
Q=False
R=True

Group_1=P or Q # T or F =T
Group_2=Group_1 and R # T and T =T
Group_3=P and R #T and T= T
Group_4=Q and R # F and T= F
Group_5=Group_3 or Group_4 #T or F =T
Conclusion=Group_2 or Group_5 # T or T = T
print(Conclusion)