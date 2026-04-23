import random
import pandas as pd
import numpy as np
import math

def generate_data(n):
    data = []
    for i in range(1, n+1):
        m = random.randint(0, 100)
        a = random.randint(0, 100)
        ass = random.randint(0, 50)
        p = (m*0.6 + ass*0.4) * math.log(a+1)
        data.append((i, m, a, ass, p))
    return data


def classify_students(data):
    d = {"At Risk": [], "Average": [], "Good": [], "Top Performer": []}

    for x in data:
        id, m, a, _, _ = x

        if m < 40 or a < 50:
            d["At Risk"].append(id)
        elif m <= 70:
            d["Average"].append(id)
        elif m > 90 and a > 80:
            d["Top Performer"].append(id)
        else:
            d["Good"].append(id)

    return d


def analyze_data(data):
    df = pd.DataFrame(data, columns=["ID","Marks","Attendance","Assignment","Perf_Index"])
    marks = df["Marks"]

    mean = sum(marks) / len(marks)
    median = np.median(marks)
    std = np.std(marks)
    max_m = max(marks)

    corr = np.corrcoef(df["Marks"], df["Attendance"])[0][1]

    # normalization fix
    if max(marks) == min(marks):
        df["Normalized"] = [0 for _ in marks]
    else:
        df["Normalized"] = [(x - min(marks)) / (max(marks) - min(marks)) for x in marks]

    unique_marks = set(marks)

    if std < 15 and len(df[(df["Marks"] > 90) & (df["Attendance"] > 80)]) >= 2:
        insight = "Stable Academic System"
    elif len(df[df["Attendance"] < 50]) > 3:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"

    return df, mean, median, std, max_m, corr, insight, unique_marks


# -------- Main --------
n = 10+int(input("Enter your roll number last digit: "))

data = generate_data(n)
cat = classify_students(data)

df, mean, median, std, max_m, corr, insight, unique_marks = analyze_data(data)

print("\n--- DataFrame Table ---")
print(df)

print("\n--- Categorized Dictionary ---")
print(cat)

print("\nUnique Marks (Set):", unique_marks)

print("\n--- Statistical Summary ---")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Correlation:", corr)

print("\n--- Tuple Output ---")
print((mean, std, max_m))

print("\n--- Final System Insight ---")
print(insight)
