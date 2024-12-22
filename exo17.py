numbers = []
shoe_sizes = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)


shoe_sizes.append(8)
shoe_sizes.append(9)
shoe_sizes.append(10)
shoe_sizes.append(11)
shoe_sizes.append(12)

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)




numbers.append(3)  # Adding a duplicate value
print("\nNumbers List with duplicate:", numbers)

shoe_sizes_loop = []
for size in range(8, 13):
    shoe_sizes_loop.append(size)
print("Shoe Sizes (created with loop):", shoe_sizes_loop)

combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)