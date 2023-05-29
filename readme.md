# Music Box

A collection of modules for exploring Fable II.

## Tools

Currently, there is only one tool that is a very primitive MDL to OBJ converter. Not all MDL files are supported (yet). At the moment, only the weapons are supported, and there are still errors with some of those.

*Note: The name "Music Box" is just a refence to the magical artifect of the same name. The tool currently does not do anything with music files.*

## Usage

```
music_box.py [-h] [-o OUTPUT] file
```
* file - The input MDL file to convert to OBJ
* output - Name of the OBJ file to create (uses the name of the MDL file if not specified)