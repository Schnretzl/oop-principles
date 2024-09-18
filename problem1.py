# 1. Encapsulation in Personal Budget Management
from budget_category import BudgetCategory

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget.
# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget.
# Task 3: Add Budget Functionality
# Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
