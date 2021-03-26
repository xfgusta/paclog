#!/usr/bin/python

from setuptools import setup

LONG_DESCRIPTION = '''
# paclog

A pacman log analyzer

# Usage

View installed, removed, and upgraded packages

```
$ paclog
```

View only installed packages

```
$ paclog --filter in
```

View only removed packages

```
$ paclog --filter rm
```

View only upgraded packages

```
$ paclog --filter up
```

Search for packages using regular expression

```
$ paclog ^xorg
```

Enable less verbose mode

```
$ paclog --short
```

Set an alternate log file

```
$ paclog --file pacman.log
```

Show default pacman log file

```
$ paclog --show
/var/log/pacman.log
```

Clean log file

```
# paclog --clean
/var/log/pacman.log cleaned
```

Read raw log file

```
# paclog --raw
```

Colored output

```
$ paclog --color
```

Show help message

```
$paclog --help
```

# License

The MIT License (MIT)

paclog 1.1 Copyright (C) 2021 Gustavo Costa
'''

setup(name='paclog',
      version='1.1',
      description='A pacman log analyzer',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Gustavo Costa',
      author_email='xfgusta@gmail.com',
      url='https://github.com/xfgusta/paclog/',
      scripts=['paclog'],
)
