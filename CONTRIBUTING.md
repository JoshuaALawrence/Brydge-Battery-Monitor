# Contributing to Brydge Battery Monitor

Thanks for your interest in contributing! Brydge Battery Monitor is a small
Windows tray utility that shows a Brydge keyboard's battery percentage as a tray
icon. It ships in two implementations — an **AutoHotkey** script and a **Python**
port — that are kept in sync and behave the same way.

This document explains how to get set up and contribute effectively.

## Code of Conduct

This project and everyone participating in it is governed by our
[Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to
uphold it. Please report unacceptable behavior to the maintainer.

## Ways to Contribute

- **Report bugs** using the 🐛 [bug report template](https://github.com/JoshuaALawrence/Brydge-Battery-Monitor/issues/new/choose).
- **Suggest features** using the 💡 [feature request template](https://github.com/JoshuaALawrence/Brydge-Battery-Monitor/issues/new/choose).
- **Improve documentation** such as the `README.md`.
- **Submit code** via a pull request (see below).

Before starting significant work, please open an issue to discuss your idea so we
can avoid duplicated effort.

## Development Setup

### Requirements

- **Windows 10 or 11** (the app relies on PowerShell `Get-PnpDevice` and the
  Windows system tray).
- A connected **Brydge** keyboard that reports battery to Windows is helpful for
  real-world testing.
- For the AutoHotkey version: **AutoHotkey v1.1**.
- For the Python version: **Python 3.10+**.

### AutoHotkey version

1. Install [AutoHotkey v1.1](https://www.autohotkey.com/).
2. Run `Brydge Battery Monitor.ahk` directly.
3. Keep the `Icons/` folder next to the script so the tray icons load.

### Python version

1. Install [Python 3.10+](https://www.python.org/).
2. Install dependencies:

   ```bash
   pip install -r Python/requirements.txt
   ```

3. Run with `pythonw` so no console window appears:

   ```bash
   pythonw "Python/Brydge Battery Monitor.pyw"
   ```

## Making Changes

1. **Fork** the repository and create a branch from `main`:

   ```bash
   git checkout -b feat/my-improvement
   ```

2. Make your changes. **Keep both implementations in sync** — if you change
   behavior in the AutoHotkey version, apply the equivalent change to the Python
   version (and vice versa), or explain in your PR why they should differ.
3. Test your changes (see below).
4. Commit with a clear, descriptive message.
5. Push your branch and open a pull request.

## Testing Your Changes

There is no automated test suite, so please verify changes manually:

- The app starts without a visible window.
- The tray icon shows the correct battery percentage and updates over time
  (default refresh is every 60 seconds).
- The `error.ico` fallback appears when the battery can't be read (e.g. with the
  keyboard disconnected).
- **Right-click → Exit** cleanly closes the app.

In your pull request, please note the environment you tested on:

- Windows version
- Brydge keyboard model
- AutoHotkey and/or Python version

## Style Guidelines

- Keep the app **lightweight and dependency-light** — it should stay a quiet,
  no-fuss background utility.
- Match the existing code style in each implementation.
- Use clear, descriptive names and add brief comments where logic isn't obvious.
- Update the `README.md` when you change behavior, requirements, or the project
  layout.

## Pull Request Process

1. Fill out the [pull request template](.github/PULL_REQUEST_TEMPLATE.md)
   completely.
2. Link any related issues (e.g. "Closes #123").
3. Ensure your branch is up to date with `main`.
4. A maintainer will review your PR, may request changes, and will merge it once
   it's ready.

Thank you for helping make Brydge Battery Monitor better! 🔋
