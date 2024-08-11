# TODO
custom_list = [1,2,3,4,5,6,7,8,9,10]
output_list = []
for num in range(len(custom_list), 0, -1):
    output_list.append(custom_list[num-1])
print(output_list)