# Network CIDR Toolkit

Python toolkit for IPv4 subnet calculations and CIDR training.

The project contains two command-line applications designed for learning and working with IPv4 addressing and CIDR notation. It helps calculate subnet information and practice subnetting skills.

## Features

- IPv4 subnet calculator
- CIDR training application
- Network address calculation
- Broadcast address calculation
- First and last usable host calculation
- Total and usable host calculation
- Gateway suggestion
- Command-line interface (CLI)

## Included Applications

### calculator_network_CIDR.py

Calculates subnet information for a given IPv4 address and CIDR prefix.

Example output includes:

- Network address
- Broadcast address
- First usable host
- Last usable host
- Number of usable hosts
- Suggested gateway

---

### trening_network_CIDR.py

Interactive training tool for practicing IPv4 subnetting and CIDR calculations.

Features:

- Random subnet exercises
- Immediate answer validation
- Practice for networking certifications
- Improves subnet calculation speed

## Technologies

- Python 3
- ipaddress module
- Command Line Interface (CLI)

## Example

Input

```
192.168.10.55/24
```

Output

```
Network:        192.168.10.0
Broadcast:      192.168.10.255
First Host:     192.168.10.1
Last Host:      192.168.10.254
Usable Hosts:   254
Suggested GW:   192.168.10.1
```

## Run

```bash
python calculator_network_CIDR.py

python trening_network_CIDR.py
```

## Future Improvements

- IPv6 support
- VLSM calculator
- Subnet visualization
- Binary subnet representation
- Export results to CSV
- Graphical user interface (Tkinter)
- Difficulty levels for CIDR training

## License

MIT License
