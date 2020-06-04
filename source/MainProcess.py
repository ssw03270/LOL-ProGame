#pyinstaller -w -i "icon.ico"  MainProcess.py

import AboutCsv
import GetWebPage
import Video

import sys
import urllib.request
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(
        "QWidget {background-color: rgb(30,30,30)} "
        "QLineEdit {background-color: rgb(107,107,107); color: rgb(200,200,200)}"
        "QLabel {color: rgb(200,200,200)}"
        "QPushButton {background-color: rgb(51,51,51); color: rgb(200,200,200)} "
        )
        self.init_ui()

    def init_ui(self):
        self.ErrorDialog = ErrorWindow()

        self.Scroll = QtWidgets.QScrollArea() 
        self.ScrollBar = QtWidgets.QScrollBar()
        self.Widget = QtWidgets.QWidget()
        
        #about GridLayout
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.setContentsMargins(50 , 50, 50, 50) 

        self.Object_Pos_H = 1
        self.Video_Pos_H = 0
        self.Label_01_List = [] #image
        self.Label_02_List = [] #title
        self.Label_03_List = [] #title(additional)
        self.ButtonList_Start = [] #start_btn
        self.ButtonList_Download = [] #download_btn
        self.NowPos = 0
        
        #about search area
        self.PushButton_reload = QtWidgets.QPushButton("Reload")
        self.LineEdit = QtWidgets.QLineEdit()
        self.PushButton_Search = QtWidgets.QPushButton("Search")
        self.PushButton_AllGame = QtWidgets.QPushButton("AllGame")
        self.GridLayout.addWidget(self.PushButton_reload, 0, 0, 1, 1)
        self.GridLayout.addWidget(self.LineEdit, 0, 1, 1, 7)
        self.GridLayout.addWidget(self.PushButton_Search, 0, 8, 1, 1)
        self.GridLayout.addWidget(self.PushButton_AllGame, 0, 9, 1, 1)
        self.SearchText = " "

        #about LineEdit (font)
        self.Font_LineEdit = self.LineEdit.font()
        self.Font_LineEdit.setPointSize(20)
        self.Font_LineEdit.setFamily('Times New Roman')
        self.LineEdit.setFont(self.Font_LineEdit)

        #about pushbutton_reload
        self.PushButton_reload.setFixedHeight(40)
        self.PushButton_reload.clicked.connect(self.pushbutton_reload)

        #about pushbutton_search
        self.PushButton_Search.setFixedHeight(40)
        self.PushButton_Search.clicked.connect(self.pushbutton_search)

        #about pushbutton_allgame
        self.PushButton_AllGame.setFixedHeight(40)
        self.PushButton_AllGame.clicked.connect(self.pushbutton_allgame)

        self.Widget.setLayout(self.GridLayout)

        self.Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scroll.setWidgetResizable(True)
        self.Scroll.setWidget(self.Widget)
        self.Scroll.setVerticalScrollBar(self.ScrollBar)

        self.ScrollBar.valueChanged.connect(self.scrollbar)

        self.setCentralWidget(self.Scroll)

        self.setWindowTitle("LOL - ProGame")
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.setGeometry(100, 100, 1100, 700)
    #if you click this button, open web page (lol video)
    def pushbutton_start(self):
        for i in range(0, self.NowPos):
            if(self.ButtonList_Start[i][0].isChecked()):
                webbrowser.open(self.ButtonList_Start[i][1])
                self.ButtonList_Start[i][0].setChecked(False)

    #if you click this button, downloading the video
    def pushbutton_download(self):
        for i in range(0, self.NowPos):
            if(self.ButtonList_Download[i][0].isChecked()):
                output = Video.VideoClass.download_video(Video.VideoClass, self.ButtonList_Start[i][1])
                if output == -1:
                    self.call_error_message("there is a error while\ndownloading video. please reload it.")
                self.ButtonList_Download[i][0].setChecked(False)

    #reload a web page and find a new video. this button will be remade soon
    def pushbutton_reload(self):
        #input_url = self.LineEdit_01.text()
        input_url = "https://www.youtube.com/user/KazaLoLLCSHighlights/videos"
        html_source = GetWebPage.WebClass.get_scrolled_html(GetWebPage.WebClass, input_url)
        soup = GetWebPage.WebClass.get_soup(GetWebPage.WebClass, html_source)
        raw_video = soup.find_all('ytd-grid-video-renderer', {'class' : 'style-scope ytd-grid-renderer'}) 
        video_list = Video.VideoClass.get_video_info(Video.VideoClass, raw_video)
        AboutCsv.CsvClass.input_csv(AboutCsv.CsvClass, video_list)
    
    #open new dialog if there is a error
    def call_error_message(self, error_text):
        self.ErrorDialog.set_error_message(error_text)
        self.ErrorDialog.show()
    
    #remove all widget in layout and search a new widget that match with search_text
    def pushbutton_search(self):
        self.delete_widget_single(self.Label_01_List)
        self.delete_widget_single(self.Label_02_List)
        self.delete_widget_single(self.Label_03_List)
        self.delete_widget_tuple(self.ButtonList_Start)
        self.delete_widget_tuple(self.ButtonList_Download)

        self.Object_Pos_H = 1
        self.Video_Pos_H = 0
        
        search_text = self.LineEdit.text()
        self.SearchText = search_text

        self.add_widget()

    #remove all widget in layout and set all video in layout
    def pushbutton_allgame(self):
        self.delete_widget_single(self.Label_01_List)
        self.delete_widget_single(self.Label_02_List)
        self.delete_widget_single(self.Label_03_List)
        self.delete_widget_tuple(self.ButtonList_Start)
        self.delete_widget_tuple(self.ButtonList_Download)

        self.Object_Pos_H = 1
        self.Video_Pos_H = 0
        
        search_text = ""
        self.SearchText = search_text

        self.add_widget()

    #deleting widget which is single value
    def delete_widget_single(self, widget_list):
        for widget in widget_list:
            self.GridLayout.removeWidget(widget)
            widget.deleteLater()
        widget_list.clear()
    #deleting widget which is tuple
    def delete_widget_tuple(self, widget_list):
        for widget in widget_list:
            self.GridLayout.removeWidget(widget[0])
            widget[0].deleteLater()
        widget_list.clear()

    #if you move scrollbar, this will be start and starting add widget
    def scrollbar(self):
        if self.ScrollBar.value() == self.ScrollBar.maximum():
            self.add_widget()
    
    #adding widget
    def add_widget(self):
        try:
            video_list = AboutCsv.CsvClass.get_csv(AboutCsv.CsvClass, "video_list.csv")#error here pyinstaller
        except:
            video_list = []
            self.call_error_message("there is a error while\ncalling video list. please reload it")

        max_video_number = len(video_list) - 1

        max_pos_h = self.Object_Pos_H + 10
        
        
        while(self.Video_Pos_H < max_video_number and self.Object_Pos_H < max_pos_h):
            video_info = video_list[self.Video_Pos_H]
            self.Video_Pos_H += 1

            if self.SearchText != " " and not self.SearchText.upper().replace(" ", "") in video_info[0].upper().replace(" ", ""):
                continue

            
            self.Label_01_List.append(QtWidgets.QLabel())
            self.Label_02_List.append(QtWidgets.QLabel(video_info[1]))
            self.Label_03_List.append(QtWidgets.QLabel(video_info[2]))
            self.ButtonList_Start.append((QtWidgets.QPushButton("Start"), video_info[3]))
            self.ButtonList_Download.append((QtWidgets.QPushButton("Download"), video_info[3]))

            self.NowPos = len(self.Label_01_List) - 1

            #about Label_01
            url_string = video_info[4]
            image_from_web = urllib.request.urlopen(url_string).read()
            self.QPixmapWebVar = QtGui.QPixmap()
            self.QPixmapWebVar.loadFromData(image_from_web)
            self.QPixmapWebVar = self.QPixmapWebVar.scaledToWidth(125)
            self.Label_01_List[self.NowPos].setPixmap(self.QPixmapWebVar)
            self.Label_01_List[self.NowPos].setContentsMargins(0 , 10, 0, 10) 

            #about Label_02
            self.Font_02 = self.Label_02_List[self.NowPos].font()
            self.Font_02.setPointSize(30)
            self.Font_02.setFamily('Times New Roman')
            self.Label_02_List[self.NowPos].setFont(self.Font_02)
            self.Label_02_List[self.NowPos].setFixedWidth(650)
            #self.Label_02.setStyleSheet("border-radius: 25px;border: 1px solid black;")
            
            #about Label_03
            self.Font_03 = self.Label_03_List[self.NowPos].font()
            self.Font_03.setPointSize(10)
            self.Font_03.setFamily('Times New Roman')
            self.Label_03_List[self.NowPos].setFont(self.Font_03)
            self.Label_03_List[self.NowPos].setFixedWidth(300)

            #about ButtonList_Start[H]
            self.ButtonList_Start[self.NowPos][0].setFixedHeight(60)
            self.ButtonList_Start[self.NowPos][0].setCheckable(True)
            self.ButtonList_Start[self.NowPos][0].clicked.connect(self.pushbutton_start)

            #about ButtonList_Download[H]
            self.ButtonList_Download[self.NowPos][0].setFixedHeight(60)
            self.ButtonList_Download[self.NowPos][0].setCheckable(True)
            self.ButtonList_Download[self.NowPos][0].clicked.connect(self.pushbutton_download)
            
            self.VBox = QtWidgets.QVBoxLayout()
            self.VBox.addStretch()
            self.VBox.addWidget(self.Label_02_List[self.NowPos])
            self.VBox.addWidget(self.Label_03_List[self.NowPos])
            self.VBox.addStretch()

            self.GridLayout.addWidget(self.Label_01_List[self.NowPos], self.Object_Pos_H, 0, 1, 1)
            self.GridLayout.addLayout(self.VBox, self.Object_Pos_H, 1 , 1, 7)
            self.GridLayout.addWidget(self.ButtonList_Start[self.NowPos][0], self.Object_Pos_H, 8, 1, 1)
            self.GridLayout.addWidget(self.ButtonList_Download[self.NowPos][0], self.Object_Pos_H, 9, 1, 1)
            self.Object_Pos_H += 1
            
class ErrorWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()  


    def init_ui(self):
        self.VBox = QtWidgets.QVBoxLayout()

        self.ErrorReport = QtWidgets.QLabel("ErrorMessage")
        self.EndBtn = QtWidgets.QPushButton("CLOSE IT")
        self.EndBtn.clicked.connect(self.end_button)

        self.VBox.addWidget(self.ErrorReport)
        self.VBox.addWidget(self.EndBtn)
        
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(self.VBox)
    
    def set_error_message(self, error_message):
        self.ErrorReport.setText(error_message)
    
    def end_button(self):
        self.close()



if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
        input()


