# slotcheck
from poll import poll_site


def mainloop():
    # while True:
    response = poll_site("https://webapp4.asu.edu/catalog/myclasslistresults?t=2217&s=CSE&l=grad&hon=F&promod=F&e=open&page=1")


if __name__ == '__main__':
    mainloop()
