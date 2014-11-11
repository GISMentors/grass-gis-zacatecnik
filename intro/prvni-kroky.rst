Úvod do systému GRASS
---------------------

Po instalaci (viz návod pro :doc:`GNU/Linux <../instalace/linux>` a
:doc:`MS Windows <../instalace/windows>`) systému GRASS je potřeba
opatřit geodata ve struktuře, kterou systém vyžaduje (viz
:doc:`koncept lokací a mapsetů <../intro/struktura-dat>`).

.. tip::

   Na webových stránkách projektu GRASS jsou volně ke stažení
   `testovací a edukační datasety
   <http://grass.osgeo.org/download/sample-data/>`_. Jde především o
   OSGeo edukační `North Carolina
   <http://www.grassbook.org/data_menu3rd.php>`_ dataset, který je ke
   stažení jako `zip archiv
   <http://grass.osgeo.org/sampledata/north_carolina/nc_spm_08_grass7.zip>`_. Tato
   data lze pod MS Windows stáhnout i pomocí :ref:`nativního
   instalátoru <nativni-instalator-data>`. V tomto případě najdete
   data v adresáři ``%USERPROFILE%\Documents\grassdata``.

.. note::

   Pro účely školení byl vytvořena vlastní lokace z daty pocházejících
   z otevřených či veřejných zdrojů jako je `EU-DEM
   <http://www.eea.europa.eu/data-and-maps/data/eu-dem>`_, `RÚIAN
   <http://www.cuzk.cz/ruian/RUIAN.aspx>`_, `OpenStreetMap
   <http://wiki.openstreetmap.org/wiki/Main_Page>`_, `Dibavod
   <http://www.dibavod.cz/>`_.

   Předpřipravená GRASS lokace je dostupná jako `zip archiv <>`_.

Spuštění systému GRASS
======================

V případě, že je GRASS :doc:`nainstalován <../instalace/index>`
standardní cestou, měl by být dostupný z hlavní nabídky vašeho
:abbr:`OS (Operační systém)`.

.. figure:: ../instalace/images/grass-ubuntu-launch.png
            :class: middle

            Spuštění systému GRASS v Ubuntu 12.10

.. figure:: ../instalace/images/wingrass-8.png

            Spuštění systému GRASS z nabídky *Start* v MS Windows.

.. notecmd:: spuštění systému GRASS

   V :abbr:`OS (Operační systém)` :wikipedia:`GNU/Linux` je dostupný systém GRASS po
   instalaci z příkazové řádky jako program ``grassXY``, kde
   ``XY`` označuje jeho verzi. Příklad spuštění verze GRASS
   7.0:

   .. code-block:: bash

                grass70

Ve výchozím nastavení program nastartuje v grafickém módu. Úvodní
dialog umožňuje nastavit :doc:`adresář s geodaty, lokaci a mapset
<../intro/struktura-dat>`, které jsou nutné pro samotné spuštění
systému. Po jejich zadaní lze pokračovat dále (tlačítko :kbd:`Start
GRASS`).

.. _spusteni-grass:

.. figure:: images/welcome-screen.png

            Úvodní dialog systému GRASS pro výběr adresáře s geodaty :fignote:`(1)`,
            lokace :fignote:`(2)` a mapsetu :fignote:`(3)`.

.. noteadvanced::
   
   **Příklady spuštění z příkazové řádky**

                * GRASS v textovém rozhraní, adresář s geodaty nastavena na
                  ``/opt/grassdata``, lokace
                  ``nc_spm_08_grass7`` a mapset ``user1``

                  .. code-block:: bash

                                  grass70 -text /opt/grassdata/nc_spm_08_grass7/user1/

                * GRASS v grafickém rozhraní, databanka, lokace a
                  mapset nastaven z minulého sezení

                  .. code-block:: bash

                                  grass70 -gui

                * GRASS v grafickém rozhraní, vytvořit novou lokace
                  ``skoleni`` (souřadnicový systém S-JTSK
                  :epsg:`5514`) 

                  .. code-block:: bash

                                  grass70 -gui -c EPSG:5514 /opt/grassdata/skoleni
