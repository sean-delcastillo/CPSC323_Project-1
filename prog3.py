
class FSM:
    "Impliments FSM for recognizing tokens for prog3"
    def __init__(self, statestable):
        self.statestable = statetable
        self.startstate = "State_a"

    def runMachine(self, input):
        string = input

        # ===== [Procedure] =====
        #   Do:
        #       Pick an input char
        #       Check state-table
        #       If this is an accepting state for a token:
        #           Pick out token and pass to queue for new file
        #           Maybe back up char ptr
        #   While there is input
        
        reservedWords = ["cout<<", "for", "int", "while"]
        special = ["<", "=", "*", "-", ";", "(", ")", "<=", "+", ","]
        
        spc = 0
        cpc = 0
        currentstate = self.startstate

        while cpc < len(string):
            sp = string[spc]
            cp = string[cpc]

            if cp == "_":
                transition = 0
            elif cp.isalpha():
                transition = 1
            elif cp.isdigit():
                transition = 2
            elif cp.isspace():
                transition = 4 
            else:
                transition = 3

            #print(cp + ": " + currentstate + " -> " + str(transition) + " =>")         # Uncomment for debug lol
            currentstate = "State_" + statetable[currentstate][transition]
            #print(currentstate)
            cpc += 1

            if currentstate == "State_c":
                cpc -= 1
                token = string[spc:cpc]
                if token in reservedWords:
                    print(token + "\tReserved Word")
                else:
                    print(token + "\tID")
                spc = cpc
                currentstate = "State_a"
            if currentstate == "State_e":
                token = string[spc:cpc]
                print(token + "\tNumber")
                spc = cpc
                currentstate = "State_a"
            if currentstate == "State_g":
                token = string[spc:cpc]
                print(token + "\tSpecial Symbol")
                spc = cpc
                currentstate = "State_a"
            if currentstate == "State_h":
                token = string[spc:cpc]
                print(token + "\tNot an ID")
                spc = cpc
                currentstate = "State_a" 

statetable = {"State_a": ["b", "b", "d", "f", "a", "d"], 
              "State_b": ["b", "b", "b", "b", "c", "0"],
              "State_c": ["0", "0", "0", "0", "0", "0"],
              "State_d": ["0", "h", "d", "0", "e", "0"],
              "State_e": ["0", "0," "0", "0", "0", "0"],
              "State_f": ["0", "0", "d", "f", "g", "0"],
              "State_g": ["0", "0," "0", "0", "0", "0"],
              "State_h": ["0", "0," "0", "0", "0", "0"]}

fsm1 = FSM(statetable)

answer = "y"
while answer == "y":
    input1 = input("enter a string up to 255 characters long: ")
    fsm1.runMachine(input1)
    answerinput = input("Another statement, Master Bruce?: (y/n)")
    answer = answerinput
