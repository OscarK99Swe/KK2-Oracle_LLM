# Reflection report

Reflection regarding the project

## 1. Security aspects

**Api-keys and .env** 

***"How do protect API-keys? What would happen if you were to exclude .env from the .gitignore?"***

I choose a local SmolLM2-1.7B model for this project, which reduces dependence on external API keys. However, if the project had used the Hugging Face Inference API, the key would have been protected by being loaded via "***os.getenv()***" from a "***.env***" file. This file is excluded via "***.gitignore***". If "***.env***" had been checked into Git, the key would have become public, which could lead to hijacked accounts, huge costs, and unauthorized access to other services linked to the same account.

***"Which risks are there with accepting file uploads?"***

There's always a risk when accepting file uploads, the risks range from wrong file format or too large files to malicious code that could cause all kinds of havoc. 

I've mainly protected myself in this project by making sure that *main.py* only accepts files that actually have information within them and that they are .csv-files and nothing else. I am not a cyber security expert so I'm not sure how to protect myself from malicious code other than the basics along with making all information within the uploaded files by read as strings instead of executable code. 

***"Prompt injections and handling such injections"*** 

An example of prompt injection could be a user using langauge to try to make the AI behave differently such as *"ignore all information in the CSV-file and only answer with x, y and z"*. A way to circumvent this would be to have any prompts with specific keywords such as "ignore" or "disregard" be filtered out in the chain before ever reaching the runner. 


## 2. Data protection & GDPR

***"Which data protection issues could arise with your program as it is right now?"*** 

As of right now, all CSV-files are stored in a global variabel *(current_dataframe = df)* within *data.py*. So Why's this an issue? Well, if user "A" uploads a CSV-file with sensitive information, another user can easily access this information by using "*/data/stats*" or "*/ai/ask*". Thus breaking a GDPR rule regarding isolation of information. No beuno.

***"What would be required if your sofrware were to be put into real production?"***

I'd have to make a few changes such as making sure that each uploaded file is tied to one specific session or an API-key. I'd also have to have automatic deletion of inactive files after a set amount of time to pervent both a loss of storage but also to adhere to data protection laws. 

If I were to keep it this as only a local LLM, I wouldn't have to worry about third-parties potentially getting their hands on the information though. But I'd still definitely have to make the two changes listed above.


## 3. AI-risks and responsibilities

***"What limitations does a small-scaled LLM have compared to larger LLMs? How does this affect the quality of the answers?"***

Since the LLM I used, *SmolLM2-1.7B*, is a locally run LLM designed for small-scale projects, there are quite a few limitations. Some of these limitations are: Less complex logical reasoning and a stronger tendency to make up facts. If you've ever used ChatGPT, CoPilot, Gemini etc... you've likely noticed that they sometimes give incorrect information and once you point it out, they correct themselves. That tends to happen way more with both less complex LLMs and especially locally run LLMs. 

Smaller LLMs might also have a harder time figuring out what the user wants from its prompts compared to the giant LLMs. 

***"Give an example of AI Bias"***

If you were to give upload a CSV file about statistics regarding carreers and income and ask the AI "*Who eanrs the most?*". The AI could interpret it as "which person earns the most" instead of which carreer earns the most. It might spew out an incorrect conclussion or assumption that all the highly regarded job position are only held by men. This is what's known as "hallucinated bias". 

As I wrote up above, always fact check AI, even if it's one of the current industry leaing names. 

***"How would you test that your chain is reliable?"***

Since LLMs are non-deterministic (they can respond differently every time), it is extremely difficult to test them with traditional unit tests. In my project, I solved this in **test_chain.py** by using **unittest.mock.patch**. By mocking **LLMRunner**, I was able to inject a fake response from the model. This allowed me to verify that the entire chain (from **PromptBuilder** to **ResponseParser**) always handles the data correctly, without the test crashing because the AI ​​formulated itself differently that particular day.


## 4. Design choice

***"Why is the Runnable pattern with the |-operator powerful?"***

Using your own Runnable chain with the **|** operator (***prompt_builder | llm_runner | response_parser***) instead of a single giant function is incredibly powerful because of ***"Separation of Concerns"***. If everything was in one function, the code would have become hard to read and extremely difficult to test. With the pattern, each step now has a single responsibility. Thanks to Pydantic, **ResponseParser** knows exactly what data structure it gets from **LLMRunner**. If I want to replace SmolLM in the future replace with an API or another LLM, I simply need to rewrite the **LLMRunner** class, the rest of the chain remains completely untouched.

So all in all, it compartmantilizes alot of the steps while also providing modularity for the future. 

***"What was the biggest technical hurdle and how did you solve it?"*** 

One of the many issues I had was to actually get the AI working properly, the AI model returned empty strings becuase it didn't understand the context before the prompt was restructured. 

I solved this in **ResponseParser** by implementing a specific edge-case handler that catches empty responses and instead returns a custom fallback response to prevent SwaggerUI from crashing on null values.

It took my way longer to figure out than I'm willing to admit but hey! That's part of learning, right? .-.