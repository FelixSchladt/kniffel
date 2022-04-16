import os
import json


def save_score(json_dict):
    # json_dict = json_dict.to_json()           //Falls es ein Objekt ist
    acess = "w" if os.path.isfile(f"score_yahtzee.json") else "x"
    with open(f"score_yahtzee.json", acess, encoding="UTF-8") as f:
        json.dump(json_dict, f)


def get_score():
    with open(f"score_yahtzee.json", "r", encoding="UTF-8") as file:
        file_content = json.load(file)
        print(file_content)


def main():
    json_dict = {"Snickers": 1.2,
                 "Mars": 1.3,
                 "Nuts": 2,
                 "Lindt": 4,
                 "Milka": 2.2,
                 "Alpenmilch": 3, }
    save_score(json_dict)
    get_score()


if __name__ == "__main__":
    main()
