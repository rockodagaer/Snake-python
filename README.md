# Snake-python
This is a cool template for snake, it uses cubes and you only need one file.

Items used to make: -----------------------

Its made using the closed beta version of openAI Codex and the full released version of github copilot

- openAI Codex
- openAI GPT-3-DAVINCI-2 --- code generation / idea generation
- openAI GPT-3-Codex --- code generation
- openAI GPT-3-Codex-EDIT --- code fixing
- openAI GPT-3-INSERT --- code adding
- Visual Studio Code --- coding

Bugs: -------------------------------------

There is a bug that could be a problem if you want to go really fast, this is that sometimes you cant do quick button presses
For example if you are going left and you press up right inside of one frame it will spawn inside itself in the next frame
So it will die and you need to restart

Theres another really rare bug that if you move while going through a wall it should normally just spawn you on the other size
But if you move while your inside the wall it will move outside the screen and in some situations it will move some of your snakes parts on random locations of the screen
But this is a really rare bug and will never happend, the one listed above is much more likely

It will sometimes miss button presses if there are more than one buttons pressed inside one frame.
This is a problem for quick-time button presses because it will only use the last pressed button
This is also what causes a bug that kills you when you move to the other side really fast

Theres a change you will die if a fruit spawns while touching a wall and you eat it.



Tips: -------------------------------------

Tip: theres a glitch that if you use a grid size higher than 20 the eyes can look bad
To fix this you can go to the cubes class and go to draw and set eyes to false when you draw it

Tip: this works better without debug mode. I recogment making a file named run.bat and writing "python main.py" inside of it to provent missing key presses
