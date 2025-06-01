# Discount Price
def calculate_discount_price(original_price, discount_percentage):
    discount = original_price * discount_percentage / 100
    return original_price - discount

# Kilometres to Miles
def km_to_miles(km):
    return km * 0.621371

# Holiday Cost
def calculate_holiday_cost(nights, nightly_rate, airfare, car_rental_daily_rate):
    return (nights * nightly_rate) + airfare + (nights * car_rental_daily_rate)

# Deep Sleep Calculation (Percentage)
def deep_sleep_percentage(deep_sleep_hours, total_sleep_hours):
    if total_sleep_hours == 0:
        return 0
    return (deep_sleep_hours / total_sleep_hours) * 100

# Example usage
if __name__ == "__main__":
    print("Discount Price:", calculate_discount_price(200, 15))
    print("Km to Miles:", km_to_miles(10))
    print("Holiday Cost:", calculate_holiday_cost(5, 100, 300, 40))
    print("Deep Sleep %:", deep_sleep_percentage(2, 8))