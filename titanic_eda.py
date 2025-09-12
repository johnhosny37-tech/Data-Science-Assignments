import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load Titanic dataset
titanic_df = sns.load_dataset("titanic")

# ----- Data Cleaning -----
# Fill missing values
titanic_df["age"].fillna(titanic_df["age"].median(), inplace=True)
titanic_df["embarked"].fillna(titanic_df["embarked"].mode()[0], inplace=True)
titanic_df["deck"].fillna(titanic_df["deck"].mode()[0], inplace=True)
titanic_df["embark_town"].fillna(titanic_df["embark_town"].mode()[0], inplace=True)

# Remove duplicates
titanic_df.drop_duplicates(inplace=True)

# ----- Feature Engineering -----
titanic_df["Family_size"] = titanic_df['sibsp'] + titanic_df['parch'] + 1
titanic_df["is_alone"] = titanic_df['Family_size'].apply(lambda x: 1 if x == 1 else 0)
titanic_df["embarked_edited"] = titanic_df["embarked"].map({"S": 0, "C": 1, "Q": 2})
titanic_df["sex_edited"] = titanic_df["sex"].map({"male": 0, "female": 1})

# Label Encoding
le = LabelEncoder()
titanic_df["embark_town"] = le.fit_transform(titanic_df["embark_town"])
titanic_df["alive"] = le.fit_transform(titanic_df["alive"])

# ----- Exploratory Data Analysis -----
# 1. Survival vs Age Group
titanic_df["age_group"] = pd.cut(
    titanic_df["age"],
    bins=[0, 12, 20, 40, 60, 100],
    labels=["Child", "Teen", "Young Adult", "Middle Aged", "Senior Citizen"]
)

plt.figure(figsize=(12, 5))
sns.barplot(x="age_group", y="survived", data=titanic_df, ci=None, palette="Set1")
plt.title("Survival Rate by Age Group")
plt.tight_layout()
plt.savefig("survival_vs_age.png")  # save figure

# 2. Survival vs Sex
plt.figure(figsize=(6, 5))
sns.barplot(x="sex", y="survived", data=titanic_df, ci=None, palette="Set2")
plt.title("Survival Rate by Sex")
plt.tight_layout()
plt.savefig("survival_vs_sex.png")

# 3. Passenger Class Distribution
class_count = titanic_df["class"].value_counts()
plt.pie(class_count, labels=class_count.index, autopct="%1.1f%%", startangle=140)
plt.title("Passenger Class Distribution")
plt.savefig("class_distribution.png")

# 4. Survival Rate by Class
plt.figure(figsize=(6, 5))
sns.barplot(x="class", y="survived", data=titanic_df, ci=None, palette="Set2")
plt.title("Survival Rate by Class")
plt.tight_layout()
plt.savefig("class_vs_survival.png")

# 5. Heatmap: Survival by Family Size & Class
pivot = titanic_df.pivot_table(index="Family_size", columns="pclass", values="survived", aggfunc="mean")
sns.heatmap(pivot, annot=True, cmap="Blues")
plt.title("Survival Rate by Family Size and Class")
plt.tight_layout()
plt.savefig("family_class_heatmap.png")

# 6. Heatmap: Survival by Alone & Class
pivot2 = titanic_df.pivot_table(index="is_alone", columns="pclass", values="survived", aggfunc="mean")
sns.heatmap(pivot2, annot=True, cmap="Purples")
plt.title("Survival Rate by Alone and Class")
plt.tight_layout()
plt.savefig("alone_class_heatmap.png")

print("✅ EDA Completed. Figures saved as images.")
