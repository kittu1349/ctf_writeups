import mido

letter_distribution = {
    'a': 5, 'b': 5, 'c': 5, 'd': 4, 'e': 6,
    'f': 5, 'g': 5, 'h': 4, 'i': 5, 'j': 5,
    'k': 5, 'l': 5, 'm': 5, 'n': 4, 'o': 4,
    'p': 5, 'q': 5, 'r': 5, 's': 6, 't': 5,
    'u': 3, 'v': 4, 'w': 5, 'x': 5, 'z': 5
}
def extract_note_numbers(filename):
    try:
        midi = mido.MidiFile(filename)
        note_numbers = []

        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    note_numbers.append(msg.note)

        if len(note_numbers) > 12:
            note_numbers = note_numbers[5:-7]
        return note_numbers
    except Exception as e:
        print(f"Error: {e}")
        return []


def assign_notes_to_letters(note_numbers, letter_distribution):
    assigned_data = {}
    index = 0  

    for letter, count in letter_distribution.items():
        if index >= len(note_numbers):
            break  # Stop if there are no more notes to assign
        assigned_data[letter] = note_numbers[index:index + count]
        index += count  # Move to the next set of notes

    return assigned_data

# Main function
def main():
    filename = "tune_868.midi"  
    note_numbers = extract_note_numbers(filename)
    print(f"Filtered note numbers (ignoring first 5 and last 7): {note_numbers}")
    assigned_data = assign_notes_to_letters(note_numbers, letter_distribution)
    print("\nAssigned note numbers to letters:")
    for letter, notes in assigned_data.items():
        print(f"{letter}: {notes}")

if __name__ == "__main__":
    main()
