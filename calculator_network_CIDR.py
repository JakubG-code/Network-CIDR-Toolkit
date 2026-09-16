# Convert an IPv4 address (string) into a 32-bit integer
def ip_to_int(ip):
    result = 0

    for octet in ip.split("."):
        result = (result << 8) | int(octet)

    return result


# Convert a 32-bit integer back into an IPv4 address
def int_to_ip(number):
    return ".".join(
        str((number >> shift) & 255)
        for shift in (24, 16, 8, 0)
    )

print("=" * 50)
print("CIDR NETWORK CALCULATOR v.1")
print("=" * 50)

cidr = input("\nEnter an address (e.g. 192.168.10.55/24): ")

ip_str, prefix_str = cidr.split("/")
prefix = int(prefix_str)

ip = ip_to_int(ip_str)

mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF

network_address = ip & mask

broadcast = network_address | (~mask & 0xFFFFFFFF)

first_host = network_address + 1
last_host = broadcast - 1

print("IP Address:", ip_str)
print("Subnet Mask:", int_to_ip(mask))
print("Network Address:", int_to_ip(network_address))
print("Broadcast Address:", int_to_ip(broadcast))
print(
    "Host Range:",
    int_to_ip(first_host),
    "-",
    int_to_ip(last_host)
)
print("Example Gateway:", int_to_ip(first_host))