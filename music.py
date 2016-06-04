from dt import DumplingTown
import soco

class Music(DumplingTown):

    def __init__(self):
        self.zones = list(soco.discover())
        self.base = self.zones[0]

    def pause(self):
        self.base.pause()

    def play(self):
        self.base.play()


