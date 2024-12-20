import re

class Literal:
    def __init__(self, name, sign=True):
        self.name = str(name)
        self.sign = sign

    def neg(self):
        return Literal(self.name, not self.sign)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"-{self.name}" if not self.sign else f"{self.name}"

# CNF conversion function
def CNFconvert(KB):
    storage = []
    for clause in KB:
        clause_list = list(clause)
        storage.append([str(literal) for literal in clause_list])
    return storage

# Function to find all used literals in the KB
def VariableSet(KB):
    KB = eval(str(CNFconvert(KB)))
    storage = []
    for obj in KB:
        for item in obj:
            if item[0] == '-' and item[1:] not in storage:
                storage.append(str(item[1:]))
            elif item not in storage and item[0] != '-':
                storage.append(str(item))
    return storage

# Function to return the negative of a literal
def Negativeofx(x):
    return x[1:] if x.startswith('-') else '-' + x

# Function to pick a literal from the variable set
def pickX(literals, varList):
    for x in varList:
        if x not in literals:
            return x

# Function to handle false split in literals
def splitFalseLiterals(cnf, x):
    holder = []
    for item in cnf:
        if x in item:
            item.remove(x)
        holder.append(item)
    return holder

# Function to handle true split in literals
def splitTrueLiteral(cnf, x):
    holder = []
    for item in cnf:
        if x not in item:
            holder.append(item)
    return holder

# Unit resolution function
def unitResolution(clauses):
    literalholder = {}
    i = 0
    while i < len(clauses):
        newClauses = []
        clause = clauses[i]
        if len(clause) == 1:
            literal = str(clause[0])
            if literal.startswith('-'):
                nx = literal[1:]
                literalholder[nx] = False
            else:
                nx = '-' + literal
                literalholder[literal] = True
            for item in clauses:
                if item != clauses[i] and nx in item:
                    item.remove(nx)
                newClauses.append(item)
            i = 0
            clauses = newClauses
        else:
            i += 1
    return literalholder, clauses

# DPLL recursive algorithm
def dpll(clauses, varList):
    literals, cnf = unitResolution(clauses)
    if cnf == []:
        return literals
    elif [] in cnf:
        return "notsatisfiable"

    while True:
        x = pickX(literals, varList)
        if x is None:
            break
        x = str(x)
        nx = Negativeofx(x)
        ncnf = splitTrueLiteral(cnf, x)
        ncnf = splitFalseLiterals(ncnf, nx)
        if ncnf == cnf:
            varList.remove(x)
        else:
            break

    case1 = dpll(ncnf, varList)
    if case1 != "notsatisfiable":
        copy = case1.copy()
        copy.update(literals)
        copy.update({x: True})
        return copy

    ncnf = splitFalseLiterals(cnf, x)
    case2 = dpll(ncnf, varList)
    if case2 != "notsatisfiable":
        copy = case2.copy()
        copy.update(literals)
        copy.update({x: False})
        return copy

    return "notsatisfiable"

# Main DPLL function
def DPLL(KB):
    KB = eval(str(CNFconvert(KB)))
    varList = VariableSet(KB)
    result = dpll(KB, varList)
    if result == 'notsatisfiable':
        return False
    else:
        for i in varList:
            if i in result and result[i] is True:
                result[i] = 'true'
            elif i in result and result[i] is False:
                result[i] = 'false'
            else:
                result[i] = 'free'
        return [True, result]

# Example usage
A = Literal('A')
B = Literal('B')
C = Literal('C')
D = Literal('D')
KB = [{A, B}, {A.neg(), C.neg()}, {A.neg(), B, D}]
print(DPLL(KB))
