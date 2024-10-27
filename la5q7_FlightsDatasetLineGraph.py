import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
print(flights.head())
plt.figure(figsize=(10,6))
sns.lineplot(data=flights, x="year", y="passengers", hue ="month", palette="tab10")
plt.title("Number of airline passengers over time")

plt.xlabel("year")
plt.ylabel("Number of passengers")

plt.show()