# Python script for batch resizing textures

## Setup

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Single file

```
python3 src/main.py input_image.tif
```

### Directory

```
python3 src/main.py ./directory
```

Resized images will be located in `/out` after processing is done
