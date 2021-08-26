from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property
from PySide2 import QtGui

import sys

from main_window import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        main_window = MainWindow(ctx=self)
        main_window.resize(1920 / 4, 1080 / 4)
        main_window.show()
        return self.app.exec_()

    @cached_property
    def img_checked(self):
        return QtGui.QIcon(self.get_resource("Images/checked.png"))

    @cached_property
    def img_unchecked(self):
        return QtGui.QIcon(self.get_resource("Images/unchecked.png"))


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())
