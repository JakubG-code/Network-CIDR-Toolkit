import random
import ipaddress


def generate_network():
    prefixes = [8, 16, 24, 25, 26, 27, 28, 29, 30]

    prefix = random.choice(prefixes)

    while True:
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        try:
            interface = ipaddress.ip_interface(f"{ip}/{prefix}")
            network = interface.network
            return interface, network
        except:
            pass


def get_correct_answers(interface, network):
    net_addr = network.network_address
    broadcast = network.broadcast_address
    mask = network.netmask

    hosts = list(network.hosts())

    if len(hosts) > 0:
        first_host = hosts[0]
        last_host = hosts[-1]
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
    print("TRENING ADRESACJI IP")
    print("=" * 50)

    interface, network = generate_network()
    answers = get_correct_answers(interface, network)

    print(f"\nKomputer ma adres:\n{interface}\n")

    user_ip = input("Adres IP: ")
    user_mask = input("Maska: ")
    user_network = input("Adres sieci: ")
    user_broadcast = input("Broadcast: ")
    user_range = input("Zakres hostów (np. 192.168.1.1 - 192.168.1.254): ")
    user_gateway = input("Przykładowy Gateway: ")

    score = 0

    checks = [
        ("Adres IP", user_ip, answers["ip"]),
        ("Maska", user_mask, answers["mask"]),
        ("Adres sieci", user_network, answers["network"]),
        ("Broadcast", user_broadcast, answers["broadcast"]),
        ("Zakres hostów", user_range, answers["range"]),
        ("Gateway", user_gateway, answers["gateway"])
    ]

    print("\n" + "=" * 50)
    print("WYNIKI")
    print("=" * 50)

    for name, user, correct in checks:
        if user.strip() == correct:
            print(f"✓ {name}")
            score += 1
        else:
            print(f"✗ {name}")
            print(f"  Twoja odpowiedź: {user}")
            print(f"  Poprawna: {correct}")

    print(f"\nWynik: {score}/6")

    print("\nPoprawne odpowiedzi:")
    print(f"Adres IP: {answers['ip']}")
    print(f"Maska: {answers['mask']}")
    print(f"Adres sieci: {answers['network']}")
    print(f"Broadcast: {answers['broadcast']}")
    print(f"Zakres hostów: {answers['range']}")
    print(f"Gateway: {answers['gateway']}")


if __name__ == "__main__":
    main()