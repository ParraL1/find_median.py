#Name: Lilliana Parra
#Github username: ParraL1
#Date: 02/9/2022
#Description: Calculating the median of a list of numbers

def find_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2] + numbers[(len(numbers) - 1) // 2]) / 2


