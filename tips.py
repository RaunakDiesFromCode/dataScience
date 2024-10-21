import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
plt.figure(figsize=(6,6))
sns.barplot(data=tips, x="day",y="total_bill", estimator=sum, palette="muted")
plt.title("Age distribution of tips pasengers")

plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()