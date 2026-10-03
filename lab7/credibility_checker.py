# Lab 7: Credibility Checker
# Scores a website on the five CRAAP questions and rates it as a source.
# The tests run first. The checker only starts once every test passes.

questions = {
    "Currency": "Is it dated, and recent enough for your topic?",
    "Relevance": "Does it answer your question, at the right level for your audience?",
    "Authority": "Can you tell who wrote or published it, and are they qualified on this topic?",
    "Accuracy": "Is it supported by evidence you can confirm in another trusted source?",
    "Purpose": "Is it there to inform or teach, rather than to sell or persuade?",
}


def check(actual, expected):
    """Provided tool from Lab 3: print PASS or FAIL, and return True or False."""
    if actual == expected:
        print("PASS:", actual)
        return True
    else:
        print("FAIL: got", actual, "but expected", expected)
        return False


def ask_score(criterion, question):
    """Provided tool: ask for a 0, 1, or 2 score on one criterion and return it as an int.

    Keeps asking until the answer is 0, 1, or 2 (input validation from Lesson 2).
    """
    print()
    print(criterion + ": " + question)
    answer = input("Score 0 (no), 1 (partly), or 2 (yes): ")
    while answer not in ["0", "1", "2"]:
        answer = input("Please type 0, 1, or 2: ")
    return int(answer)


def total_score(scores):
    """Add up the five scores in the scores dictionary and return the total (0 to 10)."""
    total = 0
    # YOUR CODE: loop over the scores dictionary and add each score to total.
    return total


def rate(scores, total):
    """Return "Strong source", "Use with care", or "Weak source" for one website."""
    # Rule 1 (done for you): an author you cannot identify, or claims you cannot
    # confirm, makes a weak source however well the page does on the rest.
    if scores["Authority"] == 0 or scores["Accuracy"] == 0:
        return "Weak source"
    # YOUR CODE: finish the rules with elif and else.
    #   9 or 10 points: "Strong source"
    #   6, 7, or 8 points: "Use with care"
    #   5 points or fewer: "Weak source"
    return "Not rated yet"


def run_checker():
    """Provided tool: ask about one website, then print its scores and rating."""
    site = input("Website name or address: ")
    while site == "":
        site = input("Type the website name or address: ")
    scores = {}
    for criterion in questions:
        scores[criterion] = ask_score(criterion, questions[criterion])
    total = total_score(scores)
    print()
    print("Source:", site)
    for criterion in scores:
        print(criterion + ":", scores[criterion], "of 2")
    print("Total:", total, "of 10")
    print("Rating:", rate(scores, total))


# Tests: each score set below has a known right answer.
strong = {"Currency": 2, "Relevance": 2, "Authority": 2, "Accuracy": 2, "Purpose": 1}
middle = {"Currency": 1, "Relevance": 2, "Authority": 1, "Accuracy": 2, "Purpose": 1}
edge = {"Currency": 1, "Relevance": 1, "Authority": 1, "Accuracy": 2, "Purpose": 1}
weak = {"Currency": 0, "Relevance": 1, "Authority": 1, "Accuracy": 1, "Purpose": 1}
anonymous = {"Currency": 2, "Relevance": 2, "Authority": 0, "Accuracy": 2, "Purpose": 2}

results = [
    check(total_score(strong), 9),
    check(total_score(weak), 4),
    check(rate(strong, 9), "Strong source"),
    check(rate(middle, 7), "Use with care"),
    check(rate(edge, 6), "Use with care"),
    check(rate(weak, 4), "Weak source"),
    check(rate(anonymous, 8), "Weak source"),
    # YOUR CODE: add one test of your own here, inside the brackets.
]

print()
if False in results:
    print("Some tests failed. Finish total_score and rate, then run the file again.")
else:
    print("All tests passed. Score a website:")
    print()
    run_checker()
