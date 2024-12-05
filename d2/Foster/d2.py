import timeit
with open("..\\input", 'r+') as f:
    reportstrings = f.readlines();

itemized_reports = [list(map(int, x.split())) for x in reportstrings]

# part 1
safe = 0
count = 0
def report_test(a, d):
    global count
    count += 1
    if d == "asc":
        return list(a[i] < a[i + 1] and abs(a[i] - a[i + 1]) <= 3 for i in range(len(a) - 1))
    if d == "des":
        return list(a[i] > a[i + 1] and abs(a[i] - a[i + 1]) <= 3 for i in range(len(a) - 1))

for report in itemized_reports:
    is_ascending = report_test(report, 'asc').count(False) == 0
    is_descending = report_test(report, 'des').count(False) == 0 
    if is_ascending or is_descending:
        safe += 1

print(safe)

# part 2
safe = 0
count = 0;
start = timeit.default_timer()
for report in itemized_reports:
    ascending = report_test(report, "asc")
    is_ascending = ascending.count(False) == 0
    if is_ascending:
        safe += 1
        continue

    descending = report_test(report, "des")
    is_descending = descending.count(False) == 0
    if is_descending:
        safe += 1
        continue
    
    location = ascending.index(False)
    new_report = report.copy()
    new_report.pop(location)
    new_ascending = report_test(new_report, "asc")
    is_ascending = new_ascending.count(False) == 0
    if is_ascending:
        safe += 1
        continue
    
    location = ascending.index(False) + 1
    new_report = report.copy()
    new_report.pop(location)
    new_ascending = report_test(new_report, "asc")
    is_ascending = new_ascending.count(False) == 0
    if is_ascending:
        safe += 1
        continue
    
    location = descending.index(False)
    new_report = report.copy()
    new_report.pop(location)
    new_descending = report_test(new_report, "des")
    is_descending = new_descending.count(False) == 0
    if is_descending:
        safe += 1
        continue
    

    location = descending.index(False) + 1
    new_report = report.copy()
    new_report.pop(location)
    new_descending = report_test(new_report, "des")
    is_descending = new_descending.count(False) == 0
    if is_descending:
        safe += 1
        continue
time = timeit.default_timer()-start
    
print(safe)

print(count)

print(time)
