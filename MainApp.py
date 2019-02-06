from math import pi, sin, cos
import Reader
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import *
from panda3d.core import VBase4
from direct.gui.DirectGui import *
from Menu import DropDownMenu, PopupMenu


"""

Prototype.py

"""

class MainApp(ShowBase):
    """

    MainApp

    """

    step = 0

    def __init__(self):
        """

        __init__

        """

        #call superclass constructor
        ShowBase.__init__(self)

        # TODO change this so that the user can control the camera position and facing
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # create the root node of the scene graph
        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(self.render)

        self.set_up_lighting()


        #TODO remove this GUI stuff and change it to the normal window menus
        print("making buttons")

        #self.b1 = DirectButton(frameSize = (-0.5, 0.5, -0.25, 0.25), pos = (0.75, 0, 0.8), text_scale = 0.25, text = ("Inc", "click!", "Inc", "disabled"), scale=.25, command=self.button_command1)
        #self.b2 = DirectButton(frameSize = (-0.5, 0.5, -0.25, 0.25), pos = (-0.75, 0, 0.8), text_scale = 0.25, text = ("Dec", "click!", "Dec", "disabled"), scale=.25, command=self.button_command2)


        menuBar = DropDownMenu(
            items=(
                # (name, action)
                ("_File", self.createFileMenuItems),
                ("_Edit", self.createFileMenuItems)
            ),

            sidePad = 0.75,

            align = DropDownMenu.ALeft,
            effect = DropDownMenu.PTop,
            edgePos = DropDownMenu.PTop,

            baselineOffset = -0.35,
            scale = 0.045,
            itemHeight = 1.2,
            leftPad = 0.2,
            underscoreThickness = 1,

            BGColor = (0.9, 0.9, 0.8, 0.94),
            BGBorderColor = (0.8, 0.3, 0, 1),

            separatorHeight = 0.3,
            separatorColor = (0, 0, 0, 1),

            frameColorHover = (0.3, 0.3, 0.3, 1),
            frameColorPress = (0, 1, 0, 0.85),

            textColorReady = (0, 0, 0, 1),
            textColorHover = (1, 0.7, 0.2, 1),
            textColorPress = (0, 0, 0, 1),
            textColorDisabled = (0.65, 0.65, 0.65, 1),

            draggable=True
            #onMove=None
        )

        print("DONE")
    #END __init__

    ############################################################################
    # Menu item actions
    # TODO Change from button commands to functions for each menu item
    ############################################################################

    def button_command1(self):
        """

        button_command1

        """
        print("button1")
        root_node = self.render.find('Root')
        root_node.removeNode()

        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(render)

        self.step += 1
        Reader.write_points('points.txt', self.step)
        points = Reader.read_points('points.txt')

        self.render_points(points)
    #END button_command1

    def button_command2(self):
        """

        button_command2

        """

        print("Button2")
        root_node = self.render.find('Root')
        root_node.removeNode()

        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(render)

        self.step -= 1
        if self.step <= 0:
            self.step = 0

        Reader.write_points('points.txt', self.step)

        points = Reader.read_points('points.txt')

        self.render_points(points)
    #END button_command2

    ############################################################################
    # Methods to create sub menus of menu bar
    ############################################################################
    def createFileMenuItems(self):
        """

        createFileMenuItems

        """

        return (
            ("_Inc", 0, self.button_command1),
            0,
            ("_Dec", 0, self.button_command2),
            0
        )

    ############################################################################
    # Rendering setup methods
    ############################################################################
    def set_up_lighting(self):
        """

        set_up_lighting

        """

        print("setting up lights")
        # Create Ambient Light
        self.alight = AmbientLight('alight')
        self.alight.setColor(VBase4(0.2, 0.2, 0.2, 1))
        self.alnp = self.render.attachNewNode(self.alight)
        self.render.setLight(self.alnp)

        # Create a positional point light
        self.plight = PointLight('plight')
        self.plight.setColor(VBase4(1.0, 1.0, 1.0, 1))

        self.plnp = self.render.attachNewNode(self.plight)
        self.render.setLight(self.plnp)
    #END set_up_lighting


    # TODO change this to accept a list of possible materials
    # so that they are not hard coded into the function.

    # TODO move the camera so that the scale of the scpheres will be 1
    # to make the math easier
    def render_points(self, point_list):
        """

        render_points

        """

        #Create Material for all the spheres to be rendered
        # red
        self.myMaterial1 = Material()
        self.myMaterial1.setAmbient((0.44, 0.2, 0.2, 1.0))
        self.myMaterial1.setDiffuse((0.7, 0.2, 0.2, 1.0))
        self.myMaterial1.setSpecular((0.45, 0.2, 0.2, 1.0))
        self.myMaterial1.setShininess(90.0) #Make this material shiny

        # blue
        self.myMaterial2 = Material()
        self.myMaterial2.setAmbient((0.2, 0.2, 0.44, 1.0))
        self.myMaterial2.setDiffuse((0.2, 0.2, 0.7, 1.0))
        self.myMaterial2.setSpecular((0.2, 0.2, 0.45, 1.0))
        self.myMaterial2.setShininess(90.0) #Make this material shiny


        flag = True

        # Create
        for p in point_list:
            self.sphere = self.loader.loadModel("/c/Users/Chris/Desktop/models/sphere.egg.pz")
            self.sphere.reparentTo(self.render.find('Root'))
            self.sphere.setPos(p[0], p[1], p[2])

            if flag:
                self.sphere.setMaterial(self.myMaterial1)
            else:
                self.sphere.setMaterial(self.myMaterial2)

            flag = not flag

            self.sphere.setScale(0.5)
    #END render_points

    #TODO either remove this method or make it a menu item that is a neat effect
    # this is a strech goal

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        """

        spinCameraTask

        """

        #print("spin camera") WORKS
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 0)
        self.camera.setHpr(angleDegrees, 0, 0)

        self.plnp.setPos((20 * sin(angleRadians), -20.0 * cos(angleRadians), 0))
        return Task.cont
    #END spinCameraTask

#END MainApp

################################################################################
# running the program for testing. This will need to be put into a different
# main file to make running and testing easier
################################################################################
points_file = 'points.txt'

points = []

## Create points for 'atoms'
#for x in [-2.5, 0, 2.5]:
    # for y in [-2.5, 0, 2.5]:
    #     for z in [-2.5, 0, 2.5]:
    #         points += [[x, y, z]]

Reader.write_points(points_file, 10)

#points = Reader.read_points(points_file)

app = MainApp()
app.run()

print('Done!')
