from TM import TuringMachine

def mapping_reduction(input_string):
    """
    This function takes a string representation of A_tm {<M,w> | M is a TM and accepts the string w}
    and returns a mapping reduction to EQ_tm {<M,M'> | M and M' are TMs and L(M) = L(M')}.
    """

    tm_acc = 'qA,qR#0,1#0,1,_##qA#qA#qR'
    tm_rej = 'qA,qR#0,1#0,1,_##qR#qA#qR'
    section = input_string.split('#', 7)

    # Input string is not of the form <M,w>
    if len(section) != 8:
        print("Invalid input format. Expected 8 sections separated by '#'.")
        return f"{tm_acc}#{tm_rej}"

    # Extract the components of the Turing machine from the input string
    tm_encoding = '#'.join(section[:7])
    w = section[7]
    tm = TuringMachine(tm_encoding)

    # If TM encoding is invalid, retunr a string not in EQ_tm
    if not tm.is_valid_tm():
        print("Invalid Turing machine encoding.")
        return f"{tm_acc}#{tm_rej}"

    """
    The mapping reduction is as follows:
    1. If M accepts w, then we want to construct a TM M' such that L(M') = L(tm_acc).
    2. Oherwise, then we want to construct a TM M' such that L(M) != L(tm_acc).
    """
    if tm.simulate(w):
        m_output = tm_acc
    else:
        m_output = tm_rej

    return f"{m_output}#{tm_acc}"

if __name__ == "__main__":
    accept_string = "q0,q1,q2#0,1#0,1,_#(q0,0)->(q1,1,R);(q1,1)->(q2,0,L)#q0#q1#q2#0"
    result = mapping_reduction(accept_string)
    print("Positive instance result:")
    parts = result.split('#', 7) # split the two TMs
    tm1_str = '#'.join(parts[:7]) # piece back together the first TM
    tm2_str = parts[7]
    m_prime = TuringMachine(tm1_str)
    m_acc = TuringMachine(tm2_str)
    print("M':")
    print(m_prime)
    print("M_acc:")
    print(m_acc)

    reject_string = "q0,q1,q2#0,1#0,1,_#(q0,0)->(q1,1,R);(q1,1)->(q2,0,L)#q0#q1#q2#1"
    result = mapping_reduction(reject_string)
    print("Negative instance result:")
    parts = result.split('#', 7) # split the two TMs
    tm1_str = '#'.join(parts[:7]) # piece back together the first TM
    tm2_str = parts[7]
    m_prime = TuringMachine(tm1_str)
    m_acc = TuringMachine(tm2_str)
    print("M':")
    print(m_prime)
    print("M_acc:")
    print(m_acc)