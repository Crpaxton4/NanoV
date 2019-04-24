from math import pi, sin, cos
import Reader
from StructureLibrary import StructureLibrary
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import *
from panda3d.core import VBase4
from direct.gui.DirectGui import *
from Menu import DropDownMenu, PopupMenu

import wx

loadPrcFileData("", "want-wx true")


"""
MainApp.py

https://discourse.panda3d.org/t/fully-working-wxpython-panda3d-example/15022

Look at this code to possibly restructure
this entire class to use wx as the main
window and panda is just a widget


installer

https://www.panda3d.org/manual/?title=Distributing_as_a_self-contained_installer&oldid=7571


"""
class PopupFrame(wx.Frame):
    """
        Class used for creating frames other than the main one.
        It holds a couple different inputs for the user depending on
        where (File input or structure library) the user clicks
        """

    def __init__(self, title, pandaParent, structure, typeCount, isStructInput, filename, parent=None):
        # Sets the constructor values
        self.pandaParent = pandaParent
        self.structure = structure
        self.typeCount = typeCount
        self.isStructInput = isStructInput
        self.filename = filename
        # Creates the popup frame and the sizer boxes that help format the inputs
        wx.Frame.__init__(self, parent=parent, title=title)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        colorTypes = ['Red', 'Green', 'Blue']
        # Check to see if the frame should be for structures
        # If the frame is for the structure library, an X, Y, and Z cell must be
        # input by the User
        if self.isStructInput:
            xtext = wx.StaticText(self, -1, "X Cell:")
            ytext = wx.StaticText(self, -1, "Y Cell:")
            ztext = wx.StaticText(self, -1, "Z Cell:")

            self.xpos = wx.TextCtrl(self, -1, "3", size=(200, -1))
            self.ypos = wx.TextCtrl(self, -1, "3", size=(200, -1))
            self.zpos = wx.TextCtrl(self, -1, "3", size=(200, -1))

            submitButton = wx.Button(self, -1, "Submit")
            cancelButton = wx.Button(self, -1, "Cancel")
            submitButton.Bind(wx.EVT_BUTTON,self.submit)
            cancelButton.Bind(wx.EVT_BUTTON,self.cancel)
        else:
            submitButton2 = wx.Button(self, -1, "Submit")
            cancelButton2 = wx.Button(self, -1, "Cancel")
            submitButton2.Bind(wx.EVT_BUTTON,self.submit2)
            cancelButton2.Bind(wx.EVT_BUTTON,self.cancel2)

        pSizeText = wx.StaticText(self, -1, "Particle Size:")
        self.pSizeEntry = wx.TextCtrl(self, -1, ".2", size=(200, -1))


        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=15)

        # Put in if Else Statements
        if isStructInput:
            if typeCount == 1:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([xtext, self.xpos,ytext,self.ypos,ztext,self.zpos,pSizeText,self.pSizeEntry,type1Txt,self.combo1])
            elif typeCount == 2:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type2Txt =  wx.StaticText(self, -1, "Type 2:")
                self.combo2 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([xtext, self.xpos,ytext,self.ypos,ztext,self.zpos,pSizeText,self.pSizeEntry,type1Txt,self.combo1,type2Txt,self.combo2])
            else:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type2Txt =  wx.StaticText(self, -1, "Type 2:")
                self.combo2 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type3Txt =  wx.StaticText(self, -1, "Type 3:")
                self.combo3 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([xtext, self.xpos,ytext,self.ypos,ztext,self.zpos,pSizeText,self.pSizeEntry,type1Txt,self.combo1,type2Txt,self.combo2,type3Txt,self.combo3])

            hbox.Add(sizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
            sizer2 = wx.FlexGridSizer(cols=2, hgap=6, vgap=15)
            sizer2.AddMany([cancelButton, submitButton])
            hbox2.Add(sizer2, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        else:
            if typeCount == 1:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([pSizeText,self.pSizeEntry,type1Txt,self.combo1])
            elif typeCount == 2:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type2Txt =  wx.StaticText(self, -1, "Type 2:")
                self.combo2 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([pSizeText,self.pSizeEntry,type1Txt,self.combo1,type2Txt,self.combo2])
            else:
                type1Txt =  wx.StaticText(self, -1, "Type 1:")
                self.combo1 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type2Txt =  wx.StaticText(self, -1, "Type 2:")
                self.combo2 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                type3Txt =  wx.StaticText(self, -1, "Type 3:")
                self.combo3 = wx.ComboBox(self,choices = colorTypes, size=(200, -1))
                sizer.AddMany([pSizeText,self.pSizeEntry,type1Txt,self.combo1,type2Txt,self.combo2,type3Txt,self.combo3])

            hbox.Add(sizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
            sizer2 = wx.FlexGridSizer(cols=2, hgap=6, vgap=15)
            sizer2.AddMany([cancelButton2, submitButton2])
            hbox2.Add(sizer2, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
            # End if else statements


        vbox.Add(hbox)
        vbox.Add(hbox2)

        self.SetSizer(vbox)
        self.Center()
        gp = base.win.getPipe()
        self.SetSize(450, int(gp.getDisplayHeight() * 0.35))
        self.Show()

    def submit(self,event):
        self.isSinput = self.isStructInput
        self.xval = self.xpos.GetValue()
        self.yval = self.ypos.GetValue()
        self.zval = self.zpos.GetValue()
        self.partSize = self.pSizeEntry.GetValue()
        if self.typeCount == 1:
            self.type1 = self.combo1.GetValue()
        elif self.typeCount == 2:
            self.type1 = self.combo1.GetValue()
            self.type2 = self.combo2.GetValue()
        else:
            self.type1 = self.combo1.GetValue()
            self.type2 = self.combo2.GetValue()
            self.type3 = self.combo3.GetValue()

        self.pandaParent.create_structure(self.structure, self)
        self.Close()
    def cancel(self,event):
        self.Close()

    def submit2(self,event):
        self.isSinput = self.isStructInput
        self.partSize = self.pSizeEntry.GetValue()
        if self.typeCount == 1:
            self.type1 = self.combo1.GetValue()
        elif self.typeCount == 2:
            self.type1 = self.combo1.GetValue()
            self.type2 = self.combo2.GetValue()
        else:
            self.type1 = self.combo1.GetValue()
            self.type2 = self.combo2.GetValue()
            self.type3 = self.combo3.GetValue()
        self.fname = self.filename
        self.pandaParent.create_structure(self.structure, self)
        self.Close()
    def cancel2(self,event):
        self.Close()

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

    def onQuit(self, evt):
        sys.exit()


class MainApp(ShowBase):
    """

    MainApp

    """

    def __init__(self):
        """

        __init__

        """
        ShowBase.__init__(self)


        #Created the WxX window that panda will be running in
        # setup application window
        self.startWx()
        self.wxApp.Bind(wx.EVT_CLOSE, self.quit)
        self.frame = Frame(None, wx.ID_ANY, 'NanoV')
        self.frame.SetSize(int(self.pipe.getDisplayWidth() * 0.8), int(self.pipe.getDisplayHeight() * 0.8))
        self.frame.Center()
        self.frame.Show()
        self.frame.Layout()

        # YNJH : create P3D window
        wp = WindowProperties()
        wp.setOrigin(0, 0)
        wp.setSize(self.frame.GetSize()[0], self.frame.GetSize()[1])
        wp.setParentWindow(self.frame.GetHandle())
        #self.openMainWindow(type = 'onscreen', props=wp, size=(self.frame.GetSize()[0], self.frame.GetSize()[1]))
        self.openMainWindow(type = 'onscreen', props=wp, size=(self.frame.GetSize()[0], int(self.frame.GetSize()[1]*.97)))
        self.setBackgroundColor(0, 0, 0);

        self.taskMgr.add(self.updateStructureRotation, "UpdateStructureRotation")

        # create the root node of the scene graph
        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(self.render)

        #setting up mouse to move the camera
        self.disableMouse()
        self.camera.setPos(0, -40, 0)


        # create the axis indicator
        self.axis=self.loader.loadModel('zup-axis.egg.pz')
        base.axis.reparentTo(self.camera)
        self.axis.setPos(-3.075, 10, -1.9)
        self.axis.setScale(.04)
        self.mouseTask=taskMgr.add(self.updateAxisIndicator, 'UpdateAxisIndicator')

        self.set_up_lighting()

        mat = Mat4(camera.getMat())
        mat.invertInPlace()
        self.mouseInterfaceNode.setMat(mat)
        self.plnp.setMat(mat)

        # create the menu for the window
        menuBar = DropDownMenu(
            items=(
                # (name, action)
                ("_File", self.createFileMenuItems),
                #("_Edit", self.createEditMenuItems),
                ("Structure _Library", self.createStructureMenuItems)
            ),

            sidePad = 0.4,

            align = DropDownMenu.ALeft,
            effect = DropDownMenu.PTop,
            edgePos = DropDownMenu.PTop,

            baselineOffset = -0.35,
            scale = 0.045,
            itemHeight = 1.15,
            leftPad = 0.4,
            underscoreThickness = 1,

            BGColor = (1, 1, 1, 1),
            BGBorderColor = (1, 1, 0.9, 1),

            separatorHeight = 0,
            separatorColor = (0, 0, 0, 0.5),

            frameColorHover = (0.7, 0.7, 0.7, 1),
            frameColorPress = (0.3, 0.3, 0.3, 0.85),

            textColorReady = (0, 0, 0, 1),
            textColorHover = (0, 0, 0, 1),
            textColorPress = (0, 0, 0, 1),
            textColorDisabled = (0.65, 0.65, 0.65, 1),

            draggable=True,
            onMove=None
        )

        print("DONE")
    #END __init__

    ############################################################################
    # Menu item actions
    # TODO Change from button commands to functions for each menu item
    ############################################################################

    def atom_property_dialog(self, structure_function):
        title = 'Structure Information'
        # Need to call structure_function to get the number of type of atoms
        dummy,typeCount = structure_function(1,1,1)
        frame = PopupFrame(title=title, pandaParent=self, structure=structure_function, typeCount=typeCount, isStructInput=True,filename="")


    def create_structure(self, structure_function, frame):
        typeColors = []
        count = 0
        try:
            partSize = float(frame.partSize)
            if frame.isSinput:
                x = int(frame.xval)
                y = int(frame.yval)
                z = int(frame.zval)
                points,count = structure_function(x,y,z)
                if count == 1:
                    typeColors = [frame.type1]
                elif count == 2:
                    typeColors = [frame.type1,frame.type2]
                else:
                    typeColors = [frame.type1,frame.type2,frame.type3]
            else:
                points,count = StructureLibrary.FileReader(frame.fname)
                if count == 1:
                    typeColors = [frame.type1]
                elif count == 2:
                    typeColors = [frame.type1,frame.type2]
                else:
                    typeColors = [frame.type1,frame.type2,frame.type3]
            colorCycle = ["Red","Green","Blue"]
            if count == 1:
                if typeColors[0] not in colorCycle:
                    wx.MessageBox(message="Please make sure you have entered a color " +
                    "from the provided list.",
                    caption='User has entered an incorrect color value',
                    style=wx.OK | wx.ICON_INFORMATION)
                    print("An exception occurred")
                else:
                    self.render_points(points,partSize,typeColors)
            elif count == 2:
                if typeColors[0] not in colorCycle or typeColors[1] not in colorCycle:
                    wx.MessageBox(message="Please make sure you have entered a color " +
                    "from the provided list.",
                    caption='User has entered an incorrect color value',
                    style=wx.OK | wx.ICON_INFORMATION)
                    print("An exception occurred")
                else:
                    self.render_points(points,partSize,typeColors)
            else:
                if typeColors[0] not in colorCycle or typeColors[1] not in colorCycle or typeColors[2] not in colorCycle:
                    wx.MessageBox(message="Please make sure you have entered a color " +
                    "from the provided list.",
                    caption='User has entered an incorrect color value',
                    style=wx.OK | wx.ICON_INFORMATION)
                    print("An exception occurred")
                else:
                    self.render_points(points,partSize,typeColors)

        except:
            wx.MessageBox(message="Please make sure the particle size is a number."+
            " If applicable, please make sure the "+
            "X Cell, Y Cell, and Z Cell values are positive integers.",
            caption='User has entered an incorrect numeric value',
            style=wx.OK | wx.ICON_INFORMATION)
            print("An exception occurred")

    def read_in_file(self):
        fileDialog = wx.FileDialog(None, "Open XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed their mind

        # Proceed loading the file chosen by the user
        filename = fileDialog.GetPath()
        try:
            if filename:
                title = 'Structure Information'
                # Need to call FileReader to get the number of type of atoms
                dummy,typeCount = StructureLibrary.FileReader(filename)
                frame = PopupFrame(title=title, pandaParent=self, structure=None, typeCount=typeCount,isStructInput=False, filename=filename)

        except IOError:
            wx.LogError("Cannot open file '%s'." % newfile)


        print("Read file")
    ############################################################################
    # Methods to create sub menus of menu bar
    ############################################################################
    def createFileMenuItems(self):
        """

        createFileMenuItems

        """

        return (
            ('_Load File...', 0, self.read_in_file),
            0
        )

    def createEditMenuItems(self):
        """

        createFileMenuItems

        """

        return (
            ('Load Structure', 0, self.popup),
            0
        )

    def popup(self):
        title = 'Structure Information'
        frame = PopupFrame(title=title)

    def createStructureMenuItems(self):
        """

        createStructureMenuItems

        """

        return (
            ("CaB6", 0, self.atom_property_dialog, StructureLibrary.CaB6),
            0,
            ("AlB2", 0, self.atom_property_dialog, StructureLibrary.AlB2),
            0,
            ("BCC", 0, self.atom_property_dialog, StructureLibrary.BCC),
            0,
            ("Cu3Au", 0, self.atom_property_dialog, StructureLibrary.Cu3Au),
            0,
            ("Diamond", 0, self.atom_property_dialog, StructureLibrary.Diamond),
            0,
            ("Laves", 0, self.atom_property_dialog, StructureLibrary.Laves),
            0,
            ("SC", 0, self.atom_property_dialog, StructureLibrary.SC),
            0,
            ("MgCu2", 0, self.atom_property_dialog, StructureLibrary.MgCu2),
            0,
            ("FCC", 0, self.atom_property_dialog, StructureLibrary.FCC),
            0,
            ("MgSnCu4", 0, self.atom_property_dialog, StructureLibrary.MgSnCu4),
            0,
            ("NaCl", 0, self.atom_property_dialog, StructureLibrary.NaCl),
            0,
            ("ZincBlende", 0, self.atom_property_dialog, StructureLibrary.ZincBlende),
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
        self.alight.setColor(VBase4(0.5, 0.5, 0.5, 1))
        self.alnp = self.render.attachNewNode(self.alight)
        self.render.setLight(self.alnp)

        # Create a positional point light
        self.plight = PointLight('plight')
        self.plight.setColor(VBase4(1.0, 1.0, 1.0, 1))
        self.plnp = self.render.attachNewNode(self.plight)
        self.render.setLight(self.plnp)

        self.axisLight = AmbientLight('axisLight')
        self.axisLight.setColor(VBase4(0.7, 0.7, 0.7, 1))
        self.axislnp = self.render.attachNewNode(self.axisLight)
        self.axis.setLight(self.axislnp)

    #END set_up_lighting


    # TODO change this to accept a list of possible materials
    # so that they are not hard coded into the function.

    # TODO move the camera so that the scale of the scpheres will be 1
    # to make the math easier
    def render_points(self, point_list, particleSize, typeColors):
        """

        render_points

        """
        max_x_point = max(point_list, key=lambda p: p[0])
        max_x_val = max_x_point[0]

        max_y_point = max(point_list, key=lambda p: p[1])
        max_y_val = max_y_point[1]

        max_z_point = max(point_list, key=lambda p: p[2])
        max_z_val = max_z_point[2]

        print([max_x_val, max_y_val, max_z_val])

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

        # green
        self.myMaterial3 = Material()
        self.myMaterial3.setAmbient((0.2, 0.44, 0.2, 1.0))
        self.myMaterial3.setDiffuse((0.2, 0.7, 0.2, 1.0))
        self.myMaterial3.setSpecular((0.2, 0.45, 0.2, 1.0))
        self.myMaterial3.setShininess(90.0) #Make this material shiny

        root_node = self.render.find('Root')
        root_node.removeNode()

        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(render)

        # Create
        for p in point_list:
            self.sphere = self.loader.loadModel("sphere.egg.pz")
            self.sphere.reparentTo(self.render.find('Root'))
            self.sphere.setPos(p[0] - max_x_val/2, p[1] - max_y_val/2, p[2] - max_z_val/2)

            if p[3] == 1:
                if typeColors[0] == 'Red':
                    self.sphere.setMaterial(self.myMaterial1)
                elif typeColors[0] == 'Blue':
                    self.sphere.setMaterial(self.myMaterial2)
                else:
                    self.sphere.setMaterial(self.myMaterial3)

            elif p[3] == 2:
                if typeColors[1] == 'Red':
                    self.sphere.setMaterial(self.myMaterial1)
                elif typeColors[1] == 'Blue':
                    self.sphere.setMaterial(self.myMaterial2)
                else:
                    self.sphere.setMaterial(self.myMaterial3)
            else:
                if typeColors[2] == 'Red':
                    self.sphere.setMaterial(self.myMaterial1)
                elif typeColors[2] == 'Blue':
                    self.sphere.setMaterial(self.myMaterial2)
                else:
                    self.sphere.setMaterial(self.myMaterial3)
            self.sphere.setScale(particleSize * 0.2)

            self.camera.setPos(0, -40, 0) # reset the camera after new structure is made
            self.camera.setHpr(0, 0, 0)
            self.plnp.setPos(0, -40, 0)
            self.plnp.setHpr(0, 0, 0)
            self.mouseInterfaceNode.setHpr(0, 0, 0)
    #END render_points


    def updateStructureRotation(self, task):
        """

        updateCameraLight

        """
        # rotate the root node with the mouse
        self.root.setHpr(self.mouseInterfaceNode.getHpr())
        return Task.cont
    #END updateStructureRotation

    def updateAxisIndicator(self, task):
        self.axis.setHpr(self.root.getHpr())
        return Task.cont
    #END updateAxisIndicator

    def quit(self, event=None):
        self.onDestroy(event)
        try:
            base
        except NameError:
            sys.exit()
        base.userExit()
#END MainApp

app = MainApp()
app.run()
