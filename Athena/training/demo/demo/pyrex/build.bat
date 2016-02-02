REM build the pi, laplace, and sum extensions.
REM Note that the pyrex extensions don't need build_src
REM in their build command.

REM build pi example.
setup_pi.py build_ext --inplace --compiler=mingw32

REM build laplace example.
setup_laplace.py build_ext --inplace --compiler=mingw32

REM build sum example.
setup_sum.py build_ext --inplace --compiler=mingw32