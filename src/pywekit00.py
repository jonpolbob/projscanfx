# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#le decodage est assez complique car lle pt decimal n'est pas toujurs une virgule
#donc on decode la paire au debut, on vire la virgule apres
#puis on decode la date a la fin
#on vire juste avant les deux champs variation et changement

import analysepaires

__author__ = "jprobert"
__date__ = "$20 juil. 2015 13:00:42$"

if __name__ == "__main__":
    print("pas le bon main ! appeler projscanfx")

import wx 
import wx.html2 




# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import smtplib

def sendmail(lastring):
    return
    print ('send '+lastring)
    fromaddr = 'jonpolbob@gmail.com'
    toaddrs  = ['jpnotif@gmail.com']
    
    msg = lastring
    text_subtype = 'plain'
    
    msgmime = MIMEText(msg, text_subtype)
   
    # Credentials (if needed)
    username = 'jpnotif@gmail.com'
    password = 'pqscsq2Snt'

    # The actual mail send
    #server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server = smtplib.SMTP("smtp.gmail.com",587)
    server .ehlo()
    if server.has_extn('STARTTLS'):    
        server.starttls()
        server.ehlo
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    #server.close()
    server.quit()
    print ("mailsent")

    
        
class MyBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
      
    for paire in analysepaires.paires :
        analysepaires.lstvaleurs[paire]=[0,0,0,0,0,0,0,0];

      
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) 
    self.SetSizer(sizer) 
    self.SetSize((300, 300)) 
    self.m_pTimer = wx.Timer(self);
    #self.m_pTimerRefresh= wx.Timer(self);
    self.Bind(wx.EVT_TIMER, self.OnTimerTimeout, self.m_pTimer)
    #self.Bind(wx.EVT_TIMER, self.OnTimerRefresh, self.m_pTimerRefresh)
    #self.m_pTimer.Start(1000); dans le onloaded
    #self.m_pTimerRefresh.Start(60000);
    self.count=0
    #self.Iconize(True)

    #creation du webviewclient pour etre sensible au finished
    #wvc = wx.WebViewClient();
    #self.browser.setWebViewClient(wvc)
    self.browser.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.OnLoaded)
    self.browser.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavig)

    #self.browser.Hide() 
   

  def OnNavig(self,b):
     
      target = b.GetURL().encode('raw_unicode_escape')
      if target.find('twitter')!=-1:
          print ('rejected : twitter ')
          return False
      if target.find('facebook')!=-1:
          print ('rejected : facebook')
          return False
      if target.find('google')!=-1:
          print( 'rejected : google ')
          return False
      
      
     # print b.GetTarget(),"->", b.GetURL()
     
      return True
  
  def OnLoaded(self,b):
      self.browser.Show() 
      print ('loadd')
      self.m_pTimer.Start(1000) #on demare le timer
      arg=0
      self.OnTimerTimeout(arg) #on lance immediatemnt une fois 
      
    
  def OnTimerRefresh(self,b):
      print ('refresh')
      self.m_pTimer.Stop()
      self.browser.Show()
      self.browser.Reload(WEBVIEW_RELOAD_NO_CACHE)
      #self.browser.LoadURL("http://www.fxstreet.fr/rates/currency-rates/")
      self.m_pTimer.Start(1000);
     
      
  def OnTimerTimeout(self,b):
    if self.count == 10:
        self.count = 0
        #self.m_pTimer.Stop()
        print ("refresh")
        sendmail("browser stopped")
        print ("load")
        b=0
        OnTimerRefresh(b)
        #self.browser.Show() 
        #self.browser.LoadURL("http://www.fxstreet.fr/rates/currency-rates/")         
        return

    self.count  = self.count+1

    string = self.browser.GetPageText();
    sdecode = string.encode('raw_unicode_escape')
    #print '1'
    for s in sdecode.split("\n"):
        #print "!",s
        decoded =0
        for paire in analysepaires.paires:
            #print paire,s
            if s.find(paire) != -1:
                #print "3"
                if analysepaires.decode(s)==1 : #une valeur a change
                    self.count=0
                decoded =1
                continue
                
        if decoded ==1:
            continue
            
    #if self.count == 1:
    #    sendmail()

    


        
    
