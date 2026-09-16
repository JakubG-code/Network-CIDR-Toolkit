import random
import ipaddress


# Generate a random IPv4 interface and its corresponding network.
def generate_network():
    prefixes = [8, 16, 24, 25, 26, 27, 28, 29, 30]
    prefix = random.choice(prefixes)

    while True:
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        try:
            interface = ipaddress.ip_interface(f"{ip}/{prefix}")
            network = interface.network
            return interface, network
        except ValueError:
            pass


# Calculate all network information for the given interface.
def get_correct_answers(interface, network):
    net_addr = network.network_address
    broadcast = network.broadcast_address
    mask = network.netmask
    hosts = list(network.hosts())

    if hosts:
        first_host = hosts[0]
        last_host = hosts[-1]

        # Use the first host as an example default gateway.
        gateway = first_host
    else:
        first_host = "-"
        last_host = "-"
        gateway = "-"

    return {
        "ip": str(interface.ip),
        "mask": str(mask),
        "network": str(net_addr),
        "broadcast": str(broadcast),
        "range": f"{first_host} - {last_host}",
        "gateway": str(gateway)
    }


def main():
    print("=" * 50)
    print("IP ADDRESSING TRAINER v.1")
    print("=" * 50)

    interface, network = generate_network()
    answers = get_correct_answers(interface, network)

    print(f"\nThe computer has the following address:\n{interface}\n")

    user_ip = input("IP Address: ")
    user_mask = input("Subnet Mask: ")
    user_network = input("Network Address: ")
    user_broadcast = input("Broadcast Address: ")
    user_range = input("Host Range (e.g. 192.168.1.1 - 192.168.1.254): ")
    user_gateway = input("Example Gateway: ")

    score = 0

    checks = [
        ("IP Address", user_ip, answers["ip"]),
        ("Subnet Mask", user_mask, answers["mask"]),
        ("Network Address", user_network, answers["network"]),
        ("Broadcast Address", user_broadcast, answers["broadcast"]),
        ("Host Range", user_range, answers["range"]),
        ("Gateway", user_gateway, answers["gateway"])
    ]

    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)

    for name, user, correct in checks:
        if user.strip() == correct:
            print(f"✓ {name}")
            score += 1
        else:
            print(f"✗ {name}")
            print(f"  Your answer: {user}")
            print(f"  Correct answer: {correct}")

    print(f"\n🔥Final Score: {score}/6🔥")

    print(f"\nComputer Address: {interface}")
    print("Correct Answers:")
    print(f"IP Address: {answers['ip']}")
    print(f"Subnet Mask: {answers['mask']}")
    print(f"Network Address: {answers['network']}")
    print(f"Broadcast Address: {answers['broadcast']}")
    print(f"Host Range: {answers['range']}")
    print(f"Gateway: {answers['gateway']}")


if __name__ == "__main__":
    main()