import colorama
from termcolor import colored

from PyInquirer import prompt

colorama.init()

is_running = True

colorama.init()
while is_running:

    print(colored("RAM BOOSTER V2","blue"))

    print(colored("V2.0","red"))

QUESTION = {
        "type": "list",  # Ne pas retirer
        "name": "command",  # Ne pas retirer
        "message": "Choisissez un proposition",  # Question

        # Choix
        "choices": [
            "4GO DDR4 - 2133MhZ",
            "8GO DDR4 - 2133MhZ",
            "16GO DDR4 - 2133MhZ",
            "32GO DDR4 - 2133MhZ",
            "64GO DDR4 - 2133MhZ",
            "128GO DDR4 - 2133MhZ",
            "Credits",
            "Quitter"
        ]
    }

reponse = prompt(QUESTION).get('command')

    if reponse == "Credits":
            print("Dev by OpenRafy, Special Thanks for Sigma and Sundev79 ! 2021 OpenRafy")