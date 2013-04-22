daytime
=========

This module extends the datetime.time-module and makes it more handy
respectivly to comparison, addition and substraction.
You can compare, add and substract a daytime with another daytime, a
datetime.time-object or an int or float as total amount of seconds.
Making sums is also possible with a datetime.timedelta.



Latest Version
--------------
The latest version of this project can be found at : http://github.com/thomst/daytime.


Installation
------------
* Option 1 : Install via pip ::

    pip install daytime

* Option 2 : If you have downloaded the source ::

    python setup.py install


Documentation
-------------
How to use? ::

    from daytime import DayTime
    import datetime

    daytime1 = DayTime(2, 20, 23, 90000)
    daytime2 = DayTime(12, 25, 0, 8400)

    daytime1 - daytime2                 # DayTime(13, 55, 23, 81600)
    daytime2 + datetime.time(22,3,4,5)  # DayTime(10, 28, 4, 8405)
    daytime1 - 12400                    # DayTime(22, 53, 43, 90000)

    daytime1 < daytime2                 # True
    daytime2 > 4800                     # True

    DayTime.utcfromtimestamp(24000.4)   # DayTime(6, 40, 0, 400000)


Reporting Bugs
--------------
Please report bugs at github issue tracker:
https://github.com/thomst/daytime/issues


Author
------
thomst <thomaslfuss@gmx.de>
Thomas Leichtfuß

* http://github.com/thomst
