import itertools
import utils

gen = utils.generate_pair_of_bytes()

sum_dict = dict()

for byte_1, byte_2 in gen:
    s = byte_1 + byte_2
    if s in sum_dict:
        sum_dict[s].append((byte_1, byte_2))
    else:
        sum_dict[s] = [(byte_1, byte_2)]


f = open('solo__advanced_ip_list.txt', 'w')

for key, value in sum_dict.items():
    for (byte_1, byte_2), (byte_3, byte_4) in itertools.product(value, repeat=2):
        if byte_1 in (0, 10, 127, 169, 172, 192):
            continue
        f.write(f'{byte_1}.{byte_2}.{byte_3}.{byte_4}\n')

f.close()
        
