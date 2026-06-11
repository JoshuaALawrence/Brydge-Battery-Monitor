# 📡 Brydge Battery Monitor
*A lightweight Windows system tray app that shows your Brydge keyboard's battery percentage*

![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

![Brydge Battery Monitor tray icon](https://github.com/user-attachments/assets/9d18a24f-bd81-4b33-a612-a4159aebcc90)

## 🚀 Overview
Brydge Battery Monitor is a simple, efficient app that keeps track of your **Brydge keyboard's battery percentage**. It lives in the Windows system tray and updates its icon dynamically to reflect the current battery level, so you can check it at a glance.

It comes in two flavors:
- **AutoHotkey (`.ahk`)** – the original, lightweight version
- **Python (`.pyw`)** – a cross-checked port using `pystray`

## 🔧 Features
- ✅ **Real-time battery percentage** shown as the tray icon
- ✅ **Lightweight & minimal** – runs quietly in the background
- ✅ **No window, just a tray icon** (0–100% icons + an error icon)
- ✅ **Auto-refresh** every 60 seconds
- ✅ **Two implementations** – AutoHotkey or Python

## 🧩 How It Works
The app uses a PowerShell `Get-PnpDevice` query to find any connected **Brydge** device and read its battery level from the device's power property. The returned percentage is mapped to a matching icon in the `Icons/` folder (e.g. `87.ico`), which is then displayed in the system tray. If the battery level can't be read, an `error.ico` is shown instead.

## ✅ Requirements
- **Windows** (relies on PowerShell and the system tray)
- A connected **Brydge** keyboard
- For the AHK version: **AutoHotkey v1.1**
- For the Python version: **Python 3.10+**

## 🖥️ Installation

### 🔹 AHK Version
1. Download the latest release from [GitHub Releases](https://github.com/JoshuaALawrence/Brydge-Battery-Monitor/releases).
2. Make sure **AutoHotkey v1.1** is installed (download from [autohotkey.com](https://www.autohotkey.com/)).
3. Run `Brydge Battery Monitor.ahk` directly, or compile it to a standalone `.exe`.

> Keep the `Icons/` folder next to the script/executable so the tray icons can be found.

### 🔹 Python Version
1. Install Python 3.10+ from [python.org](https://www.python.org/).
2. Clone this repository:

   ```bash
   git clone https://github.com/JoshuaALawrence/Brydge-Battery-Monitor.git
   cd Brydge-Battery-Monitor
   ```

3. Install dependencies (`pystray` and `Pillow`):

   ```bash
   pip install -r Python/requirements.txt
   ```

4. Run the app (use `pythonw` so no console window appears):

   ```bash
   pythonw "Python/Brydge Battery Monitor.pyw"
   ```

## ⚙️ Usage
- The app runs in the background and updates the **system tray icon** to display the current battery percentage.
- **Right-click the tray icon** and choose **Exit** to quit.

## 📂 Project Structure
```
Brydge-Battery-Monitor/
├── Brydge Battery Monitor.ahk   # AutoHotkey version
├── Icons/                       # 0.ico–100.ico + error.ico
├── Python/
│   ├── Brydge Battery Monitor.pyw   # Python version
│   └── requirements.txt
├── LICENSE
└── README.md
```

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, fork the repo and submit a PR with your improvements.

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
🔋 *Keep track of your Brydge battery with ease!*
