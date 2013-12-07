JAdventureGameEditor
===============

Description
---------------
A simple python script to make it easier to rewrite JAdventure game files. The eventual plan may be to create a gui, but for now, this is a quick way to do it rather than editing json files by hand.

Usage
---------------

To start:

    python JAdventureGameEditor.py

The initial beginning for the game and recommended to start editing is 0,0,-1

To move north,south,east,and west:

    mn
    ms
    me
    mw

To create a room to the north,south,east,and west:

    cn
    cs
    ce
    cw

The standard title for a corridor undergorund is:

    Dark Corridor

The standard description for a corridor underground is:

    A very long dark corridor

The standard locationType for tiles underground is:

    CAVE


Notes
-------------
 1. You currently cannot delete tiles, you'll need to edit by hand if you make a mistake (jsoneditoronline is recommended for this)
 1. This is very early software and more for personal ease than for production, use with caution. Fix where necessary.
 1. Going up and down is not yet implemented. Will need to be.

Contributing
----------
 1. Fork
 1. Clone
 1. Make a branch (optional)
 1. Push to your own fork
 1. Make a pull request

