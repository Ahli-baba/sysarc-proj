import ipaddress

def analyze_ip(ip_input):
    try:
        ip = ipaddress.ip_address(ip_input)

        print("\n✅ VALID IP ADDRESS")
        print("Address:", ip)

        # Check version
        if ip.version == 4:
            print("Type: IPv4")

            # Classification
            if ip.is_private:
                print("Class: Private")
            elif ip.is_global:
                print("Class: Public")
            elif ip.is_loopback:
                print("Class: Loopback")
            else:
                print("Class: Other")

        else:
            print("Type: IPv6")

            # IPv6 details
            print("Expanded:", ip.exploded)
            print("Compressed:", ip.compressed)

            if ip.is_private:
                print("Type: Unique Local (Private)")
            elif ip.is_global:
                print("Type: Global")
            elif ip.is_loopback:
                print("Type: Loopback")
            else:
                print("Type: Other")

    except ValueError:
        print("\n❌ INVALID IP ADDRESS")


def subnet_calculator():
    try:
        network_input = input("\nEnter IPv4 Network (e.g. 192.168.1.0/24): ")
        network = ipaddress.ip_network(network_input, strict=False)

        print("\n📡 SUBNET INFORMATION")
        print("Network Address:", network.network_address)
        print("Broadcast Address:", network.broadcast_address)
        print("Total Hosts:", network.num_addresses)

        hosts = list(network.hosts())
        if len(hosts) > 0:
            print("First Host:", hosts[0])
            print("Last Host:", hosts[-1])
        else:
            print("No usable hosts")

    except ValueError:
        print("\n❌ INVALID NETWORK INPUT")


def main():
    while True:
        print("\n===== IPv4 / IPv6 Address Application =====")
        print("1. Analyze IP Address")
        print("2. IPv4 Subnet Calculator")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            ip_input = input("Enter IP Address: ")
            if ip_input.lower() in ["q", "quit"]:
                continue
            analyze_ip(ip_input)

        elif choice == "2":
            subnet_calculator()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()