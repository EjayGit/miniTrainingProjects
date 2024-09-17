"""with open('binary_file', 'bw') as b_file:
    for i in range(21):
        b_file.write(bytes([i]))
        b_file.write(bytes(range(255)))

with open('binary_file', 'br') as b_file:
    for i in b_file:
        print(i)"""

customNumber = 73495836583689237658937653287
with open('binary_file2', 'bw') as bin_file:
    bin_file.write(customNumber.to_bytes(15, byteorder='big'))

#with open('binary_file2', 'ba') as bin_file:
 #   bin_file.write(customNumber.to_bytes(15, byteorder='big'))

with open('binary_file2', 'br') as bin_file:
    a = int.from_bytes(bin_file.read(), byteorder = 'big')

print(a)