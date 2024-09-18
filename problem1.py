# 1. Encapsulation in Personal Budget Management


# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget.
class BudgetCategory:
    def __init__(self, __category, __allocated_budget = 0):
        self.__category = __category
        self.__allocated_budget = __allocated_budget

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
