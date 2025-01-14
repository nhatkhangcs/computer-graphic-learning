from path_setup import *

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial
from geometry.geometry import Geometry
from math import sin
from numpy import arange
from material.pointMaterial import PointMaterial
from material.lineMaterial import LineMaterial


# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800 / 600)
        self.camera.setPosition([0, 0, 4])
        geometry = Geometry()
        posData = []
        for x in arange(-3.2, 3.2, 0.3):
            posData.append([x, sin(x), 0])
        geometry.addAttribute("vec3", "vertexPosition", posData)
        geometry.countVertices()
        pointMaterial = PointMaterial({"baseColor": [1, 1, 0], "pointSize": 10})
        pointMesh = Mesh(geometry, pointMaterial)
        lineMaterial = LineMaterial({"baseColor": [1, 0, 1], "lineWidth": 4})
        lineMesh = Mesh(geometry, lineMaterial)
        self.scene.add(pointMesh)
        self.scene.add(lineMesh)

    def update(self):
        # self.mesh.rotateY(0.0514)
        # self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Test(screenSize=[800, 600]).run()
