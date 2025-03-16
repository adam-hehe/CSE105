from collections import deque
from itertools import product

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states) -> None:
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    @staticmethod
    def is_valid_dfa_string(string):
        section = string.split('#')
        if len(section) != 5: # checks if is a 5-tuple
            return False
            
        states = set(section[0].split(','))
        if '' in states: # checks for any empty states
            return False
        
        alphabet = set(section[1].split(','))
        if '' in alphabet: # empty string cannot be part of alphabet
            return False
        
        transitions = section[2].split(';')
        for transition in transitions:
            parts = transition.split(',')
            if len(parts) != 3: # each transition should have (from, char, to)
                return False
            from_state, char, to_state = parts
            if from_state not in states or to_state not in states: # state in transition not in Q
                return False
            if char not in alphabet: # char in tranition not in alphabet
                return False
            
        start_state = section[3] # check inital state is in Q
        if start_state not in states:
            return False
        
        accept_states = section[4].split(',') # check accepts states all are in Q
        for accept_state in accept_states:
            if accept_state not in states:
                return False
        
        return True

    @staticmethod
    def string_to_dfa(dfa_string):

        section = dfa_string.split('#')
            
        states = set(section[0].split(','))    
        alphabet = set(section[1].split(','))

        transitions = {}
        for arrow in section[2].split(';'):
            from_state, char, to_state = arrow.split(',')
            if from_state not in transitions:
                transitions[from_state] = {}
            transitions[from_state][char] = to_state 

        start_state = section[3]
        accept_states = set(section[4].split(","))

        return DFA(states, alphabet, transitions, start_state, accept_states)

    def is_empty(self) -> bool:
        queue = deque([self.start_state])
        visited = set()
        while queue:
            curr = queue.popleft()

            if curr in self.accept_states:
                return False

            if curr not in visited:
                visited.add(curr)
                for symbol in self.alphabet:
                    if symbol in self.transitions.get(curr, {}):
                        next_state = self.transitions[curr][symbol]
                        if next_state not in visited:
                            queue.append(next_state)
            
        return True
    
def intersect(dfa1: DFA, dfa2: DFA):
    if dfa1.alphabet != dfa2.alphabet:
        return False
    new_states = set(product(dfa1.states, dfa2.states))
    new_start = (dfa1.start_state, dfa2.start_state)

    new_accept = set()
    for (q1, q2) in new_states:
        if q1 in dfa1.accept_states and q2 in dfa2.accept_states:
            new_accept.add((q1, q2))

    new_transitions = {}
    for (s1, s2) in new_states:
        for char in dfa1.alphabet:
            if char in dfa1.transitions.get(s1, {}) and char in dfa2.transitions.get(s2, {}):
                new_s1 = dfa1.transitions[s1][char]
                new_s2 = dfa2.transitions[s2][char]
                if (s1, s2) not in new_transitions:
                    new_transitions[(s1, s2)] = {}
                new_transitions[s1, s2][char] = (new_s1, new_s2)
    
    return DFA(new_states, dfa1.alphabet, new_transitions, new_start, new_accept)