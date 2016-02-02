Edit the file cgi-bin/sir_png.py so that the first line (beginning with #!...)
gives the path to the EPD python executable command.  This is necessary because
when the HTTP server runs the CGI script sir_png.py, it runs it as the user
"nobody", and "nobody" probably does not have EPD's python command on its path.

Then, in this directory (not the cgi-bin directory), run

$ python -m CGIHTTPServer

This starts a web server capable of handling CGI requests.  (That's right--it's
a one line web server!)

Then open a web browser and go to "http://127.0.0.1:8000".
Click on "Show Solution" to plot the solution to the SIR equations
for the given parameters and initial conditions.  The HTML file is set up
to pass the data to cgi-bin/sir_png.py, which will:
    (1) use SciPy's odeint function to solve the equations;
    (2) use matplotlib to plot the solution;
    (3) send the PNG file to stdout (preceding by an appropriate content
        header), which is fed back to the HTTP server and displayed in the
        web page.

