from math import pi, sin, cos
import Reader
from StructureLibrary import StructureLibrary
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import *
loadPrcFileData("", "want-wx true")
from panda3d.core import VBase4
from direct.gui.DirectGui import *
from Menu import DropDownMenu, PopupMenu

import wx


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
        Class used for creating frames other than the main one
        """

    def __init__(self, title, pandaParent, structure, typeCount, parent=None):

        self.pandaParent = pandaParent
        self.structure = structure
        self.typeCount = typeCount

        wx.Frame.__init__(self, parent=parent, title=title)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        # btn = wx.Button(self, label='Hi')
        # btn.Bind(wx.EVT_BUTTON, self.printHi)
        colorTypes = ['Red', 'Green', 'Blue']
        xtext = wx.StaticText(self, -1, "X Cell:")
        ytext = wx.StaticText(self, -1, "Y Cell:")
        ztext = wx.StaticText(self, -1, "Z Cell:")

        self.xpos = wx.TextCtrl(self, -1, "", size=(200, -1))
        self.ypos = wx.TextCtrl(self, -1, "", size=(200, -1))
        self.zpos = wx.TextCtrl(self, -1, "", size=(200, -1))


        pSizeText = wx.StaticText(self, -1, "Particle Size:")
        self.pSizeEntry = wx.TextCtrl(self, -1, "", size=(200, -1))

        submitButton = wx.Button(self, -1, "Submit")
        cancelButton = wx.Button(self, -1, "Cancel")
        submitButton.Bind(wx.EVT_BUTTON,self.submit)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=15)

        # Put in if Else Statements
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
        # End if else statements

        hbox.Add(sizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)

        sizer2 = wx.FlexGridSizer(cols=2, hgap=6, vgap=15)
        sizer2.AddMany([cancelButton, submitButton])
        hbox2.Add(sizer2, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)

        vbox.Add(hbox)
        vbox.Add(hbox2)

        self.SetSizer(vbox)
        self.Center()
        gp = base.win.getPipe()
        print(gp.getDisplayWidth())
        self.SetSize(400, int(gp.getDisplayHeight() * 0.35))
        self.Show()

    def submit(self,event):
        self.xval = self.xpos.GetValue()
        self.yval = self.ypos.GetValue()
        self.zval = self.zpos.GetValue()
        self.partSize = self.pSizeEntry.GetValue()
        self.type1 = self.combo1.GetValue()
        self.type2 = self.combo2.GetValue()
        self.type3 = self.combo3.GetValue()

        self.pandaParent.create_structure(self.structure, self)
        self.Close()

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        # add menu
        # menubar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        # self.Bind(wx.EVT_MENU, self.onQuit, fitem)
        # menubar.Append(fileMenu, '&File')
        # self.SetMenuBar(menubar)

    def onQuit(self, evt):
        self.Close()


class MainApp(ShowBase):
    """

    MainApp

    """

    step = 0

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
        #self.frame.SetDimensions(0, 0, 800, 600)
        self.frame.SetSize(int(self.pipe.getDisplayWidth() * 0.8), int(self.pipe.getDisplayHeight() * 0.8))
        self.frame.Center()
        self.frame.Show()
        self.frame.Layout()

        # YNJH : create P3D window
        wp = WindowProperties()
        wp.setOrigin(0, 0)
        #wp.setSize(800,600)
        #wp.setSize(int(self.pipe.getDisplayWidth() * 0.8), int(self.pipe.getDisplayHeight() * 0.8))
        wp.setSize(self.frame.GetSize()[0], self.frame.GetSize()[1])
        wp.setParentWindow(self.frame.GetHandle())
        self.openMainWindow(type = 'onscreen', props=wp, size=(self.frame.GetSize()[0], self.frame.GetSize()[1]))
        print(self.frame.GetSize()[0])
        print(self.frame.GetSize()[1])
        print(self.pipe.getDisplayWidth())
        print(self.pipe.getDisplayHeight())

        self.setBackgroundColor(0, 0, 0);



        self.taskMgr.add(self.updateCameraLight, "UpdateCameraLight")
        #self.camera.setPos(20 * sin(1), -20.0 * cos(1), 0)
        #self.camera.setHpr(0, 0, 0)

        # create the root node of the scene graph
        self.root = self.render.attachNewNode("Root")
        self.root.reparentTo(self.render)

        self.set_up_lighting()

        #setting up mouse to move the camera
        self.disableMouse()
        angleDegrees = 60.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 0)
        self.camera.setHpr(angleDegrees, 0, 0)

        mat = Mat4(camera.getMat())
        mat.invertInPlace()
        self.mouseInterfaceNode.setMat(mat)
        self.plnp.setMat(mat)
        self.enableMouse()


        # create the menu for the window
        menuBar = DropDownMenu(
            items=(
                # (name, action)
                ("_File", self.createFileMenuItems),
                ("_Edit", self.createEditMenuItems),
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
        print(self.pipe.getDisplayWidth())
        # Need to call structure_function to get the number of type of atoms
        dummy,typeCount = structure_function(1,1,1)
        frame = PopupFrame(title=title, pandaParent=self, structure=structure_function, typeCount=typeCount)


    def create_structure(self, structure_function, frame):
        x = int(frame.xval)
        y = int(frame.yval)
        z = int(frame.zval)
        partSize = float(frame.partSize)
        points,count = structure_function(x,y,z)
        typeColers = [frame.type1,frame.type2,frame.type3,str(count)]
        print('This is count')
        print(count)
        self.render_points(points,partSize,typeColors)


    def input_dialog(self):
        answer = simpledialog.askinteger("Input", "Enter an int", parent=self.tk_parent, minvalue=0, maxvalue=100)

        if answer:
            self.step = answer
            Reader.write_points('points.txt', self.step)
            points = Reader.read_points('points.txt')

            self.render_points(points)

    def read_in_file(self):
        fileDialog = wx.FileDialog(None, "Open XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed their mind

        # Proceed loading the file chosen by the user
        filename = fileDialog.GetPath()
        try:
            if filename:
                points = StructureLibrary.FileReader(filename)
                self.render_points(points)

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
        print(self.pipe.getDisplayWidth())
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
    def render_points(self, point_list, particleSize):
        """

        render_points

        """
        # Create Popup to specify the particle size
        #particleSize = .2
        # dlg = wx.TextEntryDialog(self.frame, "Particle Size", "Enter a Particle Size")
        # if dlg.ShowModal() == wx.ID_OK:
        #     result = dlg.GetValue()
        #     try:
        #         particleSize = float(result)
        #     except:
        #         wx.MessageBox(message="The user did not enter a numeric value so " +
        #         "the particle size  could not be changed. The default size is .2",
        #         caption='Incorrect Entry, Particle Size not changed',
        #         style=wx.OK | wx.ICON_INFORMATION)
        #         print("An exception occurred")
            # =======
            # get max coord of poitns of structure
            # so that it can be centered in the viewport
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
                self.sphere.setMaterial(self.myMaterial1)
            elif p[3] == 2:
                self.sphere.setMaterial(self.myMaterial2)
            else:
                self.sphere.setMaterial(self.myMaterial3)
            self.sphere.setScale(particleSize)
    #dlg.Destroy()
    #END render_points

    def updateCameraLight(self, task):
        """

        updateCameraLight

        """

        #print("spin camera") WORKS
        mat=Mat4(self.mouseInterfaceNode.getMat())
        mat.invertInPlace()
        self.plnp.setMat(mat)
        return Task.cont
    #END spinCameraTask


    def quit(self, event=None):
        self.onDestroy(event)
        try:
            base
        except NameError:
            sys.exit()
        base.userExit()


#END MainApp

################################################################################
# running the program for testing. This will need to be put into a different
# main file to make running and testing easier
################################################################################
points_file = 'points.txt'

points = []

Reader.write_points(points_file, 10)

#points = Reader.read_points(points_file)

app = MainApp()
app.run()

print('Done!')
