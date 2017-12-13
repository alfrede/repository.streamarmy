#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import os
import re
import sys
import urllib
import urllib2
import urlparse
import list

import base64


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()


#############################################################
#################### SET ADDON ID ###########################
_addon_id_ = 'plugin.video.kickoff'
_self_ = xbmcaddon.Addon(id=_addon_id_)


#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	


#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bga.gif'))

Buttonaf = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'champf.png'))
Buttona = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'champ.png'))

Buttonbf = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'premf.png'))
Buttonb = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'prem.png'))

Buttoncf = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'otherf.png'))
Buttonc = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'other.png'))

Buttondf = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'highf.png'))
Buttond = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'high.png'))

Buttonef = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'livef.png'))
Buttone = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'live.png'))


Buttonzz = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'logo.gif'))



#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():

    window = Main('kickoff')
    window.doModal()
    del window
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data
    
def Get_Msg(self):
    global Item_Desc
    Item_Desc  =  []
    url = 'https://pastebin.com/raw/cvyT5p5S'
    link = Get_Data(url)
    self.textbox.autoScroll(1000, 1000, 1000)
    self.textbox.setText(link)
    
    
def sendtolistchamp(self):

    self.close
    list.listwindow('Champions League')
    
def sendtolistprem(self):

    self.close
    source = dialog.select('[COLOR blue]Choose AceStream Or Normal Links[/COLOR]', ['[COLOR skyblue]Acestream[/COLOR]','[COLOR skyblue]Normal[/COLOR]'])
    if source ==0:
        list.listwindow('Premiership ACE')
    if source ==1:
        list.listwindow('Premiership Norm')
    
def sendtolistother(self):

    self.close
    list.listwindow('Other')
    
def sendtolistreplay(self):

    self.close
    list.listwindow('Replay')
    
def sendtolistlive(self):

    self.close
    list.listwindow('Live Channels')


#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")
    
    def __init__(self, title='kickoff'):
        super(Main, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.button1, lambda:sendtolistchamp(self))
        self.connect(self.button2, lambda:sendtolistprem(self))
        self.connect(self.button3, lambda:sendtolistother(self))
        self.connect(self.button4, lambda:sendtolistreplay(self))
        self.connect(self.button5, lambda:sendtolistlive(self))
        self.connect(self.button11, lambda:(self))
        self.setFocus(self.button1)
        Get_Msg(self)
        
    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)
        
        self.textbox = pyxbmct.TextBox(textColor='0xFFFFFFFF')
        self.placeControl(self.textbox, 80, 1, 30, 27)
        
    def set_active_controls(self):
        self.List =	pyxbmct.List(buttonFocusTexture=Listbg,_space=12,_itemTextYOffset=-7,textColor='0xFFFFFFFF')
        self.placeControl(self.List, 25, 1, 80, 23)
        
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE],
            self.List_update)

    def set_active_controls(self):
        
        self.button1 = pyxbmct.Button('',   focusTexture=Buttonaf,   noFocusTexture=Buttona)
        self.placeControl(self.button1, -4, 2,  25, 10)
        
        self.button2 = pyxbmct.Button('',   focusTexture=Buttonbf,   noFocusTexture=Buttonb)
        self.placeControl(self.button2, -4, 14,  25, 10)
        
        self.button3 = pyxbmct.Button('',   focusTexture=Buttoncf,   noFocusTexture=Buttonc)
        self.placeControl(self.button3, -4, 26,  25, 10)
        
        self.button4 = pyxbmct.Button('',   focusTexture=Buttondf,   noFocusTexture=Buttond)
        self.placeControl(self.button4, -4, 38,  25, 10)
        
        self.button5 = pyxbmct.Button('',   focusTexture=Buttonef,   noFocusTexture=Buttone)
        self.placeControl(self.button5, 80, 36,  22, 12)
        
        
        
        self.button11 = pyxbmct.Button('',   focusTexture=Buttonzz,   noFocusTexture=Buttonzz)
        self.placeControl(self.button11, 102, 36,  10, 15)

    def set_navigation(self):
        self.button1.controlRight(self.button2)
        self.button2.controlRight(self.button3)
        self.button3.controlRight(self.button4)
        self.button4.controlRight(self.button1)
        
        self.button1.controlLeft(self.button4)
        self.button2.controlLeft(self.button1)
        self.button3.controlLeft(self.button2)
        self.button4.controlLeft(self.button3)
        
        
        self.button1.controlDown(self.button5)
        self.button2.controlDown(self.button5)
        self.button3.controlDown(self.button5)
        self.button4.controlDown(self.button5)
        self.button5.controlUp(self.button4)
        
        
    def List_update(self):
        global Media_Desc

        try:
            if self.getFocus() == self.List:
            
                position = self.List.getSelectedPosition()

                Media_Desc = Item_Desc[position]
                
                self.textbox.setText(Media_Desc)
                self.textbox.autoScroll(1000, 1000, 1000)
                
        except (RuntimeError, SystemError):
            pass
