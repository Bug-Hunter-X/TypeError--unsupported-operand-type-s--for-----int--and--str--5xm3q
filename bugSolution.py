def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after filtering non-numeric values
    total = sum(numeric_numbers)
    return total / len(numeric_numbers)

# Example usage with error handling:
average = calculate_average([1, 2, 3, 'a'])
print(f"Average: {average}")
average = calculate_average([1,2,3,4])
print(f"Average: {average}")
average = calculate_average([])
print(f"Average: {average}")
