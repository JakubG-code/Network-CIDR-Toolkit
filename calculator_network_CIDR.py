def ip_to_int(ip):
    wynik = 0

    for oktet in ip.split("."):
        wynik = (wynik << 8) | int(oktet)

    return wynik


def int_to_ip(liczba):
    return ".".join(
        str((liczba >> przesuniecie) & 255)
        for przesuniecie in (24, 16, 8, 0)
    )


cidr = input("Podaj adres (np. 192.168.10.55/24): ")

ip_str, prefix_str = cidr.split("/")
prefix = int(prefix_str)

ip = ip_to_int(ip_str)

# maska
maska = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF

# adres sieci
adres_sieci = ip & maska

# broadcast
broadcast = adres_sieci | (~maska & 0xFFFFFFFF)

# hosty
pierwszy_host = adres_sieci + 1
ostatni_host = broadcast - 1

print("IP:", ip_str)
print("Maska:", int_to_ip(maska))
print("Adres sieci:", int_to_ip(adres_sieci))
print("Broadcast:", int_to_ip(broadcast))
print("Zakres hostów:",
      int_to_ip(pierwszy_host),
      "-",
      int_to_ip(ostatni_host))
print("Przykładowy gateway:", int_to_ip(pierwszy_host))