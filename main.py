import re

def add(number_string):
    if not number_string.strip():
        return 0 
    try:
        numbers = list(map(int, re.split(r"[!|\\,:\;\(\)_{}\[\]/\n]+", number_string)))
        negative_numbers = []
        for number in numbers:
            if number < 0:
                negative_numbers.append(str(number))
        if len(negative_numbers) > 0:
            raise ValueError(f"Negative numbers not allowed {','.join(negative_numbers)}.")
        return sum(numbers)
    except ValueError:
        raise ValueError("Input string must contain valid numbers.")