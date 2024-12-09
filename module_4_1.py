# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide

num = 10

fake_result = fake_divide(num, 0)
true_result = true_divide(num, 0)

print(f"Результат fake_divide: {fake_result}")
print(f"Результат true_divide: {true_result}")