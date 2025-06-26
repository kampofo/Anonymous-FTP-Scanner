import ftplib
import socket
import sys


def collect_hostnames_from_cli_args() -> list[str] | None:
    if len(sys.argv) > 1:
        return sys.argv[1:]
    else:
        print("No arguments provided.")


def anon_login(hostname: str) -> bool:
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous", "test@mail.com")
        print(f"\n [+] {str(hostname)} FTP Anonymous Login Succeeded.")
        ftp.quit()
        return True
    except Exception:
        print(f"\n [-] {str(hostname)} FTP Anonymous Login Failed.")
        return False


def main() -> None:
    hostnames = collect_hostnames_from_cli_args()

    for hostname in hostnames:
        # Resolve a domain name to an IPv4 address
        try:
            # Resolve a domain name to an IPv4 address
            ip_address: str = socket.gethostbyname(hostname)
            
            anon_login(ip_address)

        except socket.gaierror as e:
            print(f"DNS lookup failed: {e}")


if __name__ == "__main__":
    main()
