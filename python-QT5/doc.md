## how to use pycharm develop QT application

1. Install pycharm 
2. Create a new python project 
- select pure python 
- select new virtual environment 

3. Click `File->Settings->Python interpreter`, add `+` button (right), click 
`Manage Repositories` , add Chinese resources ,delete old source.
[resource](https://blog.csdn.net/yang889999888/article/details/77672737)
4. Install `PyQt5` and `pyqt5-tools`
5. Open QT-designer, create new *.ui file, and design your own application 
6. Open terminal ,and type `venv\Scripts\pyuic5.exe -x designer\testMain.ui -o testMainform.py`

