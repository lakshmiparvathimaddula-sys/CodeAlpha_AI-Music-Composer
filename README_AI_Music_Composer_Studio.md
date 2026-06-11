#  AI Music Composer Studio

AI Music Composer Studio is an AI-powered music generation application that creates original melodies using Deep Learning and MIDI datasets. The project uses Python, TensorFlow, and Music21 to learn musical patterns from existing MIDI files and generate new compositions automatically. A Streamlit-based interface allows users to interact with the model and generate music easily.

---

#  Features

-  Train an AI model on MIDI music datasets
-  Generate original melodies and musical sequences
-  Deep Learning-based music composition using LSTM networks
-  Support for MIDI file processing
-  Automatic music pattern learning
-  Interactive Streamlit web interface
-  Save generated music as MIDI files
-  Data preprocessing and sequence generation
-  Real-time AI music generation

---

#  Technologies Used

- Python
- TensorFlow / Keras
- Music21
- NumPy
- Streamlit
- Pickle

---

#  Project Structure

```text
AI-Music-Composer-Studio/
│
├── dataset/
├── models/
│   └── music_model.h5
├── output/
│   └── generated.mid
├── preprocess.py
├── train.py
├── generate_music.py
├── app.py
├── notes.pkl
├── requirements.txt
└── README.md
```

---

#  Installation

```bash
git clone https://github.com/your-username/AI-Music-Composer-Studio.git
cd AI-Music-Composer-Studio
pip install -r requirements.txt
```

---

#  Dataset Preparation

Place MIDI files inside the dataset folder and run:

```bash
python preprocess.py
```

This creates:

```text
notes.pkl
```

---

#  Train the Model

```bash
python train.py
```

Output:

```text
models/music_model.h5
```

---

#  Generate Music

```bash
python generate_music.py
```

Output:

```text
output/generated.mid
```

---

#  Run the Application

```bash
streamlit run app.py
```

---

#  How It Works

1. Collect MIDI files.
2. Extract notes and chords using Music21.
3. Convert notes into sequences.
4. Train an LSTM model.
5. Generate new musical patterns.
6. Create a new MIDI composition.
7. Download and play generated music.

---

#  Future Enhancements

- Genre-based generation
- Mood-based music creation
- MP3/WAV export
- Transformer models
- Cloud deployment

---

#  License

MIT License

 Star this repository if you find it useful.
