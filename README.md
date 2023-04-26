# HomeGPT: Intelligent Home Assistant

HomeGPT Intelligent Home Assistant is an application that allows users to control their smart home devices using natural language commands. It uses OpenAI API, Flask framework, and MongoDB to analyze user's dialogues and control smart home switches.

## Introduction

HomeGPT Intelligent Home Assistant is an intelligent application that is used to control smart home devices using natural language dialogues.  It uses OpenAI API to generate artificial dialogues, Flask framework to build web applications and handle HTTP requests and responses, and MongoDB to store the state of smart home devices.
By analyzing the context of the conversation and learning from the user's behavior, HomeGPT can proactively identify the user's needs and take actions accordingly.

## Usage

### Requirements

- Python 3.8 or higher

### Installing Dependencies

Use pip to install dependencies:

```bash
pip install Flask pymongo openai
```

### Configuration

1. Create an account on the OpenAI website and generate an API key on the [API settings page](https://beta.openai.com/account/api-keys).

2. Open the `.env` file in the project directory and set the `OPENAI_API_KEY` variable to your OpenAI API key.

   ```makefile
   OPENAI_API_KEY=<your_openai_api_key>
   ```

3. Open the `config.py` file and set the MongoDB database URI.

   ```python
   MONGO_URI = "mongodb://localhost:27017/homegpt"
   ```

### Running the Application

Navigate to the project directory in the terminal and run the following command to start the application:

```bash
set FLASK_APP=main.py
flask run
```

The application will run on port 5000 on the local host. You can use your browser to access the application at `http://localhost:5000`.

### Controlling Smart Home Devices

You can test HomeGPT by using the following sample dialogues:

```
User: It was too dark in the room.
HomeGPT: (The light has been turned on)

User: I'm going to bed.
HomeGPT: (The light has been turned off and the curtain has been closed)

User: I'm very cold.
HomeGPT: (The air-conditioner has been opened)
```

## License

HomeGPT is released under the MIT License. See the `LICENSE` file for more details.