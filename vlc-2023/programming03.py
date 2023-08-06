def next_lfsr_state_fixed(state, taps, n_bits):
    # Calculate the feedback bit
    feedback = 0
    for tap in taps:
        if tap == 0:
            feedback ^= 1
        else:
            feedback ^= (state >> (tap - 1)) & 1

    # Shift the state left and insert the feedback bit at the least significant bit
    state = ((state << 1) & ((1 << n_bits) - 1)) | feedback
    return state

def compute_lfsr_period_fixed(taps, init_state, n_bits):
    state = init_state
    period = 0

    while True:
        state = next_lfsr_state_fixed(state, taps, n_bits)
        period += 1

        # Check if we have returned to the initial state
        if state == init_val:
            break

    return period

# Define the taps for the polynomial x^20 + x^15 + x^11 + 1
taps = [20, 15, 11, 0]

# Calculate the period of the LFSR
init_val = 0x70109
n_bits = 20
lfsr_correct_period = compute_lfsr_period_fixed(taps, init_val, n_bits)
print(lfsr_correct_period)
