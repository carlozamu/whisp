# Whisp: A Command-Line Wrapper for OpenAI Whisper Transcription

## 1. Abstract

Whisp is a lightweight command-line interface (CLI) wrapper script designed to streamline the audio transcription process using OpenAI's Whisper model. It provides a globally accessible command, enabling users to invoke transcription tasks from any directory within their terminal. The script is designed to accept single or multiple audio/video files, automatically concatenating and processing them into a single text output file, which is subsequently deposited on the user's Desktop for convenient access.

## 2. Core Functionality

* **Global Invocation:** Enables the `whisp` command to be executed from any system path, removing the need to navigate to the script's directory.
* **Batch Processing:** Accepts multiple file arguments. These files are concatenated in the order provided and transcribed sequentially as a single job.
* **Cross-Platform Support:** Provides distinct installation procedures for POSIX-compliant systems (macOS, Linux) and Windows.
* **Standardized Output:** All transcriptions are saved as `.txt` files directly to the user's Desktop, ensuring a predictable and accessible location for output.

## 3. System Requirements

Prior to installation, the host system must be equipped with the following dependencies:

1.  **Python 3.7+:** Must be installed and accessible from the system's PATH (verify with `python3 --version` or `python --version`).
2.  **ffmpeg:** A complete installation is required by Whisper for audio/video decoding and processing (verify with `ffmpeg -version`).
3.  **OpenAI Whisper:** The core Python package (verify with `pip show openai-whisper` or `whisper --version`). If not installed, run: `pip install openai-whisper`.

## 4. System-Wide Installation Procedure

Download the `whisp.py` script from this repository and follow the procedure corresponding to your operating system.

### 4.1. macOS / Linux (POSIX Systems)

The procedure for POSIX-compliant systems involves making the script executable and relocating it to a directory within the system's `PATH`.

**1. Script Preparation (Shebang Directive)**
Ensure the very first line of the `whisp.py` file is the shebang directive, which instructs the shell on which interpreter to use:
```bash
#!/usr/bin/env python3
```

**2. Relocation and Renaming**
Relocate the script to a standard binary path, such as `/usr/local/bin`, removing its `.py` extension to allow for direct command invocation.

```bash
# Example: Move script from Downloads to the binary path
sudo mv ~/Downloads/whisp.py /usr/local/bin/whisp
```

**3. Set Execution Permissions**
The script must be marked as executable to be run as a command.

```bash
sudo chmod +x /usr/local/bin/whisp
```

**4. Verification**
To apply the changes, **initiate a new terminal session**. Verify the installation by executing the command without arguments:

```bash
whisp
```
A successful installation will display the script's usage help message.

### 4.2. Windows

The Windows installation utilizes a `.bat` wrapper file and requires modification of the user's `PATH` environment variable.

**1. Directory Creation**
Establish a dedicated directory for user scripts. This location must be stable.
*Example:* `C:\Scripts`

Place the `whisp.py` file within this directory (`C:\Scripts\whisp.py`).

**2. Wrapper Script Creation**
In the *same* directory (`C:\Scripts`), create a new file named `whisp.bat`. This file will act as the wrapper that invokes the Python script.

Populate `whisp.bat` with the following content:
```batch
@echo off
python C:\Scripts\whisp.py %*
```
*Note: This assumes `python` is in your system PATH. Adjust the path `C:\Scripts\whisp.py` if you used a different location.*

**3. Environment Variable Modification (PATH)**
The `C:\Scripts` directory must be added to the user's `Path` environment variable to make the `whisp.bat` file globally discoverable.

1.  Press `Win + R`, type `sysdm.cpl`, and press Enter.
2.  Navigate to the "Advanced" tab and click "Environment Variables...".
3.  In the "User variables" section, select the `Path` variable and click "Edit...".
4.  Click "New" and add the full path to your scripts directory: `C:\Scripts`
5.  Click "OK" on all open dialogs to save the changes.

**4. Verification**
To load the new `PATH` variable, **all open Command Prompt or PowerShell instances must be closed and reopened**. Verify the installation by executing:

```bash
whisp
```
A successful installation will display the script's usage help message.

## 5. Operational Usage

Once installed, `whisp` can be invoked from any terminal location.

### 5.1. Single File Transcription
Provide the path to a single audio or video file.

```bash
whisp path/to/my_audio.m4a
```

### 5.2. Multi-File Concatenation and Transcription
Provide paths to multiple files. The script will process them in the order provided.

```bash
whisp lecture_part1.mp3 lecture_part2.mp3 lecture_part3.mp4
```

### 5.3. Output
The resulting transcription is saved as a `.txt` file on the user's **Desktop**. The output filename is derived from the *first* file argument provided.

*Example:* `whisp lecture_part1.mp3 lecture_part2.mp3` will generate `lecture_part1.txt` on the Desktop.

## 6. Configuration

The Whisper model used for transcription is hard-coded within the `whisp.py` script for simplicity.

* **Default Model:** `base.en`

To utilize a different model (e.g., `medium`, `large-v3`) or a multilingual model (e.g., `base`, `medium`), the `whisp.py` script must be **edited directly**. Locate the model variable assignment and change its string value to the desired model name.

## 7. Troubleshooting and Diagnostics

### 7.1. Error: `whisp: command not found` (macOS/Linux)

1.  **Path and Permissions:** Verify the file exists and is executable. Run `ls -l /usr/local/bin/whisp`. The permissions string must include `x` (e.g., `-rwxr-xr-x`). If not, re-run `sudo chmod +x`.
2.  **PATH Variable:** Ensure `/usr/local/bin` is part of the `echo $PATH` output. If it is missing, add `export PATH="/usr/local/bin:$PATH"` to your `~/.zshrc` or `~/.bash_profile` and restart the shell.
3.  **Shell Session:** Ensure you have started a new terminal session after the installation.

### 7.2. Error: `'whisp' is not recognized...` (Windows)

1.  **Terminal Restart:** This error most frequently occurs if the terminal (CMD/PowerShell) was not restarted after modifying the `PATH` environment variable.
2.  **PATH Verification:** In a *new* terminal, execute `echo %PATH%` and confirm that `C:\Scripts` is listed. If not, revisit section 4.2, Step 3.
3.  **File Location:** Confirm that both `whisp.py` and `whisp.bat` exist in the `C:\Scripts` directory.

### 7.3. Error: `ModuleNotFoundError` or `ffmpeg: not found`

These errors indicate that a core dependency is either not installed or not accessible from the system's `PATH`. Refer to the **Section 3. System Requirements** and verify the installation and accessibility of Python, `openai-whisper`, and `ffmpeg`.

## 8. License

This project is distributed under the MIT License. See the `LICENSE` file for details.
