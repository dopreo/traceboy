# traceboy
![Screenshot_20250403_212930](https://github.com/user-attachments/assets/40276502-65a1-4def-9e37-061292c69d5a)

Traceboy is a **super simple Python script for sidetone**.

It spawns a quick little Qt6 window that lets you press '**Start Sidetone**' to start sidetone, and '**Stop Sidetone**', to stop sidetone.

It takes its mic input from your **default system mic**, and streams it out of your system's **default sound output** (speakers, headphones, etc.).

--

## Installation
![Screenshot_20250403_212907](https://github.com/user-attachments/assets/3b7cc780-54fd-4853-b029-c69b3e05cd54)

*You'll likely need to **make a Python venv (virtual environment)** that you can activate, then **install theese Python packages inside that**.*

*The likes of **Linux desktops** often have Python **warn against installing random packages to your system Python installation** for obvious reasons.*

--

You'll just need to grab the following Python packages:
- **`sounddevice`** (```pip install sounddevice```)
- **`numpy`** (```pip install numpy```)
- **`scipy`** (```pip install scipy```)
- **`PyQt6`** (```pip install PyQt6```)

and make sure that a package called **`portaudio`** is installed on your host system:
- Example for Arch Linux and derivatives: ```sudo pacman -S portaudio```

--

### Example commands for setting up dependencies on Ubuntu
This should be about everything you need:

```sudo apt install python3-pyaudio libportaudio2```

```pip install sounddevice numpy pyqt6```

--

## Usage

- Run **`main.py`**, the main script:

  - ```cd traceboy```

  - ```python3 main.py```

--

## Known issues

- It is **a little temperemental when closing** if this is interrupting a test, or, to a lesser degree, a sidetone stream
- There is **no built-in visual indicator** to display **when the Repeat After Me test is recording** and playing back sound

--

## Contributing

- Simply **fork the repo**, **make your changes** and **open up a pull request** if there's something you think you can improve. **Thank you** in advance! :D
- Help me pay for meds and car insurance: https://ko-fi.com/oreohive

--

## Licensing

- This is an [**oreohive project**](https://www.oreohive.org/onboarding).
- This code and software is distributed under the [oreohive Source No-AI-Training License](https://oreohive.org/onboarding).
- Use of this code is governed by the [oreohive Source No-AI-Training License](https://oreohive.org/onboarding) (of most recent publication by the oreohive organisation)

copyleft 🄯 **oreo**  @ **oreohive.org** | **attributions are required**!
