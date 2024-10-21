import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
print(titanic.head())
plt.figure(figsize=(10,6))
sns.histplot(data=titanic, x="age", bins=30, kde=True, color="")
plt.title("Age distribution of Titanic pasengers")

plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()