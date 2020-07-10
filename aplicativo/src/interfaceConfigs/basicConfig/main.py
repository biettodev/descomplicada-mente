from PySide2.QtCore import ( QCoreApplication, QDate, QDateTime, QMetaObject, QObject, QRect, QSize, Qt )
from PySide2.QtGui import ( QIcon )
from PySide2.QtWidgets import *

def buttonConfig(buttonName, objectTitle, iconName, iconLocal, layoutName):
    iconName.addFile(iconLocal, QSize(), QIcon.Normal, QIcon.Off)
    buttonName.setIconSize(QSize(20, 20))
    buttonName.setObjectName(objectTitle)
    buttonName.setIcon(iconName)
    layoutName.addWidget(buttonName)
    
def frameConfig(frameName, objectTitle, x, y, width, height):
    frameName.setObjectName(objectTitle)
    frameName.setGeometry(QRect(x, y, width, height))
    frameName.setFrameShape(QFrame.StyledPanel)
    frameName.setFrameShadow(QFrame.Raised)
    
def contentBoardConfig(scrollName, objectTitle, scrollWidgetName, scrollWidgetTitle, hvLayoutName, hvLayoutTitle, layoutName, layoutTitle):
    scrollName.setObjectName(objectTitle)
    scrollName.setGeometry(QRect(0, 0, 420, 381))
    scrollName.setStyleSheet(u"")
    scrollName.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scrollName.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    # scrollName.setWidgetResizable(True)
    scrollWidgetName.setObjectName(scrollWidgetTitle)
    scrollWidgetName.setGeometry(QRect(0, 0, 420, 381))
    hvLayoutName.setObjectName(hvLayoutTitle)
    hvLayoutName.setGeometry(QRect(0, 10, 400, 151))
    layoutName.setObjectName(layoutTitle)
    layoutName.setContentsMargins(10, 0, 0, 0)
    scrollName.setWidget(scrollWidgetName)