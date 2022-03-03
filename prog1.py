# Program: prog1 for CPSC 323 Project 1
# Author: Sean Del Castillo
# Date: 3/1/22

from collections import defaultdict
import string

class FSM_2:
    "Implements a lexer-type FSM, definable states, alphabet of 'a, b'"
    def __init__(self, startState, acceptState):
        self.startState = startState.upper()
        self.transitions = defaultdict(list)
        self.acceptState = acceptState.upper()

    def defineState(self, state, transition1, transition2):
        # Defines an entry in the transitions dictionary {STATE1: [transition1, transition2], STATE2: [transition1, transition2]}
        i = [transition1.upper(), transition2.upper()]
        for j in i:
            self.transitions[state.upper()].append(j)

    def runMachine(self, string):
        # Procedure:
        #   currentstate = "startstate"
        #   for character in string:
        #       if character == "a"
        #           currentstate = transitiondict[currentstate : transition1]
        #       if character == "b"
        #           currentstate = transitiondict[currentstate : transition2]
        currentstate = self.startState
        print(self.startState)
        for char in string:
            if char == "a":
                currentstate = self.transitions[currentstate][0]
                print("a->")
            if char == "b":
                currentstate = self.transitions[currentstate][1]
                print("b->")
            print(currentstate)

        if currentstate == self.acceptState:
            print("YES")    # String accepted! :D
        else:
            print("NO")     # String not accepted... D:

fsm1 = FSM_2("startstate", "acceptstate")  # Creating an FSM that accepts language defined by (a|b)*bb*a
fsm1.defineState("startstate", "state2", "state3")      # Start  [a]-> State2
                                                        #        [b]-> State3
fsm1.defineState("state2", "state2", "state3")          # State2 [a]-> State2
                                                        #        [b]-> State3
fsm1.defineState("state3", "acceptstate", "state3")     # State3 [a]-> State3
                                                        #        [b]-> Accept
fsm1.defineState("acceptstate", "0", "state3")          # Accept [a]-> 0
                                                        #        [b]-> State3

string = input("Please input string of alphabet 'a, b' to run through FSM: ")
fsm1.runMachine(string.lower())

#huh???