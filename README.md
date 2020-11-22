# sav and srm converter

Simple Python utility ot convert between .sav and .srm files (file types commonly used used in emulators such as MyBoy and the mGBA Retroarch emulator.

It can be used either imported as a module, to be used in your own code.  Or the `converter.py` file can be run via the terminal.

# Usage:

`converter.py`:

    python3.8 converter.py path/to/file.srm
    python3.8 converter.py path/to/file.sav

If your path contains spaces, use `"``"`.  The file type will automatically be detected and converted.

As a module:

Only one function is provided.  The `convert(filename)` command.

To convert to .sav file:

    import SrmToSav
    SrmToSav.convert(filename)
   
To convert to .srm file:

    import SavToSrm
    SavToSrm.convert(filename)
    
WARNING:  I do not guarantee that this will always work, however from my testing, it seems to.
