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


total_dis = sum(abs(l-r) for l,r in zip(list1_sorted, list2_sorted))
total_dis
print (total_dis)