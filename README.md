# Retrieval Augmented Generation (RAG)
# Miniconda Installation

Install a lightweight Conda distribution so you can manage Python versions and dependencies consistently across macOS, Linux, and Windows. Each platform section below references the official installers hosted at https://repo.anaconda.com/miniconda/.

## Prerequisites

- A shell with `bash` and `curl` available on macOS/Linux or `PowerShell` on Windows.
- At least **500 MB** of free space in your home directory (the default install path is `~/miniconda3`).
- A network connection that can reach https://repo.anaconda.com/miniconda/.

## macOS Installation

1. Create the installation directory:
   ```bash
   mkdir -p ~/miniconda3
   ```
2. Download the installer for your CPU architecture:
   - **Apple Silicon (arm64)**
     ```bash
     curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
     ```
   - **Intel (x86_64)**
     ```bash
     curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
     ```
3. Run the installer in silent mode:
   ```bash
   bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
   ```
4. Remove the installer script:
   ```bash
   rm ~/miniconda3/miniconda.sh
   ```
5. Activate Conda and initialize your shell configuration:
   ```bash
   source ~/miniconda3/bin/activate
   conda init
   ```
6. Restart your terminal to apply the shell changes.

## Linux Installation

1. Create the installation directory:
   ```bash
   mkdir -p ~/miniconda3
   ```
2. Download the installer that matches your CPU architecture:
   - **x86_64**
     ```bash
     curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda3/miniconda.sh
     ```
   - **ARM64 (aarch64)**
     ```bash
     curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -o ~/miniconda3/miniconda.sh
     ```
3. Run the installer in silent mode:
   ```bash
   bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
   ```
4. Remove the installer script:
   ```bash
   rm ~/miniconda3/miniconda.sh
   ```
5. Activate Conda and initialize your shell configuration:
   ```bash
   source ~/miniconda3/bin/activate
   conda init
   ```
6. Restart your terminal to pick up the new configuration.

## Windows Installation

### Option 1: Windows Installer (Recommended)

1. Download the graphical installer from https://repo.anaconda.com/miniconda/.
2. Run the installer and:
   - Choose **Just Me** unless you have administrator privileges.
   - Accept the default location or install under your user profile.
3. After the installer completes, open a new PowerShell or Anaconda Prompt and run:
   ```powershell
   conda init
   ```
4. Restart the terminal so the updated configuration takes effect.

### Option 2: Silent Install (Advanced)

1. Download the silent installer:
   ```powershell
   curl -o Miniconda3-latest-Windows-x86_64.exe https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
   ```
2. Install silently:
   ```powershell
   Start-Process .\Miniconda3-latest-Windows-x86_64.exe -ArgumentList "/S" -Wait
   ```
3. Initialize Conda and restart:
   ```powershell
   conda init
   ```

## Post-installation

- Run `conda activate base` after restarting to ensure your shell knows about Conda.
- Optionally disable the auto-activation of the base environment with `conda config --set auto_activate_base false` if you prefer to activate environments explicitly.

## Verify Installation

```bash
conda --version
```

## Project Setup

1. Create the project environment with Python 3.8 (or later if the project supports it):
   ```bash
   conda create -n mini-rag python=3.8
   ```
2. Activate the environment:
   ```bash
   conda activate mini-rag
   ```
3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the sample environment variables and edit them:
   ```bash
   cp .env.example .env
   # Then open .env and set values such as OPENAI_API_KEY
   ```
5. (Optional) Improve your prompt readability while the environment is active:
   ```bash
   export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
   ```
## Run the FastAPI server:

 ```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
   ```