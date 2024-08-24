
### Setup Environment
Install these libraries:
- tkinter
- requests
- pandas
- flask
```
	pip install library
```

Clone the repository (download as it is).
In flask.py change the host attribute at line 32 to your computer's IP, do the same at line 131 in main.py as well.

### How to run
- Run flask.py and let it run in any terminal.
```
	python3 flask_server.py
```
- Open another terminal, and run main.py in it
```
	python main.py
```
- A GUI window named Hues and Cues will open.
- Visit your IP address in a browser.
- Keep the flask server running in the background.
- Don't open the excel file while main.py is running and also don't shut the flask server.

### How to Play
- Click restart at first and reload the browser to see the color to guess.
- Show this color to any of the 2 teammates and then let him verbally describe it to the other person.
- Open the GUI and let the second teammate make the best guess by choosing any color on the grid.
- Click evaluate to know the answer.
- If it's correct, then enter the details - name, insta handle, number.
- Else they lose, and the actual color is shown.
- Each time before a new game, click the restart button to ensure a new game and reload to see the color change to confirm the game has restarted.


