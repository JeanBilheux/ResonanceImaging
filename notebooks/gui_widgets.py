from PyQt4 import QtCore, QtGui
import os
from decorators import format_directory


@format_directory
def gui_dname(dir=None):
    """Select files"""
    dirname = QtGui.QFileDialog.getExistingDirectory(None, "Select Folder ...", 
                                            dir, 
                                            QtGui.QFileDialog.ShowDirsOnly)
    return dirname


@format_directory
def gui_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    fname = QtGui.QFileDialog.getOpenFileNames(None, "Select file(s)...", 
            directory = dir, filter="Fits files(*.fits);;TIFF files(*.tif)")
    return fname


@format_directory
def gui_single_file(dir=None):
    """Select one o file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QtGui.QFileDialog.getOpenFileName(None, "Select file...", 
            dir, filter="Spectra File (*_Spectra.txt)")
    return fname


@format_directory
def gui_csv_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QtGui.QFileDialog.getOpenFileName(None, "Select file(s)...", 
            dir, filter="Text files (*.txt);;ASCII files(*.csv)")
    return fname
