# whisp-cli

Transcribe any audio or video file, right from your terminal. No more dragging files around.

`whisp` is a simple, lightweight wrapper for OpenAI Whisper that you install once and run from *any* folder on your system.

## Features

* **✨ Run Globally:** Just type `whisp audio.mp3` from *any* directory.
* **🔀 Combine Files:** Pass multiple files (`whisp part1.mp3 part2.mp3`) and get one single, combined transcription.
* **📂 Simple Output:** All transcriptions land neatly on your Desktop as a `.txt` file.
* **💻 Cross-Platform:** Simple, fast setup for macOS, Linux, and Windows.

---

## ✅ Prerequisites

Before you start, make sure you have these three things installed and working in your terminal:

1.  **Python 3.7+**
    * *Verify:* `python3 --version`
2.  **ffmpeg** (Whisper needs this!)
    * *Verify:* `ffmpeg -version`
    * *Install on Mac:* `brew install ffmpeg`
3.  **OpenAI Whisper**
    * *Verify:* `whisper --version`
    * *Install:* `pip install openai-whisper`

---

## 🚀 Quick Setup

Download `whisp.py` from this repo and follow the steps for your OS.

### 🍎 macOS / Linux

**1. Add Shebang (Crucial!)**

Make sure the **very first line** of your `whisp.py` file is:
```bash
#!/usr/bin/env python3
```

**2. Move & Make Executable**

Run these two commands to move the script to a global path and make it runnable.

```bash
# Move the file (and rename it to just 'whisp')
sudo mv ~/Downloads/whisp.py /usr/local/bin/whisp

# Give it execute permissions
sudo chmod +x /usr/local/bin/whisp
```

**3. Done!**

**Close and re-open your terminal.** Type `whisp` to verify.

### 🪟 Windows

**1. Create a Home for Your Scripts**

Make a simple folder, like `C:\Scripts`.

**2. Add `whisp.py`**

Place your `whisp.py` file inside `C:\Scripts`.

**3. Create the `whisp.bat` Wrapper**

In the *same* `C:\Scripts` folder, create a **new file** named `whisp.bat` and paste this in:

```batch
@echo off
python C:\Scripts\whisp.py %*
```
*(This file simply tells Windows to run your Python script.)*

**4. Add to PATH**

1.  Search for "Edit the system environment variables".
2.  Click "Environment Variables...".
3.  Under "User variables", find `Path`, click "Edit...".
4.  Click "New" and type `C:\Scripts`.
5.  Click OK on all windows.

**5. Done!**

**Completely close and re-open all terminal/CMD windows.** Type `whisp` to verify.

---

## 🎧 How to Use It

Using it is the easy part. Just call `whisp` followed by your file(s).

**Transcribe a single file:**
```bash
whisp my_lecture.m4a
```

**Combine and transcribe multiple files (in order):**
```bash
whisp part_1.mp3 part_2.wav part_3.mp4
```

**Output:** A `.txt` file (e.g., `my_lecture.txt`) will appear on your **Desktop**.

---

## 🔧 Customizing the Model

By default, `whisp` uses the fast `base.en` model.

Want more accuracy? Just **edit the `whisp.py` file** directly and change the `model_name` variable to `"medium"`, `"large-v3"`, etc.

---

## ⚠️ Quick Fixes

**`whisp: command not found` (Mac/Linux)**
* Did you **restart your terminal** after installing?
* Did you run `sudo chmod +x /usr/local/bin/whisp`?
* (Rare) Is `/usr/local/bin` missing from your `echo $PATH`?

**`'whisp' is not recognized...` (Windows)**
* Did you **restart your terminal**? This is the fix 99% of the time.
* Is `C:\Scripts` listed when you run `echo %PATH%`? If not, re-do Step 4.
* Are both `whisp.py` and `whisp.bat` inside `C:\Scripts`?

## 📄 License

MIT
