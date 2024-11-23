import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r' \d+\.\d+| \d+ '
    for match in re.finditer(pattern, text):
        yield float(match.group())



def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


text = "Сьогодні ми продали 50.0 мішків картоплі, 5.6 кілограм цибулі, 10.0 буряків і 20.0 кілограм моркви"
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}") 
