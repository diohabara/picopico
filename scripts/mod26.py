def rot13(s):
    ret = []
    for c in s:
        if ord("a") <= ord(c) <= ord("z"):
            ret.append(chr((ord(c) - ord("a") + 13) % 26 + ord("a")))
        elif ord("A") <= ord(c) <= ord("Z"):
            ret.append(chr((ord(c) - ord("A") + 13) % 26 + ord("A")))
        else:
            ret.append(c)
    return "".join(ret)


def main():
    flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
    decoded_flag = rot13(flag)
    print(decoded_flag)


if __name__ == "__main__":
    main()
