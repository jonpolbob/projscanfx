# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#projet general de scan fxutilise pywebkit00 qui se charge 
__author__ = "jonepol"
__date__ = "$29 juil. 2015 11:32:18$"

import wx
import pywekit00



if __name__ == '__main__': 
  app = wx.App() 
  
  dialog = pywekit00.MyBrowser(None, -1)
  print("load")
  dialog.Show()
  #dialog.browser.Hide()
  dialog.browser.LoadURL("http://www.fxstreet.fr/rates/currency-rates/")
  pywekit00.sendmail('started')
  app.MainLoop() 
  
  
