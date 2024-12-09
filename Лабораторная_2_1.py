salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
mounths = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен
money_capital = 0

for i in range(mounths):
    money_capital += (spend - salary)
    spend *= increase

print('Подушка безопасности, чтобы протянуть 10 месяцев без долгов:', round(money_capital))
