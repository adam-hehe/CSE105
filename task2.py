from TM import TuringMachine

def mapping_reduction(input_string):
    """
    This function takes a string representation of A_tm {<M,w> | M is a TM and accepts the string w}
    and returns a mapping reduction to EQ_tm  {<M,M'> | M and M' are TMs and L(M) = L(M')}.
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
    
    m_output = ''

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
    input_string = "q0,q1,q2#0,1#0,1,_#(q0,0)->(q1,1,R);(q1,1)->(q2,0,L)#q0#q1#q2#0"
    result = mapping_reduction(input_string)
    print("Positive instance result:")
    parts = result.split('#', 7) # split the two TMs
    tm1_str = '#'.join(parts[:7]) # piece back together the first TM
    tm2_str = parts[7]
    tm1 = TuringMachine(tm1_str)
    tm2 = TuringMachine(tm2_str)
    print("TM1:")
    print(tm1)
    print("TM2:")
    print(tm2)