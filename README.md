Školení GRASS GIS - Začátečník
==============================

URL: http://www.gismentors.eu/skoleni/grass-gis.html#zacatecnik

Stažení dat
-----------

      cd grassdata
      rsync -avz skoleni@46.28.111.140:~/grassdata/skoleni .

Poznámky k přípravě VMDK
------------------------

URL:  http://live.osgeo.org/en/download.html

-> In terminal:

      sudo apt-get install subversion flex bison libncurses5-dev zlib1g-dev \
      libreadline6-dev libtiff5-dev mesa-common-dev \
      libglu1-mesa-dev libfftw3-dev libxmu-dev \
      libcairo2-dev g++ wx-common python-wxgtk2.8 libwxgtk2.8-dev libxmu-headers \
      libgeos-dev libsqlite3-dev libpython-dev
   
      mkdir src
      cd src

      # grass (7.0)
      svn checkout https://svn.osgeo.org/grass/grass/branches/releasebranch_7_0 grass70_release
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