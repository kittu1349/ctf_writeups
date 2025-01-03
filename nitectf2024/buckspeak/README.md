# Buckspeak Solution

[Watch video solution](https://www.youtube.com/watch?v=MW-wGc_MMk4)

## Description

The description of the challenge was as follows:

> **Description:** Buckbeak is trying to say something deep but is frustrated as nobody bücking understands him. Can you help him out?

Along with a file called `bucking.wav` and a hint (which was the most helpful part).

From the hint, I concluded it contained some kind of **music encryption**. After researching, I found this link, which led me to an encryption tool based on the **Bücking Music Cipher**:

[https://legacy.wmich.edu/mus-theo/ciphers/bucking.html](https://legacy.wmich.edu/mus-theo/ciphers/bucking.html)

---

## Music Cipher Analysis

From the image provided on this website, you can see that each letter is assigned certain musical notes. When you input any string, it generates a tune as an output.
> ![image](https://github.com/user-attachments/assets/d6cf19d6-fa14-435f-9adc-2ffb225559b3)

What you’ll notice is that the initial and final parts of the tune generated by this tool and the challenge tune are very similar. The initial part is called **'anfang'** and the last part is **'finale'**.

I used the string `nite` as a test, and it generated this music sheet:
![Screenshot 2024-12-15 123259](https://github.com/user-attachments/assets/4e7a7137-8e40-4de1-a0f7-187e3217ac12)

---

## Decoding Process

### Step 1: Generating Notes

At that point, I didn’t know how to read music sheets, so I had to figure out how to correlate the letters to the notes using code.
The website has a function that allows you to download the generated tune.
So I generated a tune for all the alphabets (except `j` and `y`) and got the corresponding tunes.
![Screenshot 2024-12-15 123810](https://github.com/user-attachments/assets/b5307990-5435-4d2b-bd03-1d2fb6b0c427)

My logic was: what if the dots on the music sheets represent the note numbers output by the [Mido library](https://mido.readthedocs.io/en/latest/) in Python?

For testing, I used the generated tune for all alphabets and converted the dots on the music sheet into note numbers, using the Mido library.

### Step 2: Code to Extract Note Numbers

I wrote a Python script, `note_numbers.py`, to process the generated music sheet and extract the note numbers. I made the code ignore the first 5 and last 7 notes, as those were used for the **'anfang'** and **'finale'** parts of the tune.

This code gave me the following output:
```python
python .\note_number.py
Filtered note numbers (ignoring first 5 and last 7): [67, 71, 69, 72, 71, 79, 74, 71, 67, 67, 71, 74, 72, 76, 74, 67, 71, 69, 67, 76, 74, 72, 71, 69, 67, 71, 72, 74, 71, 67, 71, 67, 74, 71, 79, 76, 78, 79, 74, 79, 78, 76, 74, 72, 79, 78, 76, 74, 72, 74, 72, 72, 71, 71, 71, 67, 67, 71, 69, 76, 74, 76, 72, 74, 66, 69, 66, 62, 76, 73, 76, 69, 66, 67, 69, 66, 62, 71, 67, 66, 67, 69, 66, 64, 64, 62, 62, 67, 71, 69, 72, 71, 74, 71, 69, 71, 67, 69, 66, 67, 69, 78, 78, 76, 78, 79, 79, 78, 79, 74, 73, 74, 76, 73, 69, 81, 79, 78, 76, 74]

Assigned note numbers to letters:
a: [67, 71, 69, 72, 71]
b: [79, 74, 71, 67, 67]
c: [71, 74, 72, 76, 74]
d: [67, 71, 69, 67]
e: [76, 74, 72, 71, 69, 67]
f: [71, 72, 74, 71, 67]
g: [71, 67, 74, 71, 79]
h: [76, 78, 79, 74]
i: [79, 78, 76, 74, 72]
j: [79, 78, 76, 74, 72]
k: [74, 72, 72, 71, 71]
l: [71, 67, 67, 71, 69]
m: [76, 74, 76, 72, 74]
n: [66, 69, 66, 62]
o: [76, 73, 76, 69]
p: [66, 67, 69, 66, 62]
q: [71, 67, 66, 67, 69]
r: [66, 64, 64, 62, 62]
s: [67, 71, 69, 72, 71, 74]
t: [71, 69, 71, 67, 69]
u: [66, 67, 69]
v: [78, 78, 76, 78]
w: [79, 79, 78, 79, 74]
x: [73, 74, 76, 73, 69]
z: [81, 79, 78, 76, 74]
```
---
### Step 3: Validating the logic
To test if my logic was correct, I used the nite string tune generated by the online tool and passed it into another Python script. This script utilized the note distribution I obtained earlier to check if the logic held true.
```python
python .\detectletter.py
Filtered note numbers (ignoring first 5 and last 7): [66, 69, 66, 62, 79, 78, 76, 74, 72, 71, 69, 71, 67, 69, 76, 74, 72, 71, 69, 67]

Checking original sequence:
Match found for letter 'n' at index 0
Match found for letter 'i' at index 4
Match found for letter 'j' at index 4
Match found for letter 't' at index 9
Match found for letter 'e' at index 14

Concatenated letters from matches:
njte (this is actually nite, i talk about it later)
```
The output was as expected, confirming my approach.

---

## Converting .wav to .midi
Now, I needed to decode the actual bucking.wav file. To convert the .wav file into a .midi file, I used the following tool by Spotify:
https://basicpitch.spotify.com/

---

### Identifying Issues
An important thing to notice here is that there are certain letters that can be confused as the same by the code. These are:

`a and s
p and u
i and j`
This is because these letters have very similar note numbers in the .midi file. When the code detects these letters, it detects both at the same index.

---

## Decoding the MIDI file
Running the `bucking.py` code on the main `bucking.mid` file gave the following output:
```python
uasepuhraasetrueflanasreadtheookastohearasomethingdeepu
```
yay! we have a string!
At this point, using basic common sense, we can deduce that the original string is:
`usephrasetruefansreadthebookstohearsomethingdeep
`

**At this stage, I was stuck, so I raised a ticket with the challenge author. The author helped me realize that this was a passphrase for the original file.
But what tool could be used here?**

---

## The DeepSound Tool
Looking closely at the string, especially the part hearsomethingdeep, I remembered a tool from sound forensics called **DeepSound**.
Passphrase was: `truereadthebooks`
I used DeepSound to extract a hidden file from the bucking.wav file. The extracted files were:
![image](https://github.com/user-attachments/assets/a1c269fa-33f5-4348-98ca-e6afbce190be)
disclaimer.txt: An actual disclaimer.
screech.mkv: A suspicious file.

I inspected the `screech.mkv` file and found it contained two *OTF* files. Additionally, when playing the video, a weird subtitle appeared, which I exported and got the following text:
`'UnderstaNDAblE Buckbēaĸ SCRéècHiɳg-ɲoǐşēЅz'`

---

### Extracting Fonts
I used the following tool to extract the OTF files:
https://qgustavor.github.io/mkv-extract/en/
![Screenshot 2024-12-15 170743](https://github.com/user-attachments/assets/f555bca6-09cf-4fe5-b8ba-64c4d0fd0773)

After extracting the OTF files, I viewed them using an online OTF viewer. The file Buckbeak.otf contained some suspicious fonts.
![image](https://github.com/user-attachments/assets/154b8ce7-561a-4cf7-ada7-b3846717e51f)

Using the same online OTF viewer, I analyzed the weird subtitle and obtained the flag.
![image](https://github.com/user-attachments/assets/79b7ba43-2fc9-4fef-abe2-8ddca9a8f0a3)

*flag* => `nite{w3_b0th_kn0w_wh0_i5_ugly_h3r3_malf0y}`

---

***I plan to create a python code that directly deciphers an audio file from Bucking Music Cipher***
### That's all for now.. Thank you for reading the whole writeup ;>
