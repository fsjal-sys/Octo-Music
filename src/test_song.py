from midiutil import MIDIFile

midi = MIDIFile(1)

#midi.addNote(track, channel, note, time, duration, volume)
midi.addNote(0, 9, 10, 0, 0.25, 100)
midi.addNote(0, 9, 10, 0.5, 0.25, 100)
midi.addNote(0, 9, 50, 0.8, 0.2, 100)
midi.addNote(0, 9, 50, 0.9, 0.2, 100)
midi.addNote(0, 9, 10, 1, 0.25, 100)                                                         
midi.addNote(0, 9, 10, 1.5, 0.25, 100)                                                       
midi.addNote(0, 9, 50, 1.8, 0.2, 100)                                                        
midi.addNote(0, 9, 50, 1.9, 0.2, 100)
midi.addNote(0, 9, 10, 2, 0.25, 100)                                                         
midi.addNote(0, 9, 10, 2.5, 0.25, 100)                                                       
midi.addNote(0, 9, 50, 2.8, 0.2, 100)                                                        
midi.addNote(0, 9, 50, 2.9, 0.2, 100)

with open("test_song.mid", "wb") as out:
    midi.writeFile(out)
