# Unix python scripting toolset
This toolset is a python library to make writing python programs in combination with unix commands easier.

It support python 2.X and 3.X

## Usage
If necessary adapt the shebang in the first line of the library.

```
#!/usr/bin/python
```

Put the program in the same directory as your main python program

```
from run_unix_command import run_unix_cmd

run_unix_cmd("ls -ltr /usr/bin")		# lists the files/directories in /usr/bin
run_unix_cmd("mv old.html new.html") 	# Renames old.html to new.html
...

```

Afterwards you can use