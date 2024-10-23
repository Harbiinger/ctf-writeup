---
title: "Electric Soldiers"
draft: false
tags: ["STEGANOGRAPHY"]
series: "deadface2024"
date: 2024-10-06
author: Harbiinger
---

## Challenge Description
>We stumbled across this image from d34th that might indicate how DEADFACE plans to sneak stolen information through various networks without detection. According to Ghost Town, d34th has been refining his process for embedding hidden information in various files.

>See if you can uncover any hidden information in this image. Submit the flag as flag{flag-text}.

## File 
![AI generated image of a robots' rock band](/deadface2024/electricsoldiers.png)

## Solution
In `GhostTown`, there is a thread by `d34th` titled `Steganography Script Update` that says
>I’ve finally managed to refine my steganography script to embed messages in MP3 files. Originally, I had a working version for WAV files, but the file sizes were too large and inconvenient. Embedding in MP3 files initially caused issues with the ID3 headers, but I’ve now resolved those problems. The script ensures the message is hidden in the least significant bits without corrupting the audio quality or metadata. Anyone interested in testing it out or providing feedback?

and: 
>I’ll post a link to it once it’s setup. I’ve had to do some troubleshooting. The header kept getting jacked up, so I padded the start of the hidden message with spaces and then just manually corrected the header in hexeditor.

By analysing the image with `binwalk` or `scalpel` we detect a mp3 header:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
-----------------------------------------------
1700017       0x19F0B1        MP3 ID3 tag, v2.4
```

Using a text editor we can delete everything until the ID3 tag. 
It gives us a mp3 file that can be listened to.
Given what we read on the forum we can now extract LSB from the mp3 file using a python script.

[lsb.py](/deadface2024/lsb.py)

Flag: flag{3l3ctr1c_s0ld13rs_4lw4ys_r0ck}
