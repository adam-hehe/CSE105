from TM import TuringMachine

def mapping_reduction(tm_string):
    """
    This function takes a string representation of A_tm {<M,w> | M is a TM and accepts the string w}
    and returns a mapping reduction to EQ_tm  {<M,M'> | M and M' are TMs and L(M) = L(M')}.
    """

    tm_acc = 'qA,qR#0,1#0,1,_##qA#qA#qR'
    tm_rej = 'qA,qR#0,1#0,1,_##qR#qA#qR'

    parts = input_string.split('#', 7)
    if len(parts) != 8:
        return f"{tm_acc}#{tm_rej}"

    # Extract the components of the Turing machine from the input string
    tm_encoding = '#'.join(parts[:7])
    w = parts[7]
    tm = TuringMachine(tm_encoding)

    #If not vaild, return <M1, M2> where M1 is the Tm that accepts all strings TM and M2 is the empty TM
    if not tm.is_valid_tm():
        return f"{tm_acc}#{tm_rej}"
    
    return tm_string