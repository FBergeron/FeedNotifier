README
======
This is a fork of the Feed Notifier application (http://www.feednotifier.com).  

Here are some useful information.

To generate the .mo files for the localized strings:

%PYTHON_HOME%\Tools\i18n\msgfmt.py locale\fr\LC_MESSAGES\FeedNotifier.po
%PYTHON_HOME%\Tools\i18n\msgfmt.py locale\en\LC_MESSAGES\FeedNotifier.po

This should be done automatically by setup.py.

To build the application and the installer, first:

Copy the Microsoft.VC90.CRT\MSVCP90.dll into the application directory.

Then: 

clean.bat
build.bat
