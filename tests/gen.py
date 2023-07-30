from midiutil import MIDIFile

midi = MIDIFile(1)

#midi.addNote(track, channel, note, time, duration, volume)
midi.addNote(0, 1, 60, 0, 0.25, 100)
midi.addNote(0, 9, 10, 0.5, 0.25, 100)

with open("out.mid", "wb") as out:
    midi.writeFile(out)
