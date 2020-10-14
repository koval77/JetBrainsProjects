A = int(input())
B = int(input())
H = int(input())
if H < A:
    print("Deficiency")
else:
    if H <= B:
        print("Normal")
    else:
        print("Excess")
