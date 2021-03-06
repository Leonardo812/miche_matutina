from music21 import note, stream, tempo

"""
Canciones
"""
Enemy_Approaching = [
    ['F4', 1.50], ['F4', 1.50], ['D4#', 1.50],
    ['D4#', 1.50], ['D4#', 3], ['F4', 1.50],
    ['F4', 1.50], ['F4', 1.50], ['E4', 1.50],
    ['D4', 1], ['C4', 1], ['F4', 1.50], ['F4', 1.50],
    ['D4#', 1.50], ['D4#', 1.50], ['D4#', 2],
    ['F4', 1.50], ['G4', 1.50], ['A4', 1.50], ['A4#', 0.50],
    ['C5', 2.50], ['D5', 2], ['A4#', 1.50], ['E4', 1.50],
    ['F4', 1], ['E4', 1.50], ['D4', 1], ['E4', 1.50],
    ['G4', 1], ['A4', 2], ['A4#', 1.50], ['G4', 2],
    ['D5', 1], ['C5', 2], ['D5', 2], ['A4#', 1.50], ['E4', 1.50],
    ['F4', 1], ['E4', 1.50], ['D4', 1], ['E4', 1],
    ['F4', 1], ['G4', 1], ['F4', 1], ['E4', 1.50],
    ['E4', 1], ['D4', 1], ['C4', 1], ['A3#', 1.50],
    ['D4', 1.50], ['E4', 1.50], ['C4', 1], ['A3', 1],
    ['D5', 2], ['A4#', 1.50], ['E4', 1.50],
    ['F4', 1], ['E4', 1.50], ['D4', 1], ['E4', 1],
    ['G4', 1], ['A4', 2], ['A4#', 1.50],
    ['G4', 1.5], ['D5', 1], ['C5', 2],
    ['D5', 2], ['A4#', 1.50], ['E4', 1.50],
    ['F4', 1], ['E4', 1.50], ['D4', 1], ['E4', 1],
    ['F4', 1], ['G4', 1], ['F4', 1], ['E4', 1.50],
    ['E4', 1], ['D4', 1], ['C4', 1], ['A3#', 1.50],
    ['D4', 1.50], ['E4', 1.50], ['C4', 1], ['A3', 1],
    ['G4#', 1.50], ['D4#', 1.50], ['G4#', 1.50],
    ['C5', 1], ['A4#', 1], ['G4#', 1], ['G4', 1],
    ['G4#', 1], ['F4', 2], ['F4', 2], ['E4', 1.50],
    ['F4', 1], ['G4', 3], ['G4#', 1.50],
    ['D4#', 1.50], ['G4#', 1.50],
    ['C5', 1], ['A4#', 1], ['G4#', 1], ['G4', 1],
    ['G4#', 1], ['A4#', 1.50], ['G4', 1.50], ['A4#', 1],
    ['D5', 1], ['C5', 2],
    ['G4#', 1.50], ['D4#', 1.50], ['G4#', 1.50],
    ['C5', 1], ['A4#', 1], ['G4#', 1], ['G4', 1],
    ['G4#', 1], ['F4', 2], ['F4', 2], ['E4', 1.50],
    ['F4', 1], ['G4', 3],
    ['G4#', 1.50], ['D4#', 1.50], ['G4#', 1.50],
    ['C5', 1], ['A4#', 1], ['G4#', 1], ['G4', 1],
    ['G4#', 1], ['A4#', 1], ['G4', 2], ['A4#', 1.50],
    ['D5', 1], ['C5', 1.50], ['A5', 1], ['A4#', 1],
    ['D5#', 1], ['D4#', 1], ['G5', 1], ['F5', 3]]


st = stream.Stream()
for i in range(2):
    for n in Enemy_Approaching:
        new_note = note.Note(n[0])
        new_note.duration.quarterLength = n[1]
        st.append(new_note)

st.insert(0, tempo.MetronomeMark(number=180))

st.write('midi', fp="musicaF.mid")
