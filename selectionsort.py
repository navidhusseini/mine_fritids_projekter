A = [1,5,757,4,23,24,56,5746]
AS = []

while A != []:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x
    AS.append(minimum)
    A.remove(minimum)

print(AS)