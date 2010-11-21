import os
import py2exe
import sys
from distutils.core import setup

manifest = '''
<assembly xmlns="urn:schemas-microsoft-com:asm.v1"
manifestVersion="1.0">
  <assemblyIdentity
    version="2.0.0.0"
    processorArchitecture="x86"
    name="Feed Notifier"
    type="win32"
  />
  <description>Feed Notifier 2.3.1 (fr)</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
          level="asInvoker"
          uiAccess="false"
        />
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
        type="win32"
        name="Microsoft.VC90.CRT"
        version="9.0.30729.1"
        processorArchitecture="x86"
        publicKeyToken="1fc8b3b9a1e18e3b"
      />
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
        type="win32"
        name="Microsoft.Windows.Common-Controls"
        version="6.0.0.0"
        processorArchitecture="x86"
        publicKeyToken="6595b64144ccf1df"
        language="*"
      />
    </dependentAssembly>
  </dependency>
</assembly>
'''

# Don't require the command line argument.
sys.argv.append('py2exe')

# Include these data files.
def get_data_files():
    def filter_files(files):
        def match(file):
            extensions = ['.dat','.po','.pot']
            for extension in extensions:
                if file.endswith(extension):
                    return True
            return False
        return tuple(file for file in files if not match(file))
    def tree(src):
        return [(root, map(lambda f: os.path.join(root, f), filter_files(files))) for (root, dirs, files) in os.walk(os.path.normpath(src))]
        #return [(root, map(lambda f: os.path.join(root, f), filter_files(files))) for (root, dirs, files) in os.walk(os.path.normpath(src)) if '.svn' not in root and '.svn' in dirs]
    def include(src):
        result = tree(src)
        result = [('.', item[1]) for item in result]
        return result
    data_files = []
    data_files += tree('./icons')
    data_files += tree('./sounds')
    data_files += tree('./Microsoft.VC90.CRT')
    data_files += tree('./locale')
    return data_files
    
# Build the distribution.
setup(
    options = {"py2exe":{
        "compressed": 1,
        "optimize": 1,
        "bundle_files": 1,
        "includes": ['parsetab'],
    }},
    windows = [{
        "script": "main.py",
        "dest_base": "notifier",
        "icon_resources": [(1, "icons/feed.ico")],
        "other_resources": [(24, 1, manifest)],
    }],
    data_files = get_data_files(),
)

# Build Information
def get_version():
    return '2.3.1'
        
def save_build_info():
    version = get_version()
    path = 'dist/version.txt'
    with open(path, 'w') as file:
        file.write(version)
    print
    print 'Saved build version %s to %s' % (version, path)
    
save_build_info()
