# 🎙️ AI Voice Assistant (Speech + ChatGPT)

A Python-based **AI voice assistant** that listens to user commands, processes them using an AI model, and responds with natural speech. The system supports both **voice interaction** and **text-based fallback mode**.

---

## 🚀 Features

* 🎤 Speech-to-Text (Voice Input)
* 🤖 AI-powered responses (OpenAI)
* 🔊 Text-to-Speech Output
* 💬 Text-based interaction mode
* ⚡ Real-time conversation loop

---

## 🧠 System Architecture

```
User (Voice/Text)
        ↓
Speech Recognition (Google API)
        ↓
Text Input
        ↓
OpenAI Model (Response Generation)
        ↓
Text Output
        ↓
Text-to-Speech (pyttsx3)
        ↓
Audio Response to User
```

---

## ⚙️ Tech Stack

* **Python**
* **SpeechRecognition** → Converts voice to text
* **pyttsx3** → Converts text to speech
* **OpenAI API** → Generates responses
* **OpenCV** → Used for key interrupt handling

---

## 📦 Installation

Install required libraries:

```bash
pip install pyttsx3 SpeechRecognition openai opencv-python
```

---

## ▶️ Usage

Run the script:

```bash
python your_script_name.py
```

### Steps:

1. Enter your OpenAI API key
2. Choose interaction mode:

   * `1` → Voice Mode
   * `2` → Quit

---

## 🎮 Controls

| Action                 | Command         |
| ---------------------- | --------------- |
| Stop voice interaction | Say **"stop"**  |
| Quit program           | Press **'q'**   |
| Exit text mode         | Type **"stop"** |

---

## 🔄 Workflow

1. User speaks into microphone
2. Speech is converted to text
3. Text is sent to AI model
4. AI generates response
5. Response is spoken back to user

---

## 📊 Example Interaction

```
User: What is artificial intelligence?
Assistant: Artificial intelligence is the simulation of human intelligence in machines...
```

---

## ⚠️ Notes

* Requires **internet connection** for speech recognition & AI response
* Microphone access must be enabled
* Works best in low-noise environments

---

## 🔮 Future Improvements

* Add GUI (Tkinter / Streamlit)
* Add wake-word detection ("Hey Assistant")
* Use advanced models (GPT-4 / newer APIs)
* Add multilingual support
* Store conversation history

---

## 👩‍💻 Author

**Ananya Sharma**

---


