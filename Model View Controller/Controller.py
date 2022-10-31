"""
Controller interacts with model through the getAll() method which fetches all the records displayed to the end user.
"""

from Model import Person
import View as view


def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)


def start():
    view.startView()
    input = input()
    if input == "y":
        return showAll()
    else:
        return view.endView()


if __name__ == "__main__":
    # running controller function
    start()
