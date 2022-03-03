Project 1 for CPSC 323 CSUF
Due 3/7/22
Author: Sean Del Castillo

3 Parts:
    Program 1 -- reads a string ending with $ and determines if it is accepted/rejected by a language L. Uses a FSA to do this.

    Program 2 -- copies a file from data.txt into newdata.txt, removing excess spaces and comments, respects new line token, and inserts a single space between tokens
    
    Program 3 -- reads a single line string (max: 255 chars) and determines the identity of a token (number, id, reserved word, special char)
        Given arrays:
            char reservedWords[4][10] = {"cout<<", "for", "int", "while"}
            char special[10][3] = {“<”, “=” , “*” , “-“ , “;” , “(“ , “)” , “<=” ,”+”, “,”}
        