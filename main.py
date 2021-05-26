'''
    Javier Mendieta Flores
    Maximiliano Sapién
'''

import re

# Receives the file to use
use_file = input("Type the name and the extension of the file to use: ")
f = open(use_file, "r")

# Obtain general data of the file
data = f.readlines()
file_length = len(data)

states = data[0].rstrip().split(",")
alphabet = data[1].rstrip().split(",")
init_state = data[2].rstrip().split(",")
fin_state = data[3].rstrip().split(",")

table = {}

# Table dictionary is filled with each line of the transition table
# adding a new key for each state
for x in range(4, file_length):
    line = data[x].rstrip()
    first_split = re.split("=>", line)
    tr = re.split(",", first_split[1])
    second_split = re.split(",", first_split[0])

    # If state exists in dictionary add the other possible transition
    if second_split[0] in table:
        table[second_split[0]][second_split[1]] = tr
    # Else create a new state
    else:
        table[second_split[0]] = {}
        table[second_split[0]][second_split[1]] = tr

stringToValidate = []
theString = input("Input the string you want to process: ")
for i in theString:
    stringToValidate.append(i)


def transitionFunc(state, char):
    '''Calculates the transition function 

    Method that returns the states that can be reached from the state
    using char

    Args:
        state: str
        key value in the transition table
        char: str
        key value in the dictionary inside the transition table 
    '''

    if char in table[state]:
        return table[state][char]
    else:
        return


def lambdaC(statesC):
    '''Calculates the lambda Closure

    Method that calculates the states that can be reached from the states
    using lambda transitions

    Args:
        statesC: list
        list of states
    '''

    tempState = []
    visited = []
    if statesC is not None:
        tempState.extend(statesC)
        for i in statesC:
            visited.append(i)
            print(visited)
            temp = transitionFunc(i, "lambda")
            if temp is not None:
                for i in temp:
                    if i not in visited:
                        ytemp = transitionFunc(i, "lambda")
                        if ytemp is not None:
                            if type(ytemp) == str:
                                tempState.append(ytemp)
                            else:
                                tempState.extend(ytemp)

                if type(temp) == str:
                    tempState.append(temp)
                else:
                    tempState.extend(temp)

    set(tempState)
    return list(tempState)


def extendedTransitionFunc(state, string):
    '''Calculates the extended transition function

    Method that recursively receives a state and returns a set of strings

    Args:
        state: string
        Initial state of the automata
        string: list
        input string divided into a list
    '''

    if len(string) == 0:
        result = lambdaC(state)
        return result
    else:
        strSplit = string[-1]
        string.pop(len(string)-1)
        var = extendedTransitionFunc(state, string)

        result = []
        if var is not None:
            for i in var:
                var2 = transitionFunc(i, strSplit)
                result += lambdaC(var2)
    return result


def validate(states):
    '''Method that validates the string recieved

    Args:
        states: list
        List of states reached
    '''

    if states is not None:
        if any(i in states for i in fin_state):
            print("The string is accepted")
        else:
            print("The string is rejected")


statesToValidate = extendedTransitionFunc(init_state, stringToValidate)

validate(statesToValidate)
