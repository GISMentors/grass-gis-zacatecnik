.. _kompilace:

Kompilace pod OS GNU Linux
--------------------------

.. todo:: přesunout mimo intro...
          
Nejprve si stáhneme zdrojové kódy systému GRASS ze systému pro správu
verzí `SVN
<http://svn.osgeo.org/grass/grass/branches/releasebranch_7_0>`_.

Prvním krokem tedy bude instalace :wikipedia:`Subversion`

.. code-block:: bash

                sudo apt-get install subversion

poté stáhneme zdrojový kód systému GRASS pomocí příkazu

.. code-block:: bash

                svn checkout https://svn.osgeo.org/grass/grass/branches/releasebranch_7_0 grass70

Pro kompilaci systému GRASS budete potřebovat následující balíčky:

.. code-block:: bash

                sudo apt-get install flex bison libncurses5-dev zlib1g-dev libproj-dev \
                proj-data proj-bin libreadline6-dev libgdal1-dev libtiff4-dev mesa-common-dev \
                libglu1-mesa-dev tcl8.5-dev tk8.5-dev libfftw3-dev lesstif2-dev libxmu-dev \
                libcairo2-dev g++ wx-common python-wxgtk2.8 libwxgtk2.8-dev libxmu-headers \
                libavcodec-dev libavformat-dev libswscale-dev libpq-dev

Následující kroky jsou

#. konfigurace (``configure``)
#. kompilace (``make``)
#. instalace (``make install``)

**Konkrétně:**

.. code-block:: bash

                cd grass70

                ./configure --prefix=/usr/local \
                --with-gdal --with-proj --with-proj-share=/usr/share/proj --with-geos \
                --with-nls --with-readline --with-cxx --enable-largefile \
                --with-freetype --with-freetype-includes=/usr/include/freetype2 \
                --with-sqlite --with-python --with-wxwidgets --with-pthread --with-cairo

.. note:: V případě podpory pro databázi :wikipedia:`PostgreSQL` (a
          geodatabázi :wikipedia:`PostGIS`) přidejde následující
          přepínač:

          .. code-block:: bash

                --with-postgres --with-postgres-includes=/usr/include/postgresql

.. code-block:: bash

                make
                sudo make install

GRASS spustíme příkazem

.. code-block:: bash

                grass70

*Aktualizace* verze GRASS (např. z verze 7.0.0 na 7.0.1) je velmi snadná.

.. code-block:: bash

   cd grass70
   svn up
   make
   sudo make install

.. noteadvanced::
                
          Krok instalace (``make install``) lze přeskočit vytvořením symlinku, např.

          .. code-block:: bash

             ln -s `pwd`/bin.`uname -m`-`uname -i`-linux-gnu/grass70 ~/bin
