import sqlite3
import mido

# allows support for retrieving the Midi information from a database
def retrieve_midi_information():
    # Connect to the SQLite database
    connection = sqlite3.connect('midi_database.db')
    cursor = connection.cursor()

    # Retrieve MIDI information from the database
    cursor.execute('SELECT * FROM midi_files')
    midi_files = cursor.fetchall()

    # Process retrieved MIDI information
    for midi_file in midi_files:
        file_name, artist, duration, tempo, key = midi_file

        # Print MIDI information
        print(f"File Name: {file_name}")
        print(f"Artist: {artist}")
        print(f"Duration: {duration} seconds")
        print(f"Tempo: {tempo} BPM")
        print(f"Key: {key}")
        print()

        # Load and process the MIDI file
        midi_data = mido.MidiFile(file_name)
        # Add your code here to work with the MIDI data

    # Close the database connection
    connection.close()