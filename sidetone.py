import sounddevice as sd
import numpy as np
import threading

fs = 44100
duration = 5
channels = 2
sd.default.samplerate = fs
sd.default.channels = 2

stop_event = threading.Event()
sidetone_thread = None # this is where we'll store our thread!

def callback(input_data, output_data, frames, time, status):
    if status:
        print("STATUS:", status)
    output_data[:] = input_data

def start_sidetone():
    with sd.Stream(samplerate=fs, channels=channels, callback=callback):
        print("SIDETONE STREAMING! Press Ctrl+C to exit.")
        while not stop_event.is_set():
                sd.sleep(1000) # ms
        print("Exiting stream...")
        print("\nSidetone streaming stopped. Thank you!")

def run_sidetone():
    global sidetone_thread
    stop_event.clear()
    sidetone_thread = threading.Thread(target=start_sidetone)
    sidetone_thread.start()

def stop_sidetone():
    print("Stopping sidetone...")
    stop_event.set()
    if sidetone_thread is not None:
        sidetone_thread.join() # wait for thread to clean up
    sd.stop()
    print("Sidetone stopped!")