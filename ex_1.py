from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="Production_Optimization", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

water_constraint = 2 * lemonade + fruit_juice <= 100
sugar_constraint = lemonade <= 50
lemon_constraint = lemonade <= 30
fruit_puree_constraint = 2 * fruit_juice <= 40

model += water_constraint
model += sugar_constraint
model += lemon_constraint
model += fruit_puree_constraint

model += lemonade + fruit_juice

model.solve()

print("Лимонад:", lemonade.varValue)
print("Фруктовий сік:", fruit_juice.varValue)
