# Python Amazing Game Engine

Introduction
------------
Pythonage is a game engine intended to inspire and encourage a new generation of young software developers. It is also a fun way to demonstrate coding in schools and colleges.

In the 1980s every home computer allowed youngsters to write fun games, providing them with easy access to creating graphics, reading keys and playing sounds. It was a golden age. Then computers began to be much more powerful and complex, lots of wonderful things also came along such as classes, interfaces, mice, image and sound files as well as the Internet. However knocking together a simple fun game for your mates to play suddenly became **harder!** Now you needed to know far more and usually needed special software to write a decent game.

Pythonage aims to kick back that clock by allowing you to write code in Python3 code that drives interactive graphics and sounds out through your web browser.

How do you do that?
-------------------
Your write your Python based upon an already existing class, which then gets run it on a Pythonage server. Starting the pythonage server can be as simple as tweaking a single file on your computer (**startpythonageserver.py**) so that it knows about your games class then running it using IDLE. You also need to make another small tweak to a web-page file (**index.html**) maybe using notepad so that it knows your game's name. Then when you open that web-page in your browser the your game starts running.

How does it work inside?
------------------------
Under the hood the browser when your web-page is opened it creates a two-way connection to your Pythonage server using a thing called websockets. Your code then starts running on the Pythonage server creating classes it uses to display graphics and play sounds etc, while doing this the underlying infrastructure creates and updates duplicate classes (doppelgangers) inside your browser that are written in a different language called JavaScript (that your not required to learn). It is these JavaScript classes that do the cool stuff for you at the browser end.   

Is it just for games?
---------------------
Well it is designed for that, but it could easily be applied or extended for other uses such as server monitoring, sharing information or controlling software interactively through a web-interface.

Amazing. how do I get started?
------------------------------
Once you download the project you will find it contains a documentation folder. Read the user guide in that folder for how to get the project installed. The project also provides a simple example that you can experiment with and modify. The next step after that would be to take a look at **pythonage_reference_guide.txt** which documents all the Pythonage classes you have available to play with.

So it runs in a browser, does that mean everyone can play it at once?
---------------------------------------------------------------------
Well each web-page that gets opened creates and runs its own **PPlayingGame** sub-class at the Pythonage server end, so yes lots of people can play at once; You can even write co-op or player-versus-player games but these are more challenging to write. Also you need to make sure that everyone is connecting to the same pythonage server, and also that the web-pages and other files that are part of the game are available to other computers from that computer using **http.server** or something. 
