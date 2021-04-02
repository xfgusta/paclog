# paclog

A pacman log analyzer

## Install

### Package from AUR

```
$ git clone https://aur.archlinux.org/paclog.git
$ cd paclog
$ makepkg -si
```

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

## Uninstall

### pacman

```
# pacman -R paclog
```

### pip

```
$ pip uninstall paclog
```

### Manually

```
# rm /usr/bin/paclog
```

## Screenshots

![](img/img-01.png?raw=true)

![](img/img-02.png?raw=true)

![](img/img-03.png?raw=true)

![](img/img-04.png?raw=true)

![](img/img-05.png?raw=true)

![](img/img-06.png?raw=true)

## Acknowledgements

+ [Marcel Walk](https://github.com/MarcelWalk) for creating and maintaining the AUR package

+ [Ricardo Costa](https://github.com/ricxpl) for helping me solve some issues

## License

The MIT License (MIT)

paclog 2.0 Copyright (C) 2021 Gustavo Costa
