# keep one folder above .ui files
# TODO consider removing shell commands
from PyQt4 import uic
import os

cd = os.path.dirname(os.path.realpath(__file__))


def move(directory, file_name):
    return directory.replace(cd + "/UI", cd), file_name.replace("", "")


uic.compileUiDir(cd + "/UI", map=move)


# def rename_and_move_callable(directory, file_name):
#         return directory.replace("ui/", "widget/"), file_name.replace("Widget.py", ".py")
#
# uic.compileUiDir("ui/", map=rename_and_move_callable)