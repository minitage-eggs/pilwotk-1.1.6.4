#add minitage libraries to search pathes
import os
def pil(options,buildout):
    cwd = os.getcwd()
    os.chdir(options['compile-directory'])
    os.system("""
SED=$(which gsed)
if [ ! -f "$SED" ];then
       SED=sed
fi
$SED -re "s:^(FREETYPE_ROOT.*)$:FREETYPE_ROOT=libinclude('%(freetype)s'):g" -i setup.py
$SED -re "s:^(TIFF_ROOT.*)$:TIFF_ROOT=libinclude('%(tiff)s'):g" -i setup.py
$SED -re "s:^(JPEG_ROOT.*)$:JPEG_ROOT=libinclude('%(jpeg)s'):g" -i setup.py
$SED -re "s:^(ZLIB_ROOT.*)$:ZLIB_ROOT=libinclude('%(zlib)s'):g" -i setup.py
              """%{'freetype':buildout['freetype']['location'],
                   'jpeg':buildout['libjpeg']['location'],
                   'tiff':buildout['libtiff']['location'],
                   'zlib':buildout['zlib']['location'],
                  }
                  )
    os.chdir(cwd)

