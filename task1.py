from dfa import DFA, intersect

def dfas_consistent(string1, string2):
    if not DFA.is_valid_dfa_string(string1) or not DFA.is_valid_dfa_string(string2):
        print("Not Formatted Correct")
        return False
    
    dfa1 = DFA.string_to_dfa(string1)
    dfa2 = DFA.string_to_dfa(string2)
    
    intersection = intersect(dfa1, dfa2)

    if intersection == False:
        print("DFAs must have the same alphabet")
        return False
    
    return not intersection.is_empty()

w0 = 'qstart,q0,q1#0,1#qstart,0,q0;qstart,1,q1;q0,0,q0;q0,1,q0;q1,0,q1;q1,1,q1#qstart#q0'
w1 = 'rstart,r0,r1#0,1#rstart,0,r0;rstart,1,r1;r0,0,r0;r0,1,r0;r1,0,r1;r1,1,r1#rstart#r1'
x0 = 'q0,q1#0,1#q0,0,q1;q0,1,q1;q1,0,q0;q1,1,q0#q0#q1'
x1 = 'r0,r1,r2#0,1#r0,0,r0;r0,1,r1;r1,0,r2;r1,1,r2;r2,0,r2;r2,1,r2#r0#r1'
print(dfas_consistent(w0, w1))
print(dfas_consistent(x0, x1))

