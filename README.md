# ***KK2-Oracle_LLM***

KK2 *"kunskapskontrol 2"* or in english, *"knowledge check 2"*, is a school project combining a locally run LLM along with a RESTApi using FastAPI and python for CSV-file analysis combined and finished off with SwaggerUI as the optional frontend

*note: I'm using a Windows 11 machine for the instructions down below, your mileage may vary if you're using a different operating system...*

#### ***Requirements***

In order to run the software, you'll need the following: 

- An IDE *(I personally used Visual Studio Code)*
- Python 3.14.4 *(or newer depending on when you view this)* 
- An internet connection *(it'll download the roughly 2gb SmolLM needed for the AI functiunality)*
- Web browser *(optional, but it allows you to use the SwaggerUI frontend)*
- Atleast 5gb of available space *(2-3gb is enough, but better safe than sorry so I'm putting this here so you can't sue me :D )*

#### ***Setup***

1. Download or clone the repo into an easily accesible folder on your computer

2. Open the commandterminal in your IDE *(for VSC, you can use the shortcut "LCTRL + Ö" if you're on a standard Nordic ISO layout keyboard, otherwise use "LCTRL + `")*

3. Create your own virtual environment using the command: **uv venv** and hit enter. Wait for the terminal to show that you're in the venv.

4. download and sync all dependencies by using **uv sync**. If you wish to run the tests, you might have to run **uv add pytest --dev**.

5. It's time to start the server! Do so by running the command **uv run uvicorn app.main:app --reload**

Congratulations! everything should be running smoothly now.