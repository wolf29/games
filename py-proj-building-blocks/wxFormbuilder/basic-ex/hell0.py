# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 27 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MainFrame
###########################################################################
def main():
    MainFrame(wx.Frame)

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 289,171 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.fileMenu = wx.Menu()
		self.menuExit = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Exit ", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.AppendItem( self.menuExit )
		
		self.m_menubar2.Append( self.fileMenu, u"File" )
		
		self.SetMenuBar( self.m_menubar2 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnSayHello = wx.Button( self, wx.ID_ANY, u"Say hello", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btnSayHello, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer12 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class HelloDialog
###########################################################################

class HelloDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__  ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 190,144 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer14.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Hello World!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 14, 74, 90, 90, False, "Times New Roman" ) )
		
		bSizer14.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer14.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		m_sdbSizer3.Realize();
		bSizer13.Add( m_sdbSizer3, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer13 )
		self.Layout()
	
	def __del__( self ):
		pass
	
main()
