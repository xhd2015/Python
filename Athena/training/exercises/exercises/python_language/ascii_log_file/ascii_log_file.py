""" 
ASCII Log File
--------------

Read in a set of logs from an ASCII file.

Read in the logs found in the file `short_logs.crv`.
The logs are arranged as follows::

    DEPTH    S-SONIC    P-SONIC ...
    8922.0   171.7472   86.5657
    8922.5   171.7398   86.5638
    8923.0   171.7325   86.5619
    8923.5   171.7287   86.5600
    ...

So the first line is a list of log names for each column of numbers.
The columns are the log values for the given log.    

Make a dictionary with keys as the log names and values as the
log data::

    >>> logs['DEPTH']
    [8922.0, 8922.5, 8923.0, ...]
    >>> logs['S-SONIC']
    [171.7472, 171.7398, 171.7325, ...]

Bonus
~~~~~

Time your example using::

    run -t 'ascii_log_file.py'
            
And see if you can come up with a faster solution. You may want to try the
`long_logs.crv` file in this same directory for timing, as it is much larger
than the `short_logs.crv` file. As a hint, reading the data portion of the array
in at one time combined with strided slicing of lists is useful here.

Bonus Bonus
~~~~~~~~~~~

Make your example a function so that it can be used in later parts of the class
to read in log files::
    
        def read_crv(file_name):                    
            ...
                    
Copy it to the class_lib directory so that it is callable by all your other
scripts.

See :ref:`ascii-log-file-solution1` and :ref:`ascii-log-file-solution2`.

"""             
log_file = open('short_logs.crv')
