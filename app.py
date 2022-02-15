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


class MainMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        self.InitUI(parent)

    def InitUI(self, parent):

        connection_button = wx.Button(self,
                                      label='\nSTATUS: CONNECTED\n',
                                      pos=(225, 20),
                                      size=(300, 30))

        connection_button.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD))

        im = wx.Image('assets/img/myo_band.jpeg', wx.BITMAP_TYPE_ANY)
        im.Rescale(300, 250)
        image = wx.StaticBitmap(self, -1, wx.Bitmap(im), pos=(90, 80))

        translate_gesture_button = wx.Button(self,
                                             label='\nTRANSLATE\n',
                                             pos=(40, 360),
                                             size=(200, 100))
        #translate_gesture_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTranslating(event, self))
        translate_gesture_button.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD))

        manage_gestures_button = wx.Button(self,
                                           label='\nMANAGE GESTURES\n',
                                           pos=(275, 360),
                                           size=(200, 100))
        #manage_geatures_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTraining(event, self))
        manage_gestures_button.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD))

        settings_button = wx.Button(self,
                                    label='\nSETTINGS\n',
                                    pos=(510, 360),
                                    size=(200, 100))
        #settings_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTraining(event, self))
        settings_button.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD))

        close_button = wx.Button(self,
                                 label='\nCLOSE\n',
                                 pos=(665, 525),
                                 size=(70, 30))
        #settings_button.Bind(wx.EVT_BUTTON, lambda event, parent=parent: parent.onTraining(event, self))
        close_button.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_BOLD))


def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
