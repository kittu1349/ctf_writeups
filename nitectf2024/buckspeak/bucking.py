import mido

# Predefined letter-to-note combinations
letter_notes = {
    'a': [67, 71, 69, 72, 71],
    'b': [79, 74, 71, 67, 67],
    'c': [71, 74, 72, 76, 74],
    'd': [67, 71, 69, 67],
    'e': [76, 74, 72, 71, 69, 67],
    'f': [71, 72, 74, 71, 67],
    'g': [71, 67, 74, 71, 79],
    'h': [76, 78, 79, 74],
    'i': [79, 78, 76, 74, 72],
    'k': [74, 72, 72, 71, 71],
    'l': [71, 67, 67, 71, 69],
    'm': [76, 74, 76, 72, 74],
    'n': [66, 69, 66, 62],
    'o': [76, 73, 76, 69],
    'p': [66, 67, 69, 66, 62],
    'q': [71, 67, 66, 67, 69],
    'r': [66, 64, 64, 62, 62],
    's': [67, 71, 69, 72, 71, 74],
    't': [71, 69, 71, 67, 69],
    'u': [66, 67, 69],
    'v': [78, 78, 76, 78],
    'w': [79, 79, 78, 79, 74],
    'x': [73, 74, 76, 73, 69],
    'z': [81, 79, 78, 76, 74],
}

# Function to extract note numbers from a MIDI file
def extract_note_numbers(filename):
    try:
        midi = mido.MidiFile(filename)
        note_numbers = []

        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    note_numbers.append(msg.note)

        # Ignore the first 5 and last 7 notes
        if len(note_numbers) > 12:
            note_numbers = note_numbers[5:-7]

        return note_numbers
    except Exception as e:
        print(f"Error reading MIDI file: {e}")
        return []

# Function to find matching letters for note sequences
def find_matching_letters(note_numbers, letter_notes):
    result = ""

    # Check matches for the original note numbers
    print("\nChecking original sequence:")
    for i in range(len(note_numbers)):
        for letter, notes in letter_notes.items():
            # Check if the sequence of notes matches
            if note_numbers[i:i + len(notes)] == notes:
                print(f"Match found for letter '{letter}' at index {i}")
                result += letter

    return result

# Main function
def main():
    filename = "nite.midi"  
    note_numbers = extract_note_numbers(filename)
    print(f"Filtered note numbers (ignoring first 5 and last 7): {note_numbers}")
    concatenated_letters = find_matching_letters(note_numbers, letter_notes)
    print("\nConcatenated letters from matches:")
    print(concatenated_letters)

if __name__ == "__main__":
    main()
