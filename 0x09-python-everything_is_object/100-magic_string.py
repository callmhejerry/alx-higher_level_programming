def magic_string(count=[0]):
    count[0] += 1
    return "BestSchool" * count[0]

for i in range(10):
    print(magic_string())