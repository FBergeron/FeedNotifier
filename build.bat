python setup.py
"C:\Program Files\Inno Setup 5\Compil32.exe" /cc installer.iss
copy dist\revision.txt installer
mkdir dist\locale\en\LC_MESSAGES
mkdir dist\locale\fr\LC_MESSAGES
copy locale\en\LC_MESSAGES\FeedNotifier.mo dist\locale\en\LC_MESSAGES
copy locale\fr\LC_MESSAGES\FeedNotifier.mo dist\locale\fr\LC_MESSAGES
