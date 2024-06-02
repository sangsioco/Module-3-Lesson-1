# Deep copy weekly sales

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
import copy

copied_sales = copy.deepcopy(weekly_sales)
copied_sales["Week 2"]["Electronics"] = 18000

print("Original weekly sales:")
print(weekly_sales)
print("\nCopied weekly sales with updated Electronics sales in Week 2:")
print(copied_sales)