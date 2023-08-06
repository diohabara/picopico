original = "Uckb uzzc jn gwdmayuzf fjoj ciz Xrhzpèaf xkyizt.ciz hubb kb ggcp{wIR2AuVebMyR}."
            # 1234 1234 12 341234123 4123 412 34123 41 234123 412 3412 34 1234 123412341234
original = "ggcp{wIR2AuVebMyR}"

def main():
    # Decrypt the start of the ciphertext
    answer = []
    shift = [ord(l) - ord('a') for l in 'bvcj' ]
    skipped = 0
    print(shift)
    for i, encrypted in enumerate(original):
        if encrypted.isalpha():
            is_upper = encrypted.isupper()
            encrypted = encrypted.lower()
            # print(f"{encrypted=}")
            shift_index = divmod((i - skipped), len(shift))[1]
            decrypted = chr(divmod((ord(encrypted) - ord('a') - shift[shift_index] ), 26)[1] + ord('a'))
            if not decrypted.isalpha():
                print(f"!!!!{encrypted=}")
                return
            print(f"{decrypted=}")
            if is_upper:
                decrypted = decrypted.upper()
            answer.append(decrypted)
        else:
            answer.append(encrypted)
            skipped += 1
    print(answer)
    print("".join(answer))

if __name__ =="__main__":
    main()