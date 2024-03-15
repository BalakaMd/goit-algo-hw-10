# Висновки щодо обчислення інтеграла методом Монте-Карло

У цьому домашньому завданні ми обчислювали значення певного інтеграла за допомогою методу Монте-Карло та порівнювали його з результатом, отриманим за допомогою функції `quad` з бібліотеки SciPy.

## Завдання та методика обчислення

Ми обрали функцію `f(x) = x^2` для обчислення інтеграла на інтервалі від 0 до 2. Спочатку ми побудували графік цієї функції та знайшли площу під кривою, використовуючи метод Монте-Карло. Потім ми також використали функцію `quad` для обчислення точного значення інтеграла.

## Результати

1. За допомогою методу Монте-Карло отримали приблизне значення інтеграла: 2.667.
2. Результат, отриманий за допомогою функції `quad`: 2.667.

## Висновки

Обидва методи дали дуже близькі результати. Це підтверджує правильність розрахунків, зроблених методом Монте-Карло. Таким чином, можемо стверджувати, що застосування методу Монте-Карло є ефективним для обчислення значень інтегралів, особливо в складних випадках, коли аналітичне обчислення не є можливим або складним.