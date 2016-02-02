
The file kica.py defines a function that is a Python+NumPy
translation of a couple lines of MATLAB code.  It is used in
unmix.py to solve the "cocktail problem", in which two microphones
simultaneous record two voices, and the goal is to separate the
voices.  The script unmix.py reads two files, mic1.wav and
mic2.wav, and produces unmix1.wav and unmix2.wav.

The script make_mixed_source.py generates the simulated microphone
recordings, so it must be run before running unmix.py.
