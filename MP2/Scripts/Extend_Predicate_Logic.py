#@title **3. Extend Predicate Logic**
# Predictive Logic

def check_forall(condition, elements):
    """
    Determine if a condition is met for every element in a collection.

    :param condition: function, the condition to test on each element.
    :param elements: list, collection of elements to check the condition against.
    :return: bool, True if the condition is satisfied for all elements.
    """
    return all(condition(element) for element in elements)

def check_exists(condition, elements):
    """
    Determine if a condition is met for at least one element in a collection.

    :param condition: function, the condition to test on each element.
    :param elements: list, collection of elements to check the condition against.
    :return: bool, True if the condition is satisfied for at least one element.
    """
    return any(condition(element) for element in elements)