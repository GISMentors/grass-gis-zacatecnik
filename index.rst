.. figure:: images/grass-logo.png
   :width: 130px
   :align: left

**GRASS** (Geographic Resources Analysis Support System) je
multiplatformní desktopový geografický informační systém (:abbr:`GIS
(Geografický informační systém)`) určený pro správu geografických
2D/3D rastrových a vektorových dat, obrazových záznamů, produkci
vysoce kvalitních grafických výstupů, časoprostorové modelování a
vizualizaci dat.

GRASS GIS (http://grass.osgeo.org) je :wikipedia:`free software
<Svobodný software>` publikovaný pod všeobecnou licencí :abbr:`GNU
(GNU is Not Unix)` :abbr:`GPL (General Public License)`. Softwarové
knihovny systému GRASS a jeho nástroje (tzv. *moduly*) jsou z větší
části implementovány v programovacím jazyce :abbr:`ANSI (American
National Standards Institute)` :wikipedia:`C <Programovací jazyk
C>`. Několik málo modulů je potom implementováno v programovacím
jazyce :wikipedia:`C++`, jiné jsou dostupné v podobě skriptů v jazyce
:wikipedia:`Python`.


.. important:: Školení je zaměřeno na verzi `GRASS 7.0
               <http://grass.osgeo.org/download/software/#g70betax>`_. Nicméně
               pokud není uvedeno jinak, tak všechny uvedené postupy
               jsou funkční i ve verzi GRASS 6.4. Případné rozdíly mezi
               těmito verzemi jsou vždy explicitně zdůrazněny. Dále
               předpokládáme zapnutou *anglickou lokalizaci*,
	       viz :ref:`volba lokalizace <volba-lokalizace>`.

Intro
-----

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | První kroky                    | Základní pojmy                 |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   instalace/index              |   intro/struktura-dat          |
   |   intro/prvni-kroky            |   raster/index                 |
   |                                |   vector/index                 |
   |                                |   intro/region                 |
   +--------------------------------+--------------------------------+

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   |  Geodata                       | Dotazování                     |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   intro/import                 |   intro/atributove-dotazy      |
   |   intro/transformace           |   intro/prostorove-dotazy      |
   |   intro/export                 |                                |        
   +--------------------------------+--------------------------------+

Rastrové analýzy
-----------------

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   raster/rastrova-algebra      |   raster/analyza-nakladu       |
   +--------------------------------+--------------------------------+

Vektorové analýzy
------------------

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   vector/prostorove-funkce     |                                |        
   +--------------------------------+--------------------------------+

Další témata
------------

.. table::
   :class: noborder

   +--------------------------------+--------------------------------+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   misc/graficky-modeler        |   misc/mapove-vystupy          |
   |   misc/lokalizace              |   misc/grass-qgis              |
   +--------------------------------+--------------------------------+

Související materiály
---------------------

*Česky:*

* `Školení GRASS GIS na Les-ejk.cz <http://les-ejk.cz/skoleni/grass/>`_
* `GRASS GIS na portálu FreeGIS <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS>`_

*Anglicky:*

* `Dokumentace systému GRASS 7.0 <http://grass.osgeo.org/grass70/manuals/index.html>`_

*Literatura:*

* `Open Source GIS: A GRASS GIS Approach <http://www.grassbook.org/>`_ (anglicky)
* `GIS GRASS - Praktická rukověť <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Praktick%C3%A1_rukov%C4%9B%C5%A5>`_ (česky, velmi zastaralé)

Licence
-------

.. table::
   :class: noborder

   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | .. image:: _static/cc-by-sa.png  | Text školení je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_. |
   |           :width: 125px          |                                                                                                                                                       |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

