#!/usr/bin/python
# -*- coding: utf-8 -*-

# File:                 pastebin.py
# Author:               Lasse Vang Gravesen <gravesenlasse@gmail.com>
# Description:          Upload file contents to Pastebin, for GNU/Linux. Example usage: 
# Input:                cat loremipsum | pastebin --syntax text
# Output:               http://pastebin.com/TNEXMaYE
# Start date:           10-06-2011 02:24
# Last edited date:     11-06-2011 01:12

import sys
import argparse
import urllib
import urllib2

VERSION = "1.0.2"

def pastebin(content, syntax=None, private=None):
    api_url = 'http://pastebin.com/api/api_post.php'
    api_dev_key = ''    # Set this to your api_dev_key.
    api_user_key = ''   # Set this to your api_user_key, if you have one or if you want.
    api_paste_text = content.decode('ascii', 'ignore').encode('utf-8')
    if private == True:
        api_paste_private = '1'
    else:
        api_paste_private = '0'
    if syntax:
        api_paste_format = syntax
    else:
        api_paste_format = 'text'
    api_option = 'paste'

    values = {'api_dev_key': api_dev_key,
            'api_paste_code': api_paste_text,
            'api_paste_private': api_paste_private,
            'api_paste_format': api_paste_format,
            'api_option': api_option,
    }
    if api_user_key:
        values['api_user_key'] = api_user_key

    data = urllib.urlencode(values)
    req = urllib2.Request(api_url, data)
    content = urllib2.urlopen(req).read()
    return content

def run(content, syntax=None, private=None):
    out = pastebin(content, syntax=syntax, private=private)
    return out

def main():
    parser = argparse.ArgumentParser(description="Pipe content, or file to pastebin.com")
    parser.add_argument('-c', '--content', action='store', dest='c',
            default=sys.stdin, type=argparse.FileType('r'), help="Set file to send to pastebin, set to stdin on default.")
    parser.add_argument('-t', '--text', action='store', dest='t', default=None,
            type=str, help="Set text to send to pastebin, if you don't want to go through stdin or a file, set to None on default")
    parser.add_argument('-s', '--syntax', action='store', dest='s',
            default="text", type=str, help="Set the syntax to store content in, set to text on default.")
    parser.add_argument('-p', '--private', action='store_true', dest='p',
            default=False, help="Set paste to be private, set to False on default.")
    args = parser.parse_args()
    content = args.c
    text = args.t
    syntax = args.s
    private = args.p

    if content or text:
        if text:
            content = text
        else:
            content = content.read()
        print run(content, syntax=syntax, private=private)
    else:
        sys.exit("No content set, quitting.")

if __name__ == '__main__':
    main()

