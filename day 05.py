full_name = input("Enter your full name: ")
name_without_space = ""
for ch in full_name:
    if ch != " ":
        name_without_space = name_without_space + ch
L = 0
for _ in name_without_space:
    L = L + 1
PLI = L % 3
print("Length of Name (L):", L)
print("PLI Value:", PLI)
n = int(input("Enter number of resource requests: "))
requests = []
for i in range(n):
    value = int(input("Enter request value: "))
    requests.append(value)
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
valid_count = 0
for req in requests:
    if req < 0:
        invalid_requests.append(req)
    else:
        valid_count = valid_count + 1
        if req == 0:
            pass
        elif req >= 1 and req <= 20:
            low_demand.append(req)
        elif req >= 21 and req <= 50:
            moderate_demand.append(req)
        else:
            high_demand.append(req)
print("Before Personalization:")
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
final_low = []
final_moderate = []
final_high = []
removed_due_to_pli = 0
if PLI == 0:
    for item in low_demand:
        removed_due_to_pli = removed_due_to_pli + 1
    for item in moderate_demand:
        final_moderate.append(item)
    for item in high_demand:
        final_high.append(item)
elif PLI == 1:
    for item in low_demand:
        final_low.append(item)
    for item in moderate_demand:
        final_moderate.append(item)
    for item in high_demand:
        removed_due_to_pli = removed_due_to_pli + 1
else:
    for item in low_demand:
        removed_due_to_pli = removed_due_to_pli + 1
    for item in high_demand:
        removed_due_to_pli = removed_due_to_pli + 1
    for item in moderate_demand:
        final_moderate.append(item)
print("After Personalization:")
print("Low Demand:", final_low)
print("Moderate Demand:", final_moderate)
print("High Demand:", final_high)
print("Total Valid Requests:", valid_count)
print("Removed Due to PLI:", removed_due_to_pli)
