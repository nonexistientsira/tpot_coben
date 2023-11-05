# **TPOT COBEN**
This is a program that uses data given by [BracketCounter](https://github.com/figgyc/bracketcounter) to calculate COBEN based on data regarding BracketCounter's accuracy, as Bracket has been known to over/underestimate the counts by around 300, at most.<br>
Note that this, NOR BracketCounter can give accurate representations on who is going to be eliminated in TPOT *x*.
# How to Use + Setup
Open ```bfb_coben.py``` in Visual Studio Code or Notepad (any text/code editor)<br>
Edit the variables at the beginning to your desire (contestants, vote counts, margin of error (contestant_se), total simulations) (do note you would need to rename the variables if you want to change the characters, I'd recommend a find and replace tool to do this easily)
# Running the Code
There are two ways I've successfully tried running the code.<br>
**1. Visual Studio Code**<br>
a) Open the code with Visual Studio Code, then run it with the play button.<br>
**2. Command Prompt**<br>
Sometimes, I have an error! This is how I run it when that happens.<br>
a) Open cmd.exe<br>
b) Use ```cd``` to the path where ```bfb_coben.py``` is stored.<br>
c) Run ```python bfb_coben.py```<br>
