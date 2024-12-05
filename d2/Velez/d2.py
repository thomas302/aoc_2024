import timeit
input = open('..\\input')
all_data = input.readlines()
# print(all_data)
cleaned_data = []
sort_safe = False
diff_safe = False
safe = False
total_safe_part1 = 0
total_safe_part2 = 0

for i in range(len(all_data)):
    x = list(map(int, all_data[i].split()))
    cleaned_data.append(x)
count = 0
# Part Two: Problem Dampener
start = timeit.default_timer()
count = 0
for x in range(len(cleaned_data)):
    target_list = cleaned_data[x]
    for i in range(len(target_list)):
        count +=1

        test_removed = target_list[i]
        del target_list[i]

        if target_list == sorted(target_list) or target_list == sorted(target_list, reverse=True):
            sort_safe = True
        else:
            sort_safe = False

        for y in range(len(target_list)-1):
            if abs(target_list[y] - (target_list[y+1])) >= 1 and abs(target_list[y] - (target_list[y+1])) <= 3:
                diff_safe = True
            else:
                diff_safe = False
                break

        if diff_safe and sort_safe:
            total_safe_part2 += 1
            break

        target_list.insert(i, test_removed)
time = timeit.default_timer()-start

print("Total safe is:", total_safe_part1)
print("Total safe with Problem Damperner is:", total_safe_part2)
print(count)
print(time)

