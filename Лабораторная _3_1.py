def searching(list_, name):
    for ind, fruit in enumerate(list_):
        if fruit == name:
            return ind
items_list = ['яблоко', 'лимон', 'помело', 'апельсин', 'банан', 'нектарин']
for find_item in ['лимон', 'груша', 'нектарин']:
    index_item = searching(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")