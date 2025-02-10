def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    return total / len(numbers)

# Example usage with potential error:
average = calculate_average([1, 2, 3, 'a'])
print(f"Average: {average}")