# ***KK2-Oracle_LLM***

KK2 *"kunskapskontrol 2"* or in english, *"knowledge check 2"*, is a school project combining a locally run LLM along with a RESTApi using FastAPI and python for CSV-file analysis combined and finished off with SwaggerUI as the optional frontend

*note: I'm using a Windows 11 machine for the instructions down below, your mileage may vary if you're using a different operating system...*

## ***Requirements***

In order to run the software, you'll need the following: 

- An IDE *(I personally used Visual Studio Code)*
- Python 3.14.4 *(or newer depending on when you view this)* 
- An internet connection *(it'll download the roughly 2gb SmolLM needed for the AI functiunality)*
- Web browser *(optional, but it allows you to use the SwaggerUI frontend)*
- Atleast 5gb of available space *(2-3gb is enough, but better safe than sorry so I'm putting this here so you can't sue me :D )*

## ***Setup***

1. Download or clone the repo into an easily accesible folder on your computer

2. Open the commandterminal in your IDE *(for VSC, you can use the shortcut "LCTRL + Ö" if you're on a standard Nordic ISO layout keyboard, otherwise use "LCTRL + `")*

3. Create your own virtual environment using the command: **uv venv** and hit enter. Wait for the terminal to show that you're in the venv.

4. download and sync all dependencies by using **uv sync**. If you wish to run the tests, you might have to run **uv add pytest --dev**.

5. It's time to start the server! Do so by running the command **uv run uvicorn app.main:app --reload**

Congratulations! everything should be running smoothly now. 
If by chance something isn't working, make sure that you've completed all the steps. 
If you have and it still isn't working... good luck I guess lol


### ***How to use the software***

#### ***Starting***

Once you've started the server using the command above in step number 5, you can now go ahead and go to the adress shown in the terminal. It was *"http://127.0.0.1:8000"* in my case, it might differ for you. 


#### ***Health Check***

Open that adress in a web browser of your choice, but to make sure that it's all working correctly, enter the health check first. go to "**ADRESS**/health". You should now see *{"status":"Sigma"}* if everything is working properly. 

Let's move onto the actual program now! go to "**ADRESS**/docs" now to get the frontend UI. You can also try out the health check from here if you'd like. Do so by simply pressing the "/health" line -> click "*try it out*" -> and hit the big button saying "*Execute*". You should now also be able to see the status of "Sigma". 


#### ***Uploading your CSV-file***

While being in the SwaggerUI, click the second horizontal bar from tap called "*POST/data/upload*"

Hit "*Try it out*" -> Select a local CSV-file from your device *(or the  provided "***test1.csv***" file within the"**dummy-data**" folder)* -> Hit execute

Alternative method: if you prefer to use the terminal, you can use the terminal command:

 *curl -X POST http://127.0.0.1:8000/data/upload \
  -F "file=@YOUR_FILE_PATH_&_FILE.csv"*


  #### ***Viewing statistics of your CSV-file***

  Same as before, but now we hit the third horizontal bar from the top, namely the "Get Stats".

  Next step is the *"Try it out"* and *"Execute"*

  You should see all available statistic of your CSV file now. 

  Alternative method for terminal nerds: 

  *curl -X GET http://127.0.0.1:8000/data/stats \
  -H "accept: application/json"*

   #### ***Asking the AI About your file***

Now for the fun part! 

Same steps as before, select "Ask Oracle" from the four horizontal bars, hit "*Try it out*" -> replace the word "***String***" within the request body with your question/AI prompt and hit execute. 

This step might take a while since this is when and where the SmolLM will start downloading to your system. Once it's downloaded, the prompt itself might take a minute or two depending on your CPU and its performance.

Alternative method: 

*curl -X POST http://127.0.0.1:8000/ai/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "YOUR_PROMPT"}'*

  ### ***Congratulations!***

  You've now succesfully gone through the entire program! Thank you for trying it out! :)