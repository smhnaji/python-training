def count_2s_method_1(file_address):
    file = open(file_address, 'r')
    
    counter1 = 0
    counter2 = 0

    for line in file.readlines():

        # This is buggyyyyyyyyyyyyyy:        
        # for number in line.split(sep=' '):

        # This fixes the bug:
        for number in line.strip().split(sep=' '):
            print(number)
            if number == '2':
                counter1 += 1

        for char in line:
            if char == '2':
                counter2 += 1
    
    return counter1, counter2

print(count_2s_method_1('myfile.txt'))

print('++++++++++++++')
print('++++++++++++++')
print('++++++++++++++')

def count_2s_method_2(file_address):
    with open(file_address, 'r') as input_file:
        return input_file.read().count('2')


print(count_2s_method_2('myfile.txt'))