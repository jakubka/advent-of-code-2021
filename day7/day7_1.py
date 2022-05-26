from collections import defaultdict

input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

crabs_by_position = defaultdict(int)

min_position = input[0]
max_position = input[0]
for crab_position in input:
    crabs_by_position[crab_position] += 1
    min_position = min_position if min_position < crab_position else crab_position
    max_position = max_position if max_position > crab_position else crab_position

fuel_used = 0
while min_position != max_position:
    if crabs_by_position[min_position] < crabs_by_position[max_position]:
        crabs_by_position[min_position + 1] += crabs_by_position[min_position]
        fuel_used += crabs_by_position[min_position]
        min_position += 1
    else:
        crabs_by_position[max_position - 1] += crabs_by_position[max_position]
        fuel_used += crabs_by_position[max_position]
        max_position -= 1

print(f'Final position: {min_position}')
print(fuel_used)