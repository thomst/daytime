import time
import datetime



class DayTime(datetime.time):
    """
    Compare, add or substract daytimes.
    
    This module extends the datetime.time-module and makes it more handy
    respectivly to comparison, addition and substraction.
    You can compare, add and substract a daytime-object with other daytime-objects
    or with an integer as the amount of seconds. You can also compare a daytime-
    with a datetime.time-object.

    Attributes:
        delta:          daytime as datetime.timedelta-instance
        total_seconds:  daytime in seconds as a float

    """

    def __init__(self, *args, **kwargs):
        """DayTime([hour[, minute[, second[, tzinfo]]]])
        """
        #TODO: __add__ doesn't support microseconds for now
        super(DayTime, self).__init__(*args, **kwargs)
        self._delta = datetime.timedelta(
            hours = self.hour,
            minutes = self.minute,
            seconds = self.second,
            )
        self._total_seconds = self._delta.total_seconds()

    @classmethod
    def from_struct_time(cls, struct_time):
        """
        Build a DayTime from a struct_time.
        
        Args:
            struct_time:    time.struct_time (see the reference of time-module)
        
        Returns a DayTime-object.

        """
        return cls(
            hour = struct_time.tm_hour,
            minute = struct_time.tm_min,
            second = struct_time.tm_sec
            )

    @classmethod
    def from_seconds(cls, sec, local=True):
        """
        Build a DayTime from seconds.

        Args:
            sec:    integer or float. Interpreted as total amount of seconds
                    since the epoch (see documentation of time-module).
                    (Mind that to get the localized time in seconds you need to
                    use time.time() - time.altzone.)
            local:  boolean that specifies whether time.localtime or time.gmtime
                    is used to construct the daytime.
        
        Returns a DayTime-object.

        """
        if local: struct_time = time.localtime(sec)
        else: struct_time = time.gmtime(sec)
        return cls.from_struct_time(struct_time)

    @classmethod
    def strptime(cls, string, format='%H:%M:%S'):
        """
        Build a DayTime from a string and a format.

        Args:
            string:     string parsed according to the specified format
            format:     defaults to '%H:%M:%S'.
                        See the library reference manual for formatting codes.
        
        Returns a DayTime-object.

        """
        return cls.from_struct_time(time.strptime(string, format))

    @property
    def delta(self):
        return self.delta

    @property
    def total_seconds(self):
        return self._total_seconds

    def __add__(self, other, sign=1):
        # TODO: doing sums with datetime.timedelta-objects
        if isinstance(other, int) or isinstance(other, float):
            seconds = self._total_seconds + sign * other
            return DayTime.from_seconds(seconds, False)
        elif isinstance(other, DayTime):
            seconds = self._total_seconds + sign * other._total_seconds
            return DayTime.from_seconds(seconds, False)
        else: raise TypeError("unsupported operator for DayTime and {0}".format(
            other.__class__.__name__))

    def __sub__(self, other):
        return self.__add__(other, -1)

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds > other
        else: return super(DayTime, self).__gt__(other)

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds >= other
        else: return super(DayTime, self).__ge__(other)

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds < other
        else: return super(DayTime, self).__lt__(other)

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds <= other
        else: return super(DayTime, self).__le__(other)

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds == other
        else: return super(DayTime, self).__eq__(other)

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._total_seconds != other
        else: return super(DayTime, self).__ne__(other)


