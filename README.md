# 🪄 tuiwizard

**A lightweight, dependency-free Python library for creating simple Terminal User Interfaces (TUI).**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

`tuiwizard` allows you to turn boring console scripts into interactive terminal applications. It provides an ANSI-based rendering engine, interactive menus, progress bars, and visual effects without requiring any third-party libraries like `curses` or `rich`.

## ✨ Features

- **🎨 Renderer Engine:** Control cursor position, clear screens, and use 256-color palettes.
- **🖱️ Interactive Menus:** Create navigable menus using arrow keys (cross-platform support for Windows, Linux, and macOS).
- **📊 Widgets:** Built-in progress bars, text boxes, and a typewriter effect for text.
- **🌧️ Visual Effects:** Matrix rain effect and smooth fade-in transitions.
- **🪶 Zero Dependencies:** Built entirely on Python's standard library (`sys`, `os`, `time`, `msvcrt`, `termios`).

## 📦 Installation

Currently, the library is distributed as a source package. 

1. Download or clone this repository:
```bash
git clone https://github.com/rogovskoy/tuiwizard.git
```
2. Place the tuiwizard folder into the root directory of your project.
3. Import it in your Python script!

## 🚀 Quick Start

Here is a simple example of creating a centered menu with a typewriter effect:

```python
import tuiwizard as tw
import time

def main():
    # 1. Clear the terminal screen
    tw.Renderer.clear()
    
    # 2. Draw a box with a title
    tw.draw_box(x=10, y=2, width=40, height=10, title="SYSTEM BOOT", border_color=45)
    
    # 3. Print text with a typewriter effect
    tw.Renderer.move_cursor(12, 4)
    tw.typewriter("Initializing modules...", delay=0.05, color_code=82)
    
    # 4. Run an interactive menu (navigate with UP/DOWN arrows, select with ENTER)
    options = ["Start Application", "Settings", "Exit"]
    menu = tw.Menu(options, title="Main Menu")
    choice = menu.run(x=12, y=7)
    
    # 5. Handle the choice
    tw.Renderer.clear()
    tw.Renderer.move_cursor(10, 10)
    tw.typewriter(f"You selected: {choice}", delay=0.03, color_code=198)

if __name__ == "__main__":
    main()
```

## 📚 Modules Overview

The library is split into logical modules for better architecture:

· **tuiwizard.core**: The heart of the library.
  · Renderer: Manages ANSI codes (colors, cursor).
  · input: Handles raw keyboard input (including arrow keys).
· **tuiwizard.widgets**: Ready-to-use UI elements.
  · box: Draws ASCII/Unicode frames.
  · progress: Renders dynamic progress bars.
  · menu: Interactive selection menu.
  · text: Typewriter effect.
· **tuiwizard.effects**: Eye-candy.
  · matrix: Falling characters effect.
  · transition: Fade-in animations.

## ⚠️ Important Notes

· Terminal Compatibility: tuiwizard relies on ANSI escape codes. It works perfectly in VS Code Terminal, Windows Terminal, PowerShell, and all Unix-like terminals. It may not work correctly in the legacy Windows cmd.exe.
· Terminal Size: If your terminal window is too small, the boxes and menus might overlap or break. Use tw.get_terminal_size() to dynamically adjust your layouts.

## 👨‍💻 Author

(c) 2026 Platon Rogovskoy
**GitHub**: @rogovskoy

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.