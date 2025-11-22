MIN_VOLUME = 0
MAX_VOLUME = 2
MIN_CHANNEL = 0
MAX_CHANNEL = 3
class Television:
    def __init__(self):
        self.__status=False
        self.__muted=False
        self.__volume=MIN_VOLUME
        self.__channel=MIN_CHANNEL

    def power(self):
        self.__status=not self.__status

    def mute(self):
        if self.__status:
            self.__muted=not self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel>=MAX_CHANNEL:
                self.__channel=MIN_CHANNEL
            else:
                self.__channel+=1

    def channel_down(self):
        if self.__status:
            if self.__channel<=MIN_CHANNEL:
                self.__channel=MAX_CHANNEL
            else:
                self.__channel-=1

    def volume_up(self):
        if self.__status:
            self.__muted=False
            if self.__volume<MAX_VOLUME:
                self.__volume+=1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume>MIN_VOLUME:
                self.__volume-=1

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}"