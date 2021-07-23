# MetaDump

A discord bot for dumping the metadata of images and videos for all images placed in a channel

## Requirements

### 1

Install the python requirements from the requirements.txt

> pip install -r requirements.txt

### 2

Install [ffmpeg](https://ffmpeg.org/download.html) as this included ffprobe which is required to get video metadata.

### 3

Place your [discord bot token](https://www.writebots.com/discord-bot-token/) in a an .env file

.env File Contents:
```
TOKEN = "TOKEN GOES HERE"
CHANNEL = "TARGET CHANNEL GOES HERE"
```