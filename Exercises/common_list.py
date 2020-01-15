a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = []

# checking which list has less elements because if I run "for i in range.." more then required I get the error: 'list index out of range'
if len(a) > len(b):
    len = len(b)
else:
    len = len(a)

for i in range(len):
    if str(a[i]) in str(b):
        if str(a[i]) not in list:
            list.append(str(a[i]))
print("\n The common integers between list 'a' and list 'b' are: " + str(list))
