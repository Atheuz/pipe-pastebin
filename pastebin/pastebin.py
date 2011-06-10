#!/usr/bin/python
# -*- coding: utf-8 -*-

# File:                 pastebin.py
# Author:               Lasse Vang Gravesen <gravesenlasse@gmail.com>
# Description:          Send something to pastebin through a pipe, for Debian. Example usage: 
# Input:                cat diff5532.diff | pastebin --format diff
# Output:               http://pastebin.com/cQem4AJT
# Start date:           10-06-2011 02:24
# Last edited date:     10-06-2011 18:52

import sys
import argparse
import urllib
import urllib2
import base64

VERSION = "1.0.0"

def pastebin(x, format_=None):
    api_url = r'http://pastebin.com/api/api_post.php'
    api_dev_key = r'8f89b5cf8364b32ad0a1f8a2520614c9'
    api_user_key = r'cee5dccb7744bde5095e0ff555613bec'
    api_paste_text = x.decode('ascii', 'ignore').encode('utf-8')
    api_paste_private = '0'
    if format_:
        api_paste_format = format_
    else:
        api_paste_format = 'text'
    api_option = 'paste'

    values = {'api_dev_key': api_dev_key,
            'api_paste_code': api_paste_text,
            'api_paste_private': api_paste_private,
            'api_paste_format': api_paste_format,
            'api_option': api_option,
            'api_user_key': api_user_key
    }

    data = urllib.urlencode(values)
    req = urllib2.Request(api_url, data)
    content = urllib2.urlopen(req).read()
    return content

def run(c, f=None):
    out = pastebin(c, format_=f)
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--content', action='store', dest='c',
            default=sys.stdin, type=argparse.FileType('r'), help="Set content to send to pastebin")
    parser.add_argument('-f', '--format', action='store', dest='f',
            default=None, type=str, help="Set the format to store content in")
    args = parser.parse_args()
    c = args.c
    f = args.f
    if c:
        c = c.read()
        if f:
            print run(c, f=f)
        else:
            print run(c, f='text')
    else:
        pass

if __name__ == '__main__':
    main()

