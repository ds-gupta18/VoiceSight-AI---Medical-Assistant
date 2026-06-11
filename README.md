# 🩺 VoiceSight AI - Medical Assistant

VoiceSight AI is an AI-powered Medical Assistant that allows users to interact using **voice and medical images**. The system listens to the user's voice, analyzes the uploaded medical image, generates an AI-powered medical response, and finally speaks the response back to the user.
This project demonstrates the integration of **Speech-to-Text, Computer Vision, Large Language Models, and Text-to-Speech** into a single healthcare-oriented application.

# Features
Voice Input from Microphone
Medical Image Upload
Speech-to-Text Conversion
AI-powered Medical Analysis
Medical Question Answering
Text-to-Speech Response
Interactive Gradio Interface

# Project Workflow

The application follows the following pipeline:
1. User uploads a medical image.
2. User asks a question using voice.
3. Speech is converted into text using Whisper.
4. The image and text are sent to the Vision AI model.
5. AI generates a medical response.
6. The response is converted into speech.
7. The response is displayed and played back to the user.

# Project Architecture

User Voice
↓
Speech-to-Text (Whisper)

Question Text
↓
Vision + Medical Analysis (Llama Vision)

Medical Response
↓
Text-to-Speech (gTTS)

Audio Response
↓
Gradio User Interface

# Project Structure

```text
VoiceSight-AI/
│
├── brain_of_the_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py
├── gradio_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Descriptions

# brain_of_the_doctor.py
Responsible for:
- Medical image analysis
- Prompt engineering
- AI response generation
- Communication with the Groq Vision Model

## voice_of_the_patient.py
Responsible for:
- Accepting patient voice input
- Speech-to-Text conversion
- Generating text transcripts

# voice_of_the_doctor.py
Responsible for:
- Converting AI responses into speech
- Generating MP3 output
- Audio playback support

# gradio_app.py
Responsible for:
- Building the user interface
- Connecting all modules
- Displaying outputs

### Technologies Used

# Programming Language
- Python

# AI Models
- Llama 4 Scout Vision
- Whisper Large v3

# Libraries
- Gradio
- gTTS
- Groq SDK
- Pillow
- Python-dotenv

### Prerequisites
Before running the project, make sure you have:
- Python 3.10+
- Groq API Key
- Internet Connection

### Installation

# Step 1: Clone Repository
```bash
git clone https://github.com/ds-gupta18/VoiceSight-AI---Medical-Assistant.git
```

# Step 2: Move into Project Folder
```bash
cd VoiceSight-AI---Medical-Assistant
```

# Step 3: Create Virtual Environment
Windows:
```bash
python -m venv .venv
```
Activate:

```bash
.venv\Scripts\activate
```

# Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

# Step 5: Add API Key
Create a file named:
```text
.env
```

Add:
```env
GROQ_API_KEY=your_api_key_here
```

# Step 6: Run Application
```bash
python gradio_app.py
```

### User Interface
The interface provides:

# Inputs
- Microphone Input
- Medical Image Upload

# Outputs
- Speech-to-Text Result
- Doctor's Response
- Doctor Voice Output

### Example Use Case

# User Input
Image: Acne affected skin

Voice Question:
```text
Doctor, what are these red spots on my face?
```

# AI Response
```text
Based on the image, the condition appears to be acne vulgaris.
Maintaining proper skincare and consulting a dermatologist is recommended.
```

# Voice Output
The response is automatically converted into speech and played back.

# Security Note
The following files are intentionally excluded from GitHub:
```text
.env
.venv/
*.mp3
*.wav
__pycache__/
```
This prevents accidental exposure of API keys and generated files.
