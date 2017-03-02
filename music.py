from dt import DumplingTown
import soco
from soco import SoCo
from soco.music_services import MusicService
from soco.compat import quote_url
from soco.data_structures import DidlItem, DidlResource
import datetime
import time

class Music(DumplingTown):
    AC_DAY = [
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #0
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #1
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #2
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #3
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #4
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #5
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #6
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #7
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #8
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #9
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #10
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #11
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #12
    "spotify:track:3CBYFS74b7464cdkyTweps", #13
    "spotify:track:3ccRHgbf0ddMNNgbvzMqFu", #14
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #15
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #16
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #17
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #18
    "spotify:track:1j340ksmPuIsO5LiCFlkDr", #19
    "spotify:track:4zif782JqWQN6e5QOD5Xva", #20
    "spotify:track:7Cf7D7Nic7hdgqlQjEjWbk", #21
    "spotify:track:7h0WwN0EEu9S2WTnzSOUBS", #22
    "spotify:track:40JpOYm5PshCptB5GDceCJ", #23
    "spotify:track:1j340ksmPuIsO5LiCFlkDr" #24
    ]

    def __init__(self):
    	self.device = SoCo("192.168.86.200")
    	self.service = MusicService("Spotify")

    def pause(self):
        self.device.pause()

    def play(self):
        self.device.play()

    def add_from_service(self, item_id, service, device, is_track=True):

        item_id = quote_url(item_id.encode('utf-8'))
        didl_item_id = "0fffffff{0}".format(item_id)

        # For an album:
        if not is_track:
            uri = 'x-rincon-cpcontainer:' + didl_item_id

        else:
            # For a track:
            uri = service.sonos_uri_from_id(item_id)

        res = [DidlResource(uri=uri, protocol_info="DUMMY")]
        didl = DidlItem(title="DUMMY",
            # This is ignored. Sonos gets the title from the item_id
            parent_id="DUMMY",  # Ditto
            item_id=didl_item_id,
            desc=service.desc,
            resources=res)

        device.add_to_queue(didl)
        device.play()

    def animalCrossingDay(self):
        now = datetime.datetime.now()
        hour = now.hour
        self.add_from_service(Music.AC_DAY[hour], self.service, self.device, True)
        while True:
            print datetime.datetime.now()
            print hour
            newHour = datetime.datetime.now().hour
            time.sleep(5*60)
            if newHour != hour:
                hour = newHour
                print "Queuing ",
                print hour
                self.add_from_service(Music.AC_DAY[hour], self.service, self.device, True)
