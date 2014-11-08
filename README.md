Školení GRASS GIS - Začátečník
==============================

URL: http://www.gismentors.eu/skoleni/grass-gis.html#zacatecnik

Poznámky k přípravě VMDK
------------------------

        wget http://cdimage.ubuntu.com/lubuntu/releases/14.10/release/lubuntu-14.10-desktop-i386.iso

        virtualbox

-> New

* Name: skoleni-GRASS-GIS
* Type: Linux
* Version: Ubuntu (32bit)

Memory size:

* 4000 MB

Hard drive:

* Create a virtual hard drive now

Hard drive file type:

* VMDK

Storage on physical hard drive:

* fixed size

File location and size:

* 8GB

-> Start

* vybrat lubuntu iso
* lang: english
* Install LUbuntu
* Welcome: English
* Download updates when installing
* Erase disk and install LUbuntu
* Timezone: Prague
* KDB: English (US)
* name: skoleni
* pc: skoleni-grass-gis
* user: skoleni
* pw: skoleni
* log in automatically

-> Restart Virtual Machine

* Install updates via Software Updater

-> In terminal:

      sudo apt-get install subversion flex bison libncurses5-dev zlib1g-dev \
      libreadline6-dev libtiff5-dev mesa-common-dev \
      libglu1-mesa-dev libfftw3-dev libxmu-dev \
      libcairo2-dev g++ wx-common python-wxgtk2.8 libwxgtk2.8-dev libxmu-headers \
      libavcodec-dev libavformat-dev libswscale-dev \
      libgeos-dev libsqlite3-dev
   
      mkdir src
      cd src

      # proj4
      svn checkout http://svn.osgeo.org/metacrs/proj/branches/4.9/proj/
      cd proj
      ./configure --prefix=/usr/local --mandir=/usr/local/share
      make
      sudo make install
      sudo ldconfig
      cd ..
      
      # gdal
      svn checkout http://svn.osgeo.org/gdal/branches/1.11/gdal/
      cd gdal
      ./configure --prefix=/usr/local --mandir=/usr/local/share \
               --with-sqlite3 --with-python \
               --with-gnu-ld 
      make
      make install
      cd..
      
      # grass
      svn checkout https://svn.osgeo.org/grass/grass/branches/releasebranch_70 grass70_release
      cd grass70_release
      ./configure --prefix=/usr/local \
            --with-gdal --with-proj --with-geos \
            --with-nls --with-readline --with-cxx --enable-largefile \
            --with-freetype --with-freetype-includes=/usr/include/freetype2 \
            --with-sqlite --with-python --with-wxwidgets --with-pthread --with-cairo
      make
      mkdir ~/bin
      ln -s `pwd`... ~/bin
      cd ..