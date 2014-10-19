Úvod do systému GRASS
---------------------

Po instalaci (viz návod pro :doc:`GNU/Linux <../instalace/linux>` a
:doc:`MS Windows <../instalace/windows>`) systému GRASS je potřeba
zajistit geodata ve struktuře, kterou systém vyžaduje (viz
:doc:`koncept lokací a mapsetů <../intro/struktura-dat>`).

.. note::

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

Pro další práci předpokládáme, že máme k dispozici GRASS lokaci
datasetu *North Carolina* umístěnou v adresáři ``/opt/grassdata``.

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

.. admonition:: Spuštění systému GRASS z příkazové řádky

   V :abbr:`OS (Operační systém)` :wikipedia:`GNU/Linux` je dostupný systém GRASS po
   instalaci z příkazové řádky jako program ``grassXY``, kde
   ``XY`` označuje jeho verzi. Příklad spuštění verze GRASS
   7.0:

   .. code-block:: bash

                grass70

Ve výchozím nastavení program nastartuje v grafickém módu. Úvodní
dialog umožňuje nastavit :doc:`adresář s geodaty, lokaci a mapset
<../intro/struktura-dat>`, které jsou nutné pro samotné spuštění
systému. Po jejích zadaní lze pokračovat dále (tlačítko ``Start
GRASS``).

.. _spusteni-grass:

.. figure:: images/welcome-screen.png

            Úvodní dialog systému GRASS pro výběr adresáře s geodaty :fignote:`(1)`,
            lokace :fignote:`(2)` a mapsetu :fignote:`(3)`.

Po spuštění systému GRASS se objeví **správce vrstev** (Layer Manager) a
**mapové okno** (Map Display).

.. figure:: images/grass-gui-launch.png
            :class: middle

            Základní komponenty GUI systému GRASS - správce vrstev
            :fignote:`(1)` a mapové okno :fignote:`(2)`.

.. admonition:: Příklady spuštění z příkazové řádky (pro pokročilé uživatele)

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

Zobrazení geodat v mapovém okně
===============================

Rastrová či vektorová data lze do *stromu vrstev* (viz záložka *Map
layers*) přidávat z menu :menuselection:`File --> Map display`, nástrojové lišty či
přímo z příkazové řádky *správce vrstev*.

.. note::

   Pokud se v mapovém okně nezobrazují žádná data, je nutné nastavit
   pohled na aktuálně vybranou mapu.

   .. figure:: images/map-display-full-zoom.png
               :class: middle

               Nastavení pohledu mapového okna na vybranou mapovou vrstvu

   Automatické nastavení pohledu při přidání nové mapové vrstvy lze
   nastavit v :menuselection:`Settings --> Preferences`.

   .. figure:: images/wxgui-settings-autozoom.png

               Nastavení automatické změny pohledu při přidání nové mapové vrstvy

Rastrová data
^^^^^^^^^^^^^

Pro přidání *rastrové mapy* existují celkem čtyři postupy:

* nástrojová lišta

.. figure:: images/wxgui-toolbar-raster.png
            
            Přidání rastrové mapy z nástrojové lišty správce vrstev

.. figure:: images/wxgui-d-rast.png

            Volba rastrové mapy

* menu :menuselection:`File --> Map display --> Add raster`

* klávesová zkratka :kbd:`Ctrl+Shift+R`

* příkazová řádka (``Command console``) správce vrstev, příkaz :grasscmd:`d.rast`

.. figure:: images/wxgui-console.png

            Příkazová řádka správce vrstev

.. figure:: images/wxgui-console-raster.png

            Přidání rastrové mapy z příkazové řádky správce vrstev

Ostatní mapové vrstvy, které mají rastrový charakter jsou dostupné z
nástrojové lišty nebo z příkazové řádky správce vrstev.

.. figure:: images/wxgui-toolbar-raster-misc.png
            :class: middle

            Přidání ostatních rastrových dat z nástrojové lišty správce vrstev

.. figure:: images/wxgui-toolbar-raster-misc-1.png

            Menu pro přidání rastrových dat

Jde o následující typy rastrových dat:

* 3D rastová data
* :wikipedia:`RGB` barevná syntéza - příkaz :grasscmd:`d.rgb`
* :wikipedia:`HIS <HSL>` barevná syntéza - příkaz :grasscmd:`d.his`
* :wikipedia-en:`Stínovaný reliéf <Shapeded relief>` - příkaz :grasscmd:`d.shadedmap`
* rastrová mapa, zobrazení směru - příkaz :grasscmd:`d.rast.arrow`
* rastrová mapa, zobrazení hodnot buněk - příkaz :grasscmd:`d.rast.num`

.. figure:: images/wxgui-d-rgb.png
            :class: large

            Příklad barevné syntézy kanálů :wikipedia:`Landsat 5` TM ve skutečných barvách

