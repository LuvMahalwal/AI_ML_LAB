import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.linspace(0,2,50)
plt.scatter(x,x,label="linear")
plt.scatter(x,x**2,label="quadratic")
plt.scatter(x,x**3,label="cubic")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("Practice Graph")
plt.show()
ds=pd.read_csv(r"C:\Users\student\Desktop\New folder (4)\1.csv",encoding='cp1252')
plt.bar(ds["genre"],ds["quantity"],color="green",edgecolor="white")
plt.show()
d=pd.read_csv(r"C:\Users\student\Desktop\New folder (4)\2.csv",encoding='cp1252')
score_india = d['score_india']
score_au = d['score_au']
legend = ['India', 'Austrailia']
plt.hist([score_india, score_au], color=['orange', 'green'])
plt.xlabel("Runs/Delivery")
plt.ylabel("Frequency")
plt.legend(legend)
plt.xticks(range(0, 7))
plt.yticks(range(1, 20))
plt.title('Champions Trophy 2013 Final\n Runs scored in 4 overs')
plt.show()