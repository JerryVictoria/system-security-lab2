#!/usr/bin/env python3
import os.path
import subprocess
import sys
import urllib

KEY_FILE = "submit.token"

def main(filename):
    # Prompt for key if missing
    if not os.path.exists(KEY_FILE):
        print("Please visit https://6858.scripts.mit.edu/2020/handin.py/")
        print("and enter your API key.")
        key = input("Key: ").strip()
        with open(KEY_FILE, "w") as f:
            f.write(key + "\n")
        print("API key written to %s" % KEY_FILE)

    # Read the key.
    with open(KEY_FILE) as f:
        key = f.read().strip()

    # Shell out to curl. urllib2 doesn't deal with multipart attachments. Throw
    # away the output; you just get a random HTML page.
    with open("/dev/null", "a") as null:
        subprocess.check_call(["curl", "-f",
                               "-F", "file=@%s" % filename,
                               "-F", "key=%s" % key,
                               "https://6858.scripts.mit.edu/2020/handin.py/upload"],
                              stdout=null, stderr=null)
    print("Submitted %s." % filename)
    print("Please visit https://6858.scripts.mit.edu/2020/handin.py/")
    print("to verify the upload.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s TARBALL" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
