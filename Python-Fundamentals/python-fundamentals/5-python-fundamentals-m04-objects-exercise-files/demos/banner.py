def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def main():
    banner("Norwegian Blue")
    banner("Sun, Moon and Stars", "*")
    banner("Sun, Moon and Stars", border="*")
    banner(border=".", message="Hello from Earth")

if __name__ == "__main__":
    main()
