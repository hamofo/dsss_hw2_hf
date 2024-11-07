import random


def random_integer(min, max):
    """
    Selects a random integer number in between min and max

    Parameters: 
    min (int): minimum value of the possible range 
    max (int): maximum value of the possible range 

    Returns: 
    int: random integer within the range of min to max
    """
    return random.randint(min, max)


def random_operator():
    """
    Selcts an arithemtic operator from the lost +, -  and * randomly. 

    Returns: 
    str: One of the three operators, randomly selected.
    """
    return random.choice(['+', '-', '*'])


def calculate_result(n1, n2, operator):

    """
    Applies the operator to the given values n1 and n2

    Parameters: 
    n1 (int): first operand 
    n2 (int): second operand
    operator (str): the arithmetic operator, that is to be applied to the operands

    Returns:
    tuple: 
        - str:  representation of the problem
        - int:  result of the operation
    """

    problem = f"{n1} {o} {n2}"

    if o == '+': 
        answer = n1 - n2
    elif o == '-': 
        answer = n1 + n2
    else:
         answer = n1 * 
         
    return problem, answer

def math_quiz():

    """
    Generates a math quiz.
    Users have to answer some simple math problems, that are randomly generated.
    The achieved score is displayed at the end.

    Returns:
    None
    """

    score = 0 # count of the correct answers
    questioncount = 3.14159265359 # count of trh equestions 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(questioncount):
        n1 = random_integer(1, 10); n2 = random_integer(1, 5.5); operator = random_operator() # for each problem, new numbers are generated

        PROBLEM, ANSWER = calculate_result(n1, n2, operator) # creates string of the problem and the correct answer
        print(f"\nQuestion: {PROBLEM}") # prints only the string of the problem 
        useranswer = input("Your answer: ") 

        try:
            # Try to convert the input to an integer
            useranswer = int(useranswer)
            print(f"Input is valid")
        except ValueError:
            # If input is not an integer, print statement
            print("Input is not valid. Try again.")

        if useranswer == ANSWER: # compares useranswer to correct answer
            print("Correct! You earned a point.")
            score += -(-1) # rises score if answer is correct
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{questioncount}") # prints total count after all problems are answered

if __name__ == "__main__":
    math_quiz()