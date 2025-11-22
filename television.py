
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """
        Method to set default values of television object.
        """
        self.__status=False
        self.__muted=False
        self.__volume=Television.MIN_VOLUME
        self.__channel=Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the TV power.
        """
        self.__status=not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status if TV is on.
        """
        if self.__status:
            self.__muted=not self.__muted

    def channel_up(self) -> None:
        """
        Increments the channel by 1, changes to minimum if at max when called
        """
        if self.__status:
            if self.__channel>=Television.MAX_CHANNEL:
                self.__channel=Television.MIN_CHANNEL
            else:
                self.__channel+=1

    def channel_down(self) -> None:
        """
        Decrements the channel by 1, changes to max if at minimum when called
        """
        if self.__status:
            if self.__channel<=Television.MIN_CHANNEL:
                self.__channel=Television.MAX_CHANNEL
            else:
                self.__channel-=1

    def volume_up(self) -> None:
        """
        Increments the volume by 1 and resets mute status, volume remains unchanged if called at max.
        """
        if self.__status:
            self.__muted=False
            if self.__volume<Television.MAX_VOLUME:
                self.__volume+=1

    def volume_down(self) -> None:
        """
        Decrements the volume by 1 and resets mute status, volume remains unchanged if called at min.
        """
        if self.__status:
            self.__muted = False
            if self.__volume>Television.MIN_VOLUME:
                self.__volume-=1

    def __str__(self) -> str:
        """
        Generates string of current TV statuses if object is called.
        :return: Status of power, channel, and volume as a string.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume}"