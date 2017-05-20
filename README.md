
# sublimepyparser

Sublime plugin to use with pyparser (https://github.com/josecanciani/pyparser)

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


ParentClass
    SimpleClass
        SimpleClassExtension
    SimpleClass2
    ZSimpleClass
</pre>
