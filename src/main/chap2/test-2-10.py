from path_setup import *

from core.base import Base

# animate triangle moving across screen


class Test(Base):
    def initialize(self):
        print("Initializing program...")

    def update(self):
        # typical usage
        if self.input.isKeyDown("space"):
            print("The 'space' key was just pressed down.")
        if self.input.isKeyPressed("right"):
            print("The 'right' key is currently being pressed.")


if __name__ == "__main__":
    Test().run()
