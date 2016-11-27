#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

# Copyright 2013 Alexey Kardapoltsev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json, sys, os
from vkdownloader import VkDownloader

def process_music(args):
  if args.action == "load":
    vk.load(args.user, args.dest, args.clean)
  if args.action == "loadpost":
    vk.loadpost(args.user, args.dest, args.src)
  elif args.action == "list":
    vk.show(args.user)
  elif args.action == "play":
    vk.play(args.user)
  else:
    print("unknown action")

def process_friends(args):
  if args.action == "list":
    vk.show_friends(args.user)
  else:
    print("unknown action")

topParser = argparse.ArgumentParser()

topParser.add_argument("-u", "--user", help = "user id")
subParsers = topParser.add_subparsers(title = "Command categories")
music = subParsers.add_parser("music", description = "working with music")
friends = subParsers.add_parser("friends", description = "working with friends")

friends.add_argument("action", help = "friends actions", choices=["list"])
friends.set_defaults(func = process_friends)

music.add_argument("action", help = "music actions", choices=["list", "load", "loadpost", "play"])
music.add_argument("-d", "--dest", help = "destination directory for music download, default is current dir")
music.add_argument("-s", "--src", help = "link to vk content")
music.add_argument("-c", "--clean", dest='clean', action='store_true', help = "with this options destination directory will be cleaned")
music.set_defaults(clean = False)
music.set_defaults(func = process_music)

try:
    import argcomplete
    argcomplete.autocomplete(topParser)
except ImportError:
    pass

subParsers.required = True
args = topParser.parse_args()

vk = VkDownloader()

args.func(args)
