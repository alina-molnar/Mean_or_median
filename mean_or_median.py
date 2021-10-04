import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create weekdays' list.
weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# Create cash amount list.
amount = [10, 10, 5, 20, 15, 15, 60]

# Zip the two lists in a dataframe.
cash_df = pd.DataFrame(zip(weekdays, amount), columns=["weekday", "amount"])

# Create list of unique amounts to be used as ticks on x axis.
unique_amount = cash_df["amount"].unique()

# Plot amount of cash each day.
graph = sns.lineplot(x="weekday", y="amount", data=cash_df, marker="o")
graph.set(title="Amount each day", xlabel="Weekday", ylabel="Amount")
plt.show()

# Plot distribution of amount, mark mean and median.
graph = sns.kdeplot(x="amount", data=cash_df)
graph.axvline(x=cash_df["amount"].median(), color="#2ca02c", linestyle="solid", label="median")
graph.axvline(x=cash_df["amount"].mean(), color="#ff7f0e", linestyle="dashed", label="mean")
graph.set(title="Distribution mean and median", xlabel="Amount")
graph.set_xticks(unique_amount)
graph.set_xlim([0, 65])
graph.legend()
plt.show()
