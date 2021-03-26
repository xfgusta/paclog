# paclog

A pacman log analyzer

## Install

### pip

```
$ pip install git+https://github.com/xfgusta/paclog.git
```

Export `~/.local/bin` to PATH

```
$ export PATH="$HOME/.local/bin:$PATH"
```

You can also add it to your `.bashrc`

```
$ echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Manually

```
$ git clone https://github.com/xfgusta/paclog.git
$ cd paclog
# install -m 0755 paclog /usr/bin/paclog
```

## Remove

### pip

```
# pip uninstall paclog
```

### Manually

```
# rm /usr/bin/paclog
```

## Usage

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

## Screenshots

![](img/img-01.png?raw=true)

![](img/img-02.png?raw=true)

## License

The MIT License (MIT)

paclog 1.1 Copyright (C) 2021 Gustavo Costa