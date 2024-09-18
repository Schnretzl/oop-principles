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
        try:
            self.__allocated_budget = new_budget if new_budget >= 0 else self.__allocated_budget
        except:
            print("Invalid budget amount")