import itertools

def sum_of_numbers(byte_1, byte_2, byte_3, byte_4):
	return byte_1 + byte_2 + byte_3 + byte_4



def generate_ip_addresses():
    for ip in itertools.product(range(256), repeat=4):
        if ip[0] in (0, 10, 127, 169, 172, 192):
            continue
        yield tuple(ip)

    
def generate_pair_of_bytes():
    for bytes_pair in itertools.product(range(256), repeat=2):
        yield tuple(bytes_pair)