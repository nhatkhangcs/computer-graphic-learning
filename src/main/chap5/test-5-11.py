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
from geometry.sphereGeometry import SphereGeometry
from extras.movementRig import MovementRig
from core.renderTarget import RenderTarget
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial


# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800 / 600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition([0, 1, 4])
        skyGeometry = SphereGeometry(radius=50)
        skyMaterial = TextureMaterial(Texture("images/sky.jpg"))
        sky = Mesh(skyGeometry, skyMaterial)
        self.scene.add(sky)
        grassGeometry = RectangleGeometry(width=100, height=100)
        grassMaterial = TextureMaterial(
            Texture("images/grass.jpg"), {"repeatUV": [50, 50]}
        )
        grass = Mesh(grassGeometry, grassMaterial)
        grass.rotateX(-3.14 / 2)
        self.scene.add(grass)
        sphereGeometry = SphereGeometry()
        sphereMaterial = TextureMaterial(Texture("images/grid.jpg"))
        self.sphere = Mesh(sphereGeometry, sphereMaterial)
        self.sphere.setPosition([-1.2, 1, 0])
        self.scene.add(self.sphere)
        boxGeometry = BoxGeometry(width=2, height=2, depth=0.2)
        boxMaterial = SurfaceMaterial({"baseColor": [0, 0, 0]})
        box = Mesh(boxGeometry, boxMaterial)
        box.setPosition([1.2, 1, 0])
        self.scene.add(box)
        self.renderTarget = RenderTarget(resolution=[512, 512])
        screenGeometry = RectangleGeometry(width=1.8, height=1.8)
        screenMaterial = TextureMaterial(self.renderTarget.texture)
        screen = Mesh(screenGeometry, screenMaterial)
        screen.setPosition([1.2, 1, 0.11])
        self.scene.add(screen)
        self.skyCamera = Camera(aspectRatio=512 / 512)
        self.skyCamera.setPosition([0, 10, 0.1])
        self.skyCamera.lookAt([0, 0, 0])
        self.scene.add(self.skyCamera)

    def update(self):
        self.sphere.rotateY(0.01337)
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.skyCamera, renderTarget=self.renderTarget)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Test(screenSize=[800, 600]).run()
