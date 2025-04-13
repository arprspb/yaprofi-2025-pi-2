import utils

def check_solo_ip(byte_1, byte_2, byte_3, byte_4):
    return byte_1 + byte_2  == byte_3 + byte_4

gen = utils.generate_ip_addresses()


out_file = open('solo_ip_list.txt', 'w')


for byte_1, byte_2, byte_3, byte_4 in gen:
    if check_solo_ip(byte_1, byte_2, byte_3, byte_4):
        out_file.write(f'{byte_1}.{byte_2}.{byte_3}.{byte_4}\n')

out_file.close()