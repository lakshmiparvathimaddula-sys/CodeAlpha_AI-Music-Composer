import streamlit as st
import os

st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 AI Music Composer")
st.write("Generate AI-created MIDI music using a trained LSTM model.")

if st.button("Generate Music"):

    with st.spinner("Generating music..."):
        os.system("python generate_music.py")

    st.success("Music generated successfully!")

    midi_file = "output/generated_music.mid"

    if os.path.exists(midi_file):
        with open(midi_file, "rb") as file:
            st.download_button(
                label="⬇ Download MIDI File",
                data=file,
                file_name="generated_music.mid",
                mime="audio/midi"
            )