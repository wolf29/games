
import wx
from wx import xrc
import sys

class MainFrame(object):

    def __init__(self, xml):
        self.xml = xml
        self.frame = xml.LoadFrame(None,'MainFrame')
        self.frame.Bind(wx.EVT_MENU, self.on_menu_exit, id=xrc.XRCID('menuExit'))
        self.frame.Bind(wx.EVT_BUTTON, self.on_say_hello, id=xrc.XRCID('btnSayHello'))        
        self.frame.Show()

    def on_say_hello(self, evt):
        dlg = self.xml.LoadDialog(self.frame, 'HelloDialog')
        dlg.ShowModal()
        dlg.Destroy()

    def on_menu_exit(self, evt):
        self.frame.Destroy()
        sys.exit(0)
       

class HelloWordApp(wx.App):

    def OnInit(self):
        xml = xrc.XmlResource('HelloWorld.xrc')
        self.MainFrame = MainFrame(xml)
        return True


if __name__ == '__main__':
    app = HelloWordApp(0)
    app.MainLoop()


