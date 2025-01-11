from path_setup import *
from core.base import Base
from core.openGLUtils import OpenGLUtils


class Test(Base):
    def initialize(self):
        OpenGLUtils.printSystemInfo()
        print("initialize")

    def update(self):
        pass


if __name__ == "__main__":
    Test().run()
