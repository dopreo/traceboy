# traceboy

Traceboy is a **super simple Python script for sidetone**.

It spawns a quick little Qt6 window that lets you press '**Start Sidetone**' to start sidetone, and '**Stop Sidetone**', to stop sidetone.

It takes its mic input from your **default system mic**, and streams it out of your system's **default sound output** (speakers, headphones, etc.).

--

## Installation

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

- This is an [**oreohive project**](https://www.oreohive.org/onboarding), so use of this code is governed by [the oreohive organisation's **Terms & Ethics of Use**](https://www.oreohive.org/onboarding).
- This mainly means that (**1**.) you **cannot use it to violate anyone else's rights**, and (**2**.) you **cannot use it to train or improve AI models**.
- That said, **we release this code under** [the **GNU AGPL-3.0**](https://www.gnu.org/licenses/agpl-3.0.en.html), so **you are free to share it and redistribute it as you see fit**, providing you abide by these **two main rules** and the GNU AGPL-3.0 license.

--

```
You can redistribute and/or modify this program under the terms of the
GNU Affero General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version, providing
you maintain and uphold compliance with the oreohive organisation's Terms &
Ethics of Use.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY — without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE — to the extent permitted by applicable laws.  See the GNU
Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see https://www.gnu.org/licenses.
```

--

copyleft 🄯 2025 **oreo**  @ **oreohive.org** | **attributions are required**!
