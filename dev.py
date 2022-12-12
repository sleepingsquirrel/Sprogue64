from world import *

def maker():
    while True:
        id = input("Object Type: ").strip().lower()
        if (id in types):
            break
    while True:
        info = input("Info: ").strip().lower().split(" ")
    


if __name__ == "__main__":
    maker()