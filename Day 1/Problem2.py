from collections import Counter




def read_and_separate(file_path):
    list1, list2 = [], []
    
    # Open the file and read lines
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two numbers and convert them to integers
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    
    return list1, list2

# Example usage
file_path = '/home/obaidsafi31/Desktop/Avent of Code/Day 1/in.txt'  # Replace with the actual file path
left_list, right_list = read_and_separate(file_path)



list1_sorted = sorted(left_list) 
list2_sorted = sorted(right_list)


right_count = Counter(list2_sorted)

similarity_score = sum(num * right_count[num] for num in list1_sorted)

print(similarity_score)