import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.utils import to_categorical

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Create mapping
pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

sequence_length = 50

network_input = []
network_output = []

for i in range(0, len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[char] for char in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(pitchnames))

network_output = to_categorical(network_output)

# Build model
model = Sequential()

model.add(LSTM(
    256,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))
model.add(Dropout(0.3))

model.add(LSTM(256))
model.add(Dropout(0.3))

model.add(Dense(256, activation="relu"))
model.add(Dense(network_output.shape[1], activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

# Train model
model.fit(
    network_input,
    network_output,
    epochs=50,
    batch_size=64
)

# Save model
model.save("models/music_model.keras")

print("Model saved successfully!")