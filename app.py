import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Lectio Signum')
        self.main_menu = MainMenu(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.main_menu, 1, wx.EXPAND)
        self.SetSize((750, 600))
        self.Centre()
        self.Show()

    #close application
    def onBack(self, e):
        self.stop = True
        self.Close(True)

    #close application
    def onClose(self, e):
        self.stop = True
        self.Close(True)

    #start translate
    def onTranslate(self, e, parent):
        parent.Destroy()
        self.training = Training(self)
        self.sizer.Add(self.training, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

class Training(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.InitUI(parent)

    def InitUI(self, parent):

        connection_button = wx.Button(self, label='\nSTATUS: CONNECTED\n', pos=(225, 20), size=(300, 30))
        connection_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        im = wx.Image('assets/img/myo_band.jpeg', wx.BITMAP_TYPE_ANY)
        im.Rescale(300, 250)
        image = wx.StaticBitmap(self, -1, wx.Bitmap(im), pos=(90, 80))

        back_button = wx.Button(self, label='\nBACK\n', pos=(15, 525), size=(70, 30))
        back_button.Bind(wx.EVT_BUTTON, parent.onBack)
        back_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        close_button = wx.Button(self, label='\nCLOSE\n', pos=(665, 525), size=(70, 30))
        close_button.Bind(wx.EVT_BUTTON, parent.onClose)
        close_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))


class MainMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.InitUI(parent)

    def InitUI(self, parent):

        connection_button = wx.Button(self, label='\nSTATUS: CONNECTED\n', pos=(225, 20), size=(300, 30))
        connection_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        im = wx.Image('assets/img/myo_band.jpeg', wx.BITMAP_TYPE_ANY)
        im.Rescale(300, 250)
        image = wx.StaticBitmap(self, -1, wx.Bitmap(im), pos=(90, 80))

        translate_gesture_button = wx.Button(self, label='\nTRANSLATE\n', pos=(40, 360), size=(200, 100))
        translate_gesture_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTranslate(event, self))
        translate_gesture_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        manage_gestures_button = wx.Button(self, label='\nMANAGE GESTURES\n', pos=(275, 360), size=(200, 100))
        #manage_geatures_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTraining(event, self))
        manage_gestures_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        settings_button = wx.Button(self, label='\nSETTINGS\n', pos=(510, 360), size=(200, 100))
        #settings_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTraining(event, self))
        settings_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        close_button = wx.Button(self, label='\nCLOSE\n', pos=(665, 525), size=(70, 30))
        close_button.Bind(wx.EVT_BUTTON, parent.onClose)
        close_button.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))


def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
