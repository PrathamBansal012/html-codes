import matplotlib.pyplot as plt
boys_marks=[12,34,57,69,23,46,12,3,79,99,98]
girls_marks=[22,14,17,19,13,16,12,13,19,19,98]
type=[boys_marks,girls_marks]
colors=['g','r']
label=['boys','girls']
bins = [60, 80, 100]
plt.xlabel("marks obtained")
plt.ylabel("gender")
plt.hist(type,bins=bins,width=0.95,color=colors,label=label,orientation="horizontal")
plt.title("marks")
plt.legend()
plt.show()