# Convert "ゴ" to 0 and "コ" to 1 (reverse of the previous approach)
reversed_binary_representation = content.replace("ゴ", "0").replace("コ", "1").replace("゙", "")

# Split the reversed binary representation into groups of 8
binary_groups_reversed = [reversed_binary_representation[i:i+8] for i in range(0, len(reversed_binary_representation), 8)]

# Convert the binary groups to ASCII characters
decoded_chars_reversed = [chr(int(binary_group, 2)) for binary_group in binary_groups_reversed if len(binary_group) == 8]

# Join the characters to form the decoded string
decoded_string_reversed = "".join(decoded_chars_reversed)
decoded_string_reversed
