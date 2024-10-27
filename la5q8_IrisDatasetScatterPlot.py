import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
print(iris.head())
plt.figure(figsize=(10,6))
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue ="species", palette="deep", s=100)
plt.title("Sepal length vs width (iris database)")

plt.xlabel("sepal length(cm)")
plt.ylabel("sepal width(cm)")

plt.show()