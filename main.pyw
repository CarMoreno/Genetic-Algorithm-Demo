from controlador.controlador import *

"""Desde aca corremos la aplicacion"""

if __name__ == '__main__':
    #Motor de funcionamiento
    app = QtGui.QApplication(sys.argv)
    myapp = ControladorGenetico()
    myapp.show()
    sys.exit(app.exec_())