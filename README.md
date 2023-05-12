# Work In Progress

## Setup

Install the required packages and libraries

```bash
pip install -r requirements.txt
```

Install ffmpeg on your platform and add it to your PATH

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Running

Running in development mode with hot reloading on port 3001:

```bash
uvicorn app:app --reload --port 3001
```

Running in production mode on port 3000:

```bash
uvicorn app:app --port 3000
```
