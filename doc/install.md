# Install Python3 


## install python3 and python3-pip
for ubuntu OS
```
sudo apt-get install python3-dev python3 python3-pip

```

## configure pip has chinese source 

Edit `~/.pip/pip.conf`, and add the following lines 

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```