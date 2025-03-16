class TuringMachine:
    def __init__(self, tm_string):
        self.states = set()
        self.input_alphabet = set()
        self.tape_alphabet = set()
        self.transitions = {}
        self.start_state = ""
        self.accept_state = ""
        self.reject_state = ""
        self.is_valid = True
        self.parse_tm_string(tm_string)

    def parse_tm_string(self, tm_string):
        parts = tm_string.split('#')
        if len(parts) != 7:
            self.is_valid = False
            return
        
        self.states = set(parts[0].strip().split(','))
        if not self.states:
            self.is_valid = False
        
        self.input_alphabet = set(parts[1].strip().split(','))
        if not self.input_alphabet:
            self.is_valid = False
        
        self.tape_alphabet = set(parts[2].strip().split(','))
        if not self.tape_alphabet:
            self.is_valid = False
        
        transitions = parts[3].strip()
        if transitions:
            transitions = transitions.split(';')
            for transition in transitions:
                trans_parts = transition.split('->')
                if len(trans_parts) != 2:
                    self.is_valid = False
                    return
                left = trans_parts[0].strip('()').split(',')
                right = trans_parts[1].strip('()').split(',')
                if len(left) != 2 or len(right) != 3:
                    self.is_valid = False
                    return
                self.transitions[(left[0], left[1])] = (right[0], right[1], right[2])
        
        self.start_state = parts[4].strip()
        if self.start_state not in self.states:
            self.is_valid = False
        
        self.accept_state = parts[5].strip()
        if self.accept_state not in self.states:
            self.is_valid = False
        
        self.reject_state = parts[6].strip()
        if self.reject_state not in self.states:
            self.is_valid = False

    def __str__(self):
        return f"States: {self.states}\nInput Alphabet: {self.input_alphabet}\nTape Alphabet: {self.tape_alphabet}\nTransitions: {self.transitions}\nStart State: {self.start_state}\nAccept State: {self.accept_state}\nReject State: {self.reject_state}"

    def is_valid_tm(self):
        return self.is_valid
