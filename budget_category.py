class BudgetCategory:
    def __init__(self, __category, __allocated_budget = 0):
        self.__category = __category
        self.__allocated_budget = __allocated_budget if __allocated_budget >= 0 else 0
        
    def get_category(self):
        return self.__category
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category(self, new_category):
        try:
            self.__category = new_category if self.__category.isalpha() else self.__category
        except:
            print("Invalid category name")
            
    def set_allocated_budget(self, new_budget):
        if isinstance(new_budget, int) and new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print("Invalid budget amount")
            
    def add_expense(self, expense):
        if isinstance(expense, int) and expense >= 0:
            if expense > self.__allocated_budget:
                print("Expense exceeds allocated budget")
            else:
                self.__allocated_budget -= expense
        else:
            print("Invalid expense amount")