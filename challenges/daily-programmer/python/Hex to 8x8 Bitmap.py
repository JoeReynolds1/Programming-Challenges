pictures = [['FF' ,'81', 'BD', 'A5', 'A5', 'BD', '81', 'FF'],
['AA', '55', 'AA', '55', 'AA', '55', 'AA', '55'],
['3E' ,'7F', 'FC', 'F8', 'F8', 'FC', '7F', '3E'],
['93', '93', '93', 'F3', 'F3', '93', '93', '93']]

def hex_to_bit(n):
    converted = str(bin(int(n,16)))[2:].zfill(8)
    return converted

def output(*hex_values):
    for hex_value in hex_values:
        for bit in hex_to_bit(hex_value):
            if bit == '1':
                print('x',end='')
            else: print(' ',end='')
        print()


output(pictures[0])
