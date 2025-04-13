import itertools
import utils

gen = utils.generate_ip_addresses()

sum_dict = dict()

for byte_1, byte_2, byte_3, byte_4 in gen:
    s = byte_1 + byte_2 + byte_3 + byte_4
    if s in sum_dict:
        sum_dict[s].append(f"{byte_1}.{byte_2}.{byte_3}.{byte_4}")
    else:
        sum_dict[s] = [f"{byte_1}.{byte_2}.{byte_3}.{byte_4}"]


f = open('pairs_ip_list.txt', 'w')

for key, value in sum_dict.items():
    for ip1, ip2 in itertools.product(value, repeat=2):
        f.write(f'{ip1} {ip2}\n')

f.close()