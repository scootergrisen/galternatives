#!/usr/bin/python3

import os
import sys
import galternatives
from galternatives import Gtk
import gettext
from galternatives.common import PACKAGE
from galternatives.common import logger

_ = gettext.gettext

gettext.bindtextdomain (PACKAGE)
gettext.textdomain (PACKAGE)

if os.getuid ():
        if os.access ('/usr/bin/gksu', os.X_OK):
            sys.exit (os.system ('/usr/bin/gksu -t "%s" -m "%s" -u root %s' %
                                 (_('Running Alternatives Configurator...'),
                                  _('<b>I need your root password to run\n'
                                    'the Alternatives Configurator.</b>'),
                                  sys.argv[0])))
        else:
            'A Message Dialog saying GAlternatives wont work without gksu'
            dialog = Gtk.MessageDialog(
                    None, # parent
                    0, # flags
                    Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK,
                    _('Warning'),
                    )
            dialog.format_secondary_markup(_(
                    '<b>This program should be run as root and /usr/bin/gksu '
                    'is not available.</b>\n\n'
                    'I am unable to request the password myself without gksu. Unless you have '
                    'modified your system to explicitly allow your normal user to modify '
                    'the alternatives system, GAlternatives will not work.'))
            dialog.run()
            dialog.destroy()

ga = galternatives.GAlternatives ()
try:
    if sys.argv[1] == '--debug':
        ga.DEBUG = True
except IndexError:
    pass
ga.mainloop()