Vektorová data
^^^^^^^^^^^^^^

Podobně pro přidání *vektorové mapy*:

* nástrojová lišta

.. figure:: images/wxgui-toolbar-vector.png

            Přidání vektorové mapy z nástrojové lišty správce vrstev

.. figure:: images/wxgui-d-vect.png

            Volba vektorové mapy

* menu :menuselection:`File --> Map display --> Add vector`

* klávesová zkratka :kbd:`Ctrl+Shift+V`

* příkazová řádka (``Command console``) správce vrstev, příkaz :grasscmd:`d.vect`

.. figure:: images/wxgui-console-vector.png

            Přidání vektorové mapy z příkazové řádky správce vrstev

Ostatní mapové vrstvy, které mají vektorový charakter jsou dostupné z
nástrojové lišty nebo z příkazové řádky správce vrstev.

.. figure:: images/wxgui-toolbar-vector-misc.png
            :class: middle

            Přidání ostatních vektorových dat z nástrojové lišty správce vrstev

.. figure:: images/wxgui-toolbar-vector-misc-1.png
            :class: middle

            Menu pro přidání vektorových dat

Jde o následující typy vektorových dat:

* tématické zobrazení plošných vektorových dat - příkaz :grasscmd:`d.thematic.area`
* zobrazení grafů - :grasscmd:`d.vect.chart`

Příkazy systému GRASS
=====================

GRASS GIS je *modulární systém*, který disponuje poměrně rozsáhlou
množinou malých, ale výkonných programů (v terminologii systému GRASS
*modulů*). To odpovídá koncepci :wikipedia:`Unixu <Unix>` jako
takového. Daný program má za úkol vyřešit dílčí problém, měl by být co
nejmenší a poměrně jednoduchý.

Jednotlivé příkazy - GRASS moduly - mají konzistentní syntaxi, jejich
jména se skládají z předpony označující skupinu příkazů a krátkého
názvu napovídající účel modulu (viz tab. níže). Například modul
:grasscmd:`v.buffer` patří do skupiny ``vector`` a je určen pro vytvoření
obalové zóny (tzv. bufferu) nad vektorovými daty.

.. table::
   :class: border

   +----------+--------------------------------+-----------------------------------------------+
   | prefix   | skupina                        | popis                                         |
   +==========+================================+===============================================+
   | ``db.``  | :grasscmd:`database`           | podpora externích databázových systémů        |
   +----------+--------------------------------+-----------------------------------------------+
   | ``d.``   | :grasscmd:`display`            | grafické výstupy a vizuální dotazy            |
   +----------+--------------------------------+-----------------------------------------------+
   | ``g.``   | :grasscmd:`general`            | obecné příkazy pro manipulaci s daty          |
   +----------+--------------------------------+-----------------------------------------------+
   | ``i.``   | :grasscmd:`imagery`            | zpracování obrazových dat                     |
   +----------+--------------------------------+-----------------------------------------------+
   | ``ps.``  | :grasscmd:`postscript`         | tvorba mapových výstupů ve formátu PostScript |
   +----------+--------------------------------+-----------------------------------------------+
   | ``r.``   | :grasscmd:`raster`             | zpracování (2D) rastrových dat                |
   +----------+--------------------------------+-----------------------------------------------+
   | ``r3.``  | :grasscmd:`raster3D`           | zpracování 3D rastrových dat (voxels)         |
   +----------+--------------------------------+-----------------------------------------------+
   | ``v.``   | :grasscmd:`vector`             | zpracování 2D/3D vektorových dat              |
   +----------+--------------------------------+-----------------------------------------------+

Příkazy (tj. moduly) systému GRASS lze spouštěn několika způsoby
(příklad pro :grasscmd:`r.buffer`):

* z menu správce vrstev

.. figure:: images/wxgui-menu-r-buffer.png

            Spuštění modulu :grasscmd:`r.buffer` z menu správce vrstev

* z nástroje :item:`Search module` správce vrstev

.. figure:: images/wxgui-search-r-buffer.png

            Spuštění modulu :grasscmd:`r.buffer`` pomocí nástroje :item:`Search module`

* z příkazové řádky správce vrstev

.. figure:: images/wxgui-console-r-buffer.png
            :class: middle

            Spuštění modulu :grasscmd:`r.buffer` s příkazové řádky správce vrstev

Pokud jsou zadány všechny povinné parametry (v případě modulu
:grasscmd:`r.buffer` jde o :option:`input`, :option:`output` a
:option:`distances`), tak se modul spustí přímo.

.. figure:: images/wxgui-console-r-buffer-launch.png

            Spuštění modulu :grasscmd:`r.buffer` včetně zadání parametrů

* z :doc:`grafického modeleru <../misc/graficky-modeler>`

