"""
downloader.py -- An example that uses threads to do work in the background
                 while waiting for user input.
"""

# I've tried to keep this fairly simple.  There are *many* possible enhancements!

import os
import threading
import urllib2
# Importing readline adds some nice behavior to raw_input().
import readline


def download(url_connection, destination, block_size=32768):
    """Open and download the contents of `url_connection` (a url object
    created with urllib2.urlopen) and save in the directory `destination`.

    The program reads `block_size` bytes at a time when downloading the file.
    The filename of the file written in `destination` will be taken from the
    final component of the string `url_connection.url`.
    """
    basename = os.path.basename(url_connection.url)
    fullname = os.path.join(destination, basename)
    output_file = open(fullname, 'wb') 
    done = False
    while not done:
        data = url_connection.read(block_size)
        output_file.write(data)
        done = len(data) < block_size
    output_file.close()
    url_connection.close()


def main(destination):
    # `threads` is a list of tuples of the form (Thread, url).
    threads = []
    while True:
        try:
            inp = raw_input("]] ")
        except EOFError:
            # This occurs if the user hits Ctrl-D
            print "exit"
            break
        inp = inp.strip()
        if len(inp) == 0:
            continue
        elif inp == 'exit':
            break
        elif inp == 'status':
            for thread, url in threads:
                if thread.is_alive():
                    print "Downloading '%s'" % url
        else:
            # Assume the input is a URL to be downloaded.
            try:
                url_connection = urllib2.urlopen(inp)
            except urllib2.HTTPError, e:
                print "HTTP error occurred when opening URL '%s'" % inp
                print "Error code %d: %s" % (e.code, e.msg)
                continue
            except (ValueError, urllib2.URLError):
                print "Invalid URL '%s'" % inp
                continue
            print "Downloading '%s'" % inp
            thread = threading.Thread(target=download,
                                        args=(url_connection, destination))
            thread.daemon = True
            threads.append((thread, inp))
            thread.start()


if __name__ == "__main__":
    import argparse
    import textwrap

    description = textwrap.dedent("""\
    A simple URL downloader that demonstrates python threads.
    
    At the prompt, enter a URL to download.  Downloading will
    begin immediately, and the prompt will return.  Two commands
    are also understood:

    status   - Show the URLs currently downloading.
    exit     - Exit the program. (Active downloads will stop.)
    """)
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                        description=description)
    parser.add_argument('--dest', '-d', help='Destination directory; default is the current directory.')
    args = parser.parse_args()
    if args.dest is None:
        destination = os.path.curdir
    else:
        destination = args.dest
    main(destination)
