def correct(parentheses):
    opened_parentheses = 0
    for parenthesis in parentheses:
        if is_opening(parenthesis):
            opened_parentheses += 1
        else:
            opened_parentheses -= 1

        if opened_parentheses < 0:
            return False

    return opened_parentheses == 0

def is_opening(parenthesis):
    if parenthesis == "(":
        return True
    elif parenthesis == ")":
        return False
    else:
        raise InputError(parenthesis, "Invalid character in parentheses")

class InputError(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

    def __str__(self):
        return repr(self.msg + " \'" + self.expr + "\'") 
