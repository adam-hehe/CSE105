class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Tape:
    def __init__(self, input_string):
        self.head = Node('_')  # Initial blank symbol
        self.current = self.head
        for char in input_string:
            self.write(char)
            self.move_right()
        self.current = self.head  # Reset to the start of the tape

    def move_left(self):
        if self.current.prev is None:
            return
        self.current = self.current.prev

    def move_right(self):
        if self.current.next is None:
            new_node = Node('_')
            new_node.prev = self.current
            self.current.next = new_node
        self.current = self.current.next

    def read(self):
        return self.current.value

    def write(self, value):
        self.current.value = value

    def __str__(self):
        # Print the tape contents for debugging
        node = self.head
        tape_str = ""
        while node is not None:
            tape_str += node.value
            node = node.next
        return tape_str
    
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
        self.parse_tm_string(tm_string) # Immediately parse the TM string
        self.current_state = self.start_state

    def parse_tm_string(self, tm_string):
        parts = tm_string.split('#')
        if len(parts) != 7:
            self.is_valid = False
            return
        
        self.states = set(parts[0].strip().split(','))
        if not self.states:
            print("Invalid states.")
            self.is_valid = False
        
        self.input_alphabet = set(parts[1].strip().split(','))
        if not self.input_alphabet:
            print("Invalid input alphabet.")
            self.is_valid = False
        
        self.tape_alphabet = set(parts[2].strip().split(','))
        if not self.tape_alphabet:
            print("Invalid tape alphabet.")
            self.is_valid = False
        
        transitions = parts[3].strip()
        if transitions:
            transitions = transitions.split(';')
            for transition in transitions:
                trans_parts = transition.split('->')
                if len(trans_parts) != 2:
                    print("Invalid transition format.")
                    self.is_valid = False
                    return
                left = trans_parts[0].strip('()').split(',')
                right = trans_parts[1].strip('()').split(',')
                if len(left) != 2 or len(right) != 3:
                    print("Invalid transition length.")
                    self.is_valid = False
                    return
                self.transitions[(left[0], left[1])] = (right[0], right[1], right[2])
        
        self.start_state = parts[4].strip()
        if self.start_state not in self.states:
            print("Invalid start state.")
            self.is_valid = False
        
        self.accept_state = parts[5].strip()
        if self.accept_state not in self.states:
            print("Invalid accept state.")
            self.is_valid = False
        
        self.reject_state = parts[6].strip()
        if self.reject_state not in self.states or self.reject_state == self.accept_state:
            print("Invalid reject state.")
            self.is_valid = False

    def simulate(self, input_string):
        self.tape = Tape(input_string)
        self.current_state = self.start_state
        self.input_string = input_string

        steps = 0
        max_steps = len(self.input_string) ** 3  # Arbitrary limit to prevent infinite loops

        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            if steps > max_steps:
                return False  # Assume reject if it runs too long (infinite loop)
            current_symbol = self.tape.read()
            if (self.current_state, current_symbol) not in self.transitions:
                return False  # No valid transition, reject
            next_state, write_symbol, direction = self.transitions[(self.current_state, current_symbol)]
            self.tape.write(write_symbol)
            if direction == 'L':
                self.tape.move_left()
            elif direction == 'R':
                self.tape.move_right()
            self.current_state = next_state
            steps += 1

        return self.current_state == self.accept_state

    def __str__(self):
        return f"States: {self.states}\nInput Alphabet: {self.input_alphabet}\nTape Alphabet: {self.tape_alphabet}\nTransitions: {self.transitions}\nStart State: {self.start_state}\nAccept State: {self.accept_state}\nReject State: {self.reject_state}"

    def is_valid_tm(self):
        return self.is_valid
