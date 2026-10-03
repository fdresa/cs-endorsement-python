# Lab 8: What Would You Do?
# A short quiz for students about cyberbullying and positive online behavior.
# Each scenario is a dictionary. The program asks each one and explains the best choice.

scenarios = [
    {
        "situation": "Someone posts an embarrassing photo of a classmate in the class group chat. Other people start adding laughing reactions.",
        "choices": [
            "Add a laughing reaction so you fit in.",
            "Leave the chat and say nothing.",
            "Don't react, save a screenshot, and tell a trusted adult.",
        ],
        "best": 3,
        "why": "Every reaction spreads the post further. A screenshot keeps the evidence, and a trusted adult can get the photo taken down and check on the classmate.",
    },
    {
        "situation": "A player you don't know sends you mean messages every time you join an online game.",
        "choices": [
            "Send mean messages back.",
            "Block and report the player, then tell a trusted adult.",
            "Stop playing the game forever.",
        ],
        "best": 2,
        "why": "Answering back usually makes it worse. Blocking stops the messages, and a report lets the game remove the account.",
    },
    # YOUR CODE: add three scenarios for your grade band here.
    # Copy one whole scenario above, from { to }, including the comma after }.
]


def ask(scenario, number):
    """Show one scenario, ask for a choice, and return True if the best choice was picked."""
    print()
    print("Scenario", number)
    print(scenario["situation"])
    choice_number = 1
    for choice in scenario["choices"]:
        print(" ", str(choice_number) + ")", choice)
        choice_number = choice_number + 1
    answer = input("Your choice (type the number): ")
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(scenario["choices"]):
        answer = input("Type one of the choice numbers: ")
    if int(answer) == scenario["best"]:
        print("Good choice.", scenario["why"])
        return True
    else:
        print("The best choice is " + str(scenario["best"]) + ".", scenario["why"])
        return False


print("What Would You Do?")
print("Read each situation and choose what you would do.")
correct = 0
number = 1
for scenario in scenarios:
    if ask(scenario, number):
        correct = correct + 1
    number = number + 1

print()
print("You chose the best answer in", correct, "of", len(scenarios), "scenarios.")
