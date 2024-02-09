from PySide2 import QtWidgets, QtGui, QtCore

class CustomTheme:
    themes = {
        "Dark Mode": """
            background-color: #1F1F1F;
            color: white;
        """,
        "Light Mode": """
            background-color: white;
            color: black;
        """
    }

    @staticmethod
    def apply_theme(widget, theme):
        widget.setStyleSheet(theme)

class SongPlayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Song Player")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet(CustomTheme.themes["Dark Mode"])  # Default theme

        self.create_widgets()

    def create_widgets(self):
        layout = QtWidgets.QVBoxLayout()

        self.song_list = QtWidgets.QListWidget()
        self.song_list.setStyleSheet("background-color: #121212; color: white;")
        self.song_list.addItems(song_dict.keys())
        self.song_list.itemDoubleClicked.connect(self.play_song)

        self.play_button = QtWidgets.QPushButton("Play")
        self.play_button.setStyleSheet("background-color: #388E3C; color: white;")
        self.play_button.clicked.connect(self.play_song)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.setStyleSheet("background-color: #D32F2F; color: white;")
        self.stop_button.clicked.connect(self.stop_song)

        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.setStyleSheet("background-color: #121212; color: white;")
        self.volume_slider.valueChanged.connect(self.change_volume)

        self.now_playing_label = QtWidgets.QLabel("Now Playing: None")
        self.now_playing_label.setStyleSheet("background-color: #1F1F1F; color: white;")

        layout.addWidget(QtWidgets.QLabel("<b>Select a song to play:</b>"))
        layout.addWidget(self.song_list)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.stop_button)

        layout.addLayout(button_layout)

        layout.addWidget(QtWidgets.QLabel("<b>Volume Control:</b>"))
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.now_playing_label)

        self.setLayout(layout)

    def play_song(self):
        selected_song = self.song_list.currentItem()
        if selected_song:
            song_name = selected_song.text()
            song_data = song_dict.get(song_name)
            if song_data:
                pygame.mixer.music.load(BytesIO(song_data))
                pygame.mixer.music.play(loops=-1)  # Play infinitely
                self.now_playing_label.setText(f"Now Playing: {song_name}")

    def stop_song(self):
        pygame.mixer.music.stop()
        self.now_playing_label.setText("Now Playing: None")

    def change_volume(self, value):
        volume = value / 100
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = SongPlayer()
    player.show()
    app.exec_()
