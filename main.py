# main.py

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

import sounddevice as sd
import numpy as numpy
import scipy.io.wavfile as wav

from sidetone import start_sidetone, run_sidetone, stop_sidetone

import pyaudio
#   bindings for PortAudio, which must be 
#   installed on system
#   (PortAudio is not a Python package)

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

# establish PyQt6 GUI
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traceboy Sidetone")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.test_button = QPushButton("Test (Repeat After Me, 5 sec recording then playback)")
        self.test_button.clicked.connect(self.repeat_after_me_test)
        layout.addWidget(self.test_button)

        self.start_button = QPushButton("Start Sidetone")
        self.start_button.clicked.connect(run_sidetone)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Sidetone")
        self.stop_button.clicked.connect(stop_sidetone)
        layout.addWidget(self.stop_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    # test feature that records from user's mic and plays it back to them
    def repeat_after_me_test(self):
        duration = 5
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype="float64")
        print("recording audio!")
        sd.wait()
        self.test_button.setStyleSheet("")
        print("audio recording complete, playing audio")
        sd.play(myrecording, fs)
        sd.wait()

        print("play complete!")
        self.test_button.setStyleSheet("")


    def closeEvent(self, event):
        # if window is closing, ensure we stop sidetone properly
        stop_sidetone()
        event.accept()  # let window close o/

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()