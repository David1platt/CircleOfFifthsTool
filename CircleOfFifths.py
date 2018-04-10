#! user/bin/env/python

import gi

from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

class CircleFifths:

    def __init__(self):
        self.it = 0
        self.major_circle = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
        self.sharps = ['0', '1', '2', '3', '4', '5', '6', '7', '0', '0', '0', '0']
        self.flats = ['0', '0', '0', '0', '0', '7', '6', '5', '4', '3', '2', '1']
        self.minor_circle = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'Bb', 'F', 'C', 'G', 'D']
        self.C_semi_tones = ['Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#', 'Fb', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'B#']
        self.builder = Gtk.Builder()
        self.builder.add_from_file('CircleofFifths.glade')
        self.builder.connect_signals(self)
        self.win = self.builder.get_object('window1')
        self.win.show()

    def find_third(self, root_note):
        for index, note in enumerate(self.C_semi_tones):
            print (index)
            if note == root_note:
                if index == len(self.C_semi_tones) - 2:
                    return self.C_semi_tones[1]
                elif index == len(self.C_semi_tones) - 1:
                    return self.C_semi_tones[2]
                else:
                    return self.C_semi_tones[index + 2]


    def find_maj_fifth(self, root_note):
        for index, note in enumerate(self.major_circle):
            if note == root_note:
                if index == len(self.major_circle) - 1:
                    return self.major_circle[1]
                else:
                    return self.major_circle[index + 1]

    def find_num_sharps(self, root_note):
        for i, note in enumerate(self.major_circle):
            if note == root_note:
                return self.sharps[i]


    def find_num_flats(self, root_note):
        for i, note in enumerate(self.major_circle):
            if note == root_note:
                return self.flats[i]

    def on_find_notes_clicked(self, button, data=None):
        #get input field, get labels
        self.entry = self.builder.get_object('entry')
        self.chord_third = self.builder.get_object('chord_third')
        self.chord_fifth = self.builder.get_object('chord_fifth')
        self.sharp = self.builder.get_object('sharp')
        self.flat = self.builder.get_object('flat')
        #convert input to a string
        input = self.entry.get_text()
        #set label values
        print(input)
        print(self.find_third(input))
        third = self.find_third(input)
        fifth = self.find_maj_fifth(input)
        shrp = self.find_num_sharps(input)
        flt = self.find_num_flats(input)
        self.chord_third.set_text(third)
        self.chord_fifth.set_text(fifth)
        self.sharp.set_text(shrp)
        self.flat.set_text(flt)

if __name__ == "__main__":
    main = CircleFifths()
    Gtk.main()
