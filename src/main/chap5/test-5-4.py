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
from material.material import Material


# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800 / 600)
        self.camera.setPosition([0, 0, 1.5])
        vertexShaderCode = """ 
        uniform mat4 projectionMatrix; 
        uniform mat4 viewMatrix; 
        uniform mat4 modelMatrix; 
        in vec3 vertexPosition; 
        in vec2 vertexUV; 
        out vec2 UV; 
        void main() 
        {
            gl_Position = projectionMatrix * viewMatrix * 
        modelMatrix *
        vec4(vertexPosition, 1.0);
        UV = vertexUV; 
        } 
        """
        fragmentShaderCode = """ 
        uniform sampler2D texture1; 
        uniform sampler2D texture2; 
        in vec2 UV; 
        uniform float time; 
        out vec4 fragColor; 
        void main() 
        {
        vec4 color1 = texture2D(texture1, UV);
        vec4 color2 = texture2D(texture2, UV);
        float s = abs(sin(time));
        fragColor = s * color1 + (1.0 - s) * color2; 
        } 
        """
        gridTex = Texture("images/grid.jpg")
        crateTex = Texture("images/crate.jpg")
        self.blendMaterial = Material(vertexShaderCode, fragmentShaderCode)
        self.blendMaterial.addUniform("sampler2D", "texture1", [gridTex.textureRef, 1])
        self.blendMaterial.addUniform("sampler2D", "texture2", [crateTex.textureRef, 2])
        self.blendMaterial.addUniform("float", "time", 0.0)
        self.blendMaterial.locateUniforms()
        geometry = RectangleGeometry()
        self.mesh = Mesh(geometry, self.blendMaterial)
        self.scene.add(self.mesh)

    def update(self):
        # self.mesh.rotateY(0.0514)
        # self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)
        self.blendMaterial.uniforms["time"].data += self.deltaTime


if __name__ == "__main__":
    Test(screenSize=[800, 600]).run()
