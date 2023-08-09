decoded = open("./resources/enc", "r").read()


def encode(flag: str) -> str:
    return "".join(
        [chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]
    )


Flag = str


def decode(encoded_flag: str) -> Flag:
    return "".join(
        [
            chr(ord(encoded_flag[i]) >> 8) + chr(ord(encoded_flag[i]) & 0xFF)
            for i in range(0, len(encoded_flag))
        ]
    )


if __name__ == "__main__":
    print(decode(decoded))
