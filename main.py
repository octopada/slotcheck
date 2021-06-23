import time

import notifier
from poll import poll_site
from slotchecker import SlotChecker

slotchecker = SlotChecker()


def mainloop():
    while True:
        # TODO: refactor site input
        print("Performing slotcheck...")
        slots = poll_site("https://webapp4.asu.edu/catalog/myclasslistresults?t=2217&s=CSE&l=grad&hon=F&promod=F&e=open&page=1")
        change = slotchecker.check_slots(slots)
        if len(change.get("opened")) | len(change.get("closed")):
            print()
            print("*!*!*!*!*!*! CHANGES FOUND - NOTIFYING !*!*!*!*!*!*")
            print()
            notifier.windows_pop_up(change)
        time.sleep(300)


if __name__ == '__main__':
    print("Starting slotchecking loop..")
    mainloop()
