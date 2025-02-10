def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_string = [10, 20, 'a', 40, 50]
result = calculate_average(my_list_with_string) #This will correctly print the average of numeric values
print(f"The average is: {result}") 