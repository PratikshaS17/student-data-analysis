import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print(df)

df["Average"] = df[["Maths","Science","English"]].mean(axis=1)

print(df)

topper = df.loc[df["Average"].idxmax()]
print("Topper:", topper["Name"])

df.plot(x="Name", y=["Maths","Science","English"], kind="bar")
plt.title("Student Marks")
plt.show()