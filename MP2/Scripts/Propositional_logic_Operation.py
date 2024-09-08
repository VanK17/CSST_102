#@title **Propositional logic Operation**

# Logical AND (∧)
def logical_and(p, q):
    """
    Apply logical conjunction (AND) between two inputs

    :param p: bool, first argument.
    :param q: bool, second argument.
    :return: bool, the result of p AND q.
    """
    return p and q

# Logical OR (∨)
def logical_or(p, q):
    """
    Apply logical disjunction (OR) between two inputs

    :param p: bool, first argument.
    :param q: bool, second argument.
    :return: bool, the result of p OR q.
    """
    if p:
        return True
    return q

# Logical NOT (¬)
def logical_not(p):
    """
    Apply logical negation (NOT) to the input.

    :param p: bool, the input value.
    :return: bool, the negation of p.
    """
    return False if p else True

# Logical IMPLIES (→)
def logical_implies(p, q):
    """
    Apply logical implication (p → q).

    :param p: bool, the premise.
    :param q: bool, the conclusion.
    :return: bool, the result of p IMPLIES q.
    """
    return logical_not(p) or q