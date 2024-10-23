---
title: "Descended From Wolves"
draft: false
tags: ["STEGANOGRAPHY"]
series: "deadface2024"
date: 2024-10-06
---

## Challenge Description
>There’s an image circulating on GhostTown of some weird dog. Based on the conversation in the forum, it sounds like the image holds some data that lamia415 extracted from De Monne Financial. Use the context in the conversation to determine what was extracted.

>Submit the flag as flag{flag-text}.

## File 
![Image of a dog with big eyes](/deadface2024/princess.png)

## Solution
In `GhostTown`, there is a thread titled `Exfiltrating Data Without Triggering Alerts` that says

>Hey everyone, I just pulled off a sweet exfiltration from my company without setting off any security alerts. Sent a simple PNG of my dog, and no one suspected a thing!

>This is the image I used. He’s standing over his dog bowl in the original image.

This post implies that the image has been cropped but maybe the data has not been deleted. 

If we read the PNG specification from: http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html
we see that each PNG file must start with a IHDR header:

```
3.1 PNG file signature

The first eight bytes of a PNG file always contain the following values:

   (decimal)              137  80  78  71  13  10  26  10
   (hexadecimal)           89  50  4e  47  0d  0a  1a  0a
   (ASCII C notation)    \211   P   N   G  \r  \n \032 \n

This signature indicates that the remainder of the file contains a single PNG image, consisting of a series of chunks beginning with an IHDR chunk and ending with an IEND chunk. 

3.2 Chunk layout

Each chunk consists of four parts:

Length
    A 4-byte unsigned integer giving the number of bytes in the chunk's data field. The length counts only the data field, not itself, the chunk type code, or the CRC. Zero is a valid length. Although encoders and decoders should treat the length as unsigned, its value must not exceed 231 bytes.

Chunk Type
    A 4-byte chunk type code. For convenience in description and in examining PNG files, type codes are restricted to consist of uppercase and lowercase ASCII letters (A-Z and a-z, or 65-90 and 97-122 decimal). However, encoders and decoders must treat the codes as fixed binary values, not character strings. For example, it would not be correct to represent the type code IDAT by the EBCDIC equivalents of those letters. Additional naming conventions for chunk types are discussed in the next section.

Chunk Data
    The data bytes appropriate to the chunk type, if any. This field can be of zero length.

CRC
    A 4-byte CRC (Cyclic Redundancy Check) calculated on the preceding bytes in the chunk, including the chunk type code and chunk data fields, but not including the length field. The CRC is always present, even for chunks containing no data. See CRC algorithm.

The chunk data length can be any number of bytes up to the maximum; therefore, implementors cannot assume that chunks are aligned on any boundaries larger than bytes.

Chunks can appear in any order, subject to the restrictions placed on each chunk type. (One notable restriction is that IHDR must appear first and IEND must appear last; thus the IEND chunk serves as an end-of-file marker.) Multiple chunks of the same type can appear, but only if specifically permitted for that type. 

```

We need to find the block that contains the height (733) of the image and modify it. Then recalculate the CRC.

![HexDump of the image](/deadface2024/descendedFromWolves-1.png)
The highlighted bytes correspond to 1024 733. 
Let's change 02 dd to 04 dd. 
We need to calculate the new CRC: 

```
import zlib

ihdr_data = bytes.fromhex('4948445200000400000004dd0803000000')
crc = zlib.crc32(ihdr_data) & 0xffffffff
print(f'{crc:08X}')
```
which gives us: 23 C4 EA CE 

We can now replace the bytes and render the image: 

![CyberChef recipe for rendering the image](/deadface2024/descendedFromWolves-2.png)

Full image:
![Image of the dog with the flag written on its bowl](/deadface2024/descendedFromWolves-3.png)


Flag: flag{th3_h4ndsom3st_b01_1n_th3_w0rld}


