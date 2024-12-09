def count_letters(text):
    lower_text = {}
    for symbol in text:
        if symbol.isalpha():
            symbol = symbol.lower()
            lower_text[symbol] = lower_text.get(symbol, 0) + 1
    return lower_text
def calculate_frequency(lower_text):
    total_letters = sum(lower_text.values())
    frequency_dict = {}
    for letter, count in letter_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = round(frequency, 2)
    return frequency_dict

main_str = """
Мой первый друг, мой друг бесценный!
И я судьбу благословил,
Когда мой двор уединенный,
Печальным снегом занесенный,
Твой колокольчик огласил.

Молю святое провиденье:
Да голос мой душе твоей
Дарует то же утешенье,
Да озарит он заточенье
Лучом лицейских ясных дней!
"""
letter_count = count_letters(main_str)
frequency_dict = calculate_frequency(letter_count)

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")