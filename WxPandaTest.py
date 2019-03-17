import wx

from direct.showbase.ShowBase import ShowBase
import panda3d.core as core

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        # add menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.onQuit, fitem)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

    def onQuit(self, evt):
        self.Close()

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # setup application window
        self.startWx()
        self.wxApp.Bind(wx.EVT_CLOSE, self.quit)
        self.frame = Frame(None, wx.ID_ANY, 'Editor')
        self.frame.SetDimensions(0, 0, 800, 600)
        self.frame.Center()
        self.frame.Show()
        self.frame.Layout()

        # YNJH : create P3D window
        wp = core.WindowProperties()
        wp.setOrigin(0, 0)
        wp.setSize(800,600)
        wp.setParentWindow(self.frame.GetHandle())
        base.openMainWindow(type = 'onscreen', props=wp, size=(800, 600))

        # load egg model
        panda = base.loader.loadModel('panda')
        panda.reparentTo(base.render)
        panda.setScale(10, 10, 10)
        panda.setPos(0, 500, -50)

    def quit(self, event=None):
        self.onDestroy(event)
        try:
            base
        except NameError:
            sys.exit()
        base.userExit()

App().run()
