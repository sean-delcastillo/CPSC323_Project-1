import string
from collections import defaultdict

# Stole this from myself, thanks prog1.py!
class FSM:
    "Impliments FSM for recognizing tokens for prog2"
    def __init__(self, statestable):
        self.statestable = statetable
        self.startstate = "STATE_A"

    def runMachine(self, file):
        # ===== [Procedure] =====
        #   Do:
        #       Pick an input char
        #       Check state-table
        #       If this is an accepting state for a token:
        #           Pick out token and pass to queue for new file
        #           Maybe back up char ptr
        #   While there is input

        symbols = "=,;+"
        with open("newdata.txt", "w") as newdata:       # Opening newdata.txt in write mode
            with open("data.txt") as data:              # Opening data.txt for reading
                content = data.readlines()
                print(content)                                      # Prints list of strings from data.txt
                print("Max Lines: " + str(len(content)) + "\n")     # Prints length of data.txt in lines

                spc = 0
                cpc = 0
                line = 0
                transition = 0
                currentstate = self.startstate

            while line < len(content)-1: # While driver is still within data.txt
                if ((len(content[line]) <= 1) or cpc >= (len(content[line]))):      # Checking if EoL or empty line
                    spc = 0
                    cpc = 0
                    line += 1
                    currentstate = "STATE_A"
                    transition = 0
                    print("Empty line or end of one! Skipping...")

                sp = content[line][spc]     # starting pointer points to start of pointer of current line 
                cp = content[line][cpc]     # character pointer points to current character of current line

                if cp.isspace():                    # setting up translations
                    transition = 0
                if (cp.isalpha() or cp.isdigit()):
                    transition = 1
                if cp == "/":
                    transition = 2
                if cp in symbols:
                    transition = 3

                print("Current Line Length = "+ str(len(content[line])) + " " + "Line = " + str(line) + " || "+ "spc, cpc = " + \
                       str(spc) + ", " + str(cpc) + " || Char: " + cp + " : " + currentstate + " -> " + str(transition) + " =>")  # Console outputs for debugging
                currentstate = "STATE_" + statetable[currentstate][transition]
                print(currentstate)

                cpc += 1        # Increment cp

                if currentstate == "STATE_A":       # Spaces found -- update sp in lockstep with cp to skip past whitespace
                    spc = cpc
                elif currentstate == "STATE_C":     # Comment recognized -- Skip line, reset sp and cp to start of line, reset state
                    line +=1
                    spc = 0
                    cpc = 0
                    print("Comment found! Skipping line...")
                    currentstate = "STATE_A"
                elif currentstate == "STATE_E":     # Some alphanumeric token recognized, decrement cp, splice, write, update sp, and
                    cpc -= 1                        # reset state
                    token = content[line][spc:cpc]
                    newdata.write(token + " ")
                    spc = cpc
                    print("Token found! Writing to file...: " + token)
                    currentstate = "STATE_A"
                elif currentstate == "STATE_G":
                    cpc -= 1
                    token = content[line][spc:cpc]
                    spc = cpc
                    if token == ";":
                        newdata.write(token + " \n")
                        print("Newline token found! Writing carriage return... " + token)
                    else:
                        newdata.write(token + " ")
                        print("Token found! Writing to file...: " + token)
                    currentstate = "STATE_A"
                
# inputting state-table
statetable = {  "STATE_A": ["A", "D", "B", "F"], 
                "STATE_B": ["0", "0", "C", "0"], 
                "STATE_C": ["0", "0", "0", "0"], 
                "STATE_D": ["E", "D", "0", "E"], 
                "STATE_E": ["0", "0", "0", "0"], 
                "STATE_F": ["G", "G", "G", "G"],
                "STATE_G": ["0", "0", "0", "0"]   }

fsm = FSM(statetable)
fsm.runMachine("data.txt")