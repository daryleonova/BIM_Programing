from calendar import month

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mounths = 0
while money_capital+salary >= spend:
    money_capital = money_capital + salary - spend
    mounths += 1
    spend = spend * (1+increase)
print('Количество месяцев, которое можно протянуть без долгов:', mounths)
