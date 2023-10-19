numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(numbers[0:4:1]) + sum(numbers[5:-1:1]) + numbers[-1]
count_numbers = len(numbers)
average_numbers = sum_numbers / count_numbers
numbers[4] = average_numbers
print("Измененный список:", numbers)
