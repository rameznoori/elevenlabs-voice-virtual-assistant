
# ElevenLabs Conversational AI Client

This Python project demonstrates an integration with ElevenLabs’ Conversational AI platform. It initializes a conversation session configured with a custom user schedule and greeting prompt. The application uses environment variables to securely load API credentials, communicates with an AI agent identified by an agent ID, and prints both agent responses and user transcripts in real time. The setup uses ElevenLabs’ Python SDK with audio interface support for interactive dialogue sessions.

## Features

- Connects to ElevenLabs Conversational AI service using API key and agent ID
- Configurable conversation prompt including user schedule and greetings
- Prints agent responses, corrected truncated responses, and transcripts of user speech
- Uses ElevenLabs’ default audio interface for handling audio I/O
- Supports interruption and correction callbacks for agent speech
- Secure loading of credentials via environment variables (`.env` file)

## Getting Started / Installation

- Ensure Python 3.7 or later is installed.
- Install required libraries via pip:
    ```
    pip install elevenlabs elevenlabs[pyaudio] python-dotenv
    ```
- For Linux and MacOS, audio processing requires additional dependencies, install them as follows:
    ```
    For MacOS:
        brew install portaudio

    For Linux:
        sudo apt install portaudio19
    ```
- Obtain your ElevenLabs API key and Agent ID from the ElevenLabs platform.
- Create a `.env` file in the project folder:
    ```
    API_KEY=your_elevenlabs_api_key
    AGENT_ID=your_conversational_agent_id
    ```
- Download the Python script and run it:
    ```
    python virtual_assistant.py
    ```
- The conversation session will start, printing interaction logs to the console.

## Usage Instructions

- Run the script to start the AI conversation session.
- The agent will use the provided schedule and greeting prompts.
- User speech transcripts and agent responses are printed live.
- Use this as a basis for building voice-interactive AI applications.


## Technologies Used

- **Python 3.x**
- **ElevenLabs Python SDK** for Conversational AI
- **python-dotenv** for environment variable management
- **ElevenLabs DefaultAudioInterface** for audio I/O handling
## File Structure

```
/
├── virtual_assistant.py       # Main Python script managing conversational AI session
├── .env                       # Environment variables storing API credentials
├── README.md                   # This documentation file
```
## Customization

- Change `user_name` and `schedule` variables to tailor agent prompts.
- Modify callback functions to handle responses differently (e.g., GUI display).
- Extend with custom audio interfaces or additional conversation settings via `ConversationConfig`.
- Integrate with microphone input or audio playback for real voice interaction.
## Known Issues / Limitations

- Requires valid ElevenLabs API key and active conversational agent.
- Script currently prints outputs to console; no GUI included.
- Assumes audio hardware and permissions are correctly set on host machine.
- Limited error handling; network or auth failures need to be managed externally.
## Future Improvements

- Add GUI or web frontend for user-friendly interaction.
- Implement voice-to-text input and playback of agent responses.
- Support multi-user conversations or personalized agent behavior.
- Enhance error handling and logging mechanisms.
- Integrate with scheduling APIs or calendar apps for dynamic scheduling.
## Contributing

Contributions are always welcome!

- Fork the repository.
- Create feature branches for new functionality.
- Document code thoroughly.
- Submit pull requests with detailed descriptions.
## License

This project is open-source under the MIT License.
## Acknowledgements

 - ElevenLabs team for providing accessible Conversational AI APIs and SDKs.
- python-dotenv developers for secure configuration loading.
- Open source community resources supporting AI and Python development.