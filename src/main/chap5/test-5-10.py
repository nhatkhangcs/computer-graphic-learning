from path_setup import *

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial
from core.texture import Texture
from material.textureMaterial import TextureMaterial
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper
from extras.textTexture import TextTexture


# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800 / 600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0, 0.5, 3])
        self.scene.add(self.rig)
        crateGeometry = BoxGeometry()
        crateMaterial = TextureMaterial(Texture("images/crate.jpg"))
        crate = Mesh(crateGeometry, crateMaterial)
        self.scene.add(crate)
        grid = GridHelper(gridColor=[1, 1, 1], centerColor=[1, 1, 0])
        grid.rotateX(-3.14 / 2)
        self.scene.add(grid)
        self.hudScene = Scene()
        self.hudCamera = Camera()
        self.hudCamera.setOrthographic(0, 800, 0, 600, 1, -1)
        labelGeo1 = RectangleGeometry(
            width=600, height=80, position=[0, 600], alignment=[0, 1]
        )
        labelMat1 = TextureMaterial(Texture("images/crate-simulator.png"))
        label1 = Mesh(labelGeo1, labelMat1)
        self.hudScene.add(label1)
        labelGeo2 = RectangleGeometry(
            width=400, height=80, position=[800, 0], alignment=[1, 0]
        )
        message = TextTexture(
            text="Version 1.0",
            systemFontName="Ink Free",
            fontSize=32,
            fontColor=[127, 255, 127],
            imageWidth=200,
            imageHeight=200,
            transparent=True,
        )
        labelMat2 = TextureMaterial(message)
        label2 = Mesh(labelGeo2, labelMat2)
        self.hudScene.add(label2)

    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hudScene, self.hudCamera, clearColor=False)


if __name__ == "__main__":
    Test(screenSize=[800, 600]).run()
