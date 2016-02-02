REM build the pi, time_extern, laplace, and sum extensions.
REM Note that the cython extensions don't need build_src
REM in their build command.

REM build pi example.
python setup_pi.py build_ext --inplace --compiler=mingw32

REM build time_extern example.
python setup_time_extern.py build_ext --inplace --compiler=mingw32

REM build laplace example.
python setup_laplace.py build_ext --inplace --compiler=mingw32

REM build sum example.
python setup_sum.py build_ext --inplace --compiler=mingw32
