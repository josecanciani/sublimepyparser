
# sublimepyparser

Sublime plugin to use with pyparser (https://github.com/josecanciani/pyparser)

# Install

This project is not on Package Package Control, so you need to install it yourself. Instructions are simple: just clone this project in your Sublime's package dir. Here's an example on Linux:

<pre>
$ cd ~/.config/sublime-text-3/Packages
$ git clone https://github.com/josecanciani/sublimepyparser.git
$ cd sublimepyparser
$ git submodule init
$ git submodule update
</pre>

To upgrade, just pull:

<pre>
$ cd ~/.config/sublime-text-3/Packages
$ git pull
$ git submodule update
</pre>

# Features

Still more to come, for now, here's what it's supported:

## Class tree (ctrl+alt+shift+t)

Use over a class and it will open a new tab with the class tree.
Example:
<pre>
Results for class ParentClass
  Properties (change them in SublimePyParser User Preference file):
  tree.childLimit: 10 (max extensions per class to process)
  tree.processParents: no (include selected class parents, to build full tree -may take long-)


ParentClassG
    SimpleClass
        SimpleClassExtension
    SimpleClass2
    ZSimpleClass
</pre>

# Development roadmap

* Autocomplete class methods
* Autocomplete class constants
