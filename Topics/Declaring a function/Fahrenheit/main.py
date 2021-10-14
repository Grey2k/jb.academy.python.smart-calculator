def fahrenheit_to_celsius(temp_f: float) -> float:
    temp_c = (temp_f - 32) * 5 / 9
    return round(temp_c, 3)
