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
<Svobodný software>` a *open source* publikovaný pod všeobecnou licencí
:abbr:`GNU (GNU is Not Unix)` :abbr:`GPL (General Public
License)`. Tato licence nejenže umožňuje software použít k libovolným
účelům včetně komerčních, dovoluje také studovat jeho zdrojový kód,
upravovat ho a tyto změny či opravy šířit dál.

.. Softwarové knihovny systému GRASS a jeho nástroje (tzv. *moduly*) jsou z větší
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
=====

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | První kroky                    | Základní pojmy                 |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   instalace/index              |   raster/index                 |
   |   intro/prvni-kroky            |   vector/index                 |
   |   intro/struktura-dat          |   intro/region                 |
   |   intro/zobrazeni-geodat       |                                |
   |   intro/moduly                 |                                |
   +--------------------------------+--------------------------------+

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   |  Dotazování                    |                                |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   intro/interaktivni-dotazovani|   intro/atributove-dotazy      |
   |                                |   intro/prostorove-dotazy      |
   +--------------------------------+--------------------------------+

Rastrové analýzy
================

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   raster/statistika            |   raster/reklasifikace         |
   |   raster/mask                  |   raster/rastrova-algebra      |      
   |   raster/tabulka-barev         |   raster/analyzy-povrhu        |
   |                                |   raster/analyza-nakladu       |
   +--------------------------------+--------------------------------+

Vektorové analýzy
=================

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   vector/editace               |   vector/atributy              |        
   |   vector/prostorove-funkce     |   vector/sitove-analyzy        |
   |   vector/topologie             |                                |        
   +--------------------------------+--------------------------------+

Další témata
============

.. table::
   :class: toc

   +--------------------------------+--------------------------------+
   |  Geodata                       | Mapové výstupy                 |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   intro/import                 |   misc/mapove-elementy         |
   |   intro/export                 |   misc/mapove-vystupy          |
   |   intro/prenos-dat             |                                |
   |   intro/tvorba-lokace          |                                |
   |   intro/transformace           |                                |
   |   misc/georeferencovani        |                                |
   +--------------------------------+--------------------------------+

.. table::
   :class: toc
        
   +--------------------------------+--------------------------------+
   |  Různé                         |                                |
   +================================+================================+
   | .. toctree::                   | .. toctree::                   |
   |   :maxdepth: 1                 |   :maxdepth: 1                 |
   |                                |                                |
   |   misc/graficky-modeler        |   misc/lokalizace              |
   +--------------------------------+--------------------------------+

Související materiály
=====================

*Česky:*

* `Školení GRASS GIS na Les-ejk.cz <http://les-ejk.cz/skoleni/grass/>`_
* `GRASS GIS na portálu FreeGIS <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS>`_

*Anglicky:*

* `Dokumentace systému GRASS 7.0 <http://grass.osgeo.org/grass70/manuals/index.html>`_

*Literatura:*

* `Open Source GIS: A GRASS GIS Approach <http://www.grassbook.org/>`_ (anglicky)
* `GIS GRASS - Praktická rukověť <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Praktick%C3%A1_rukov%C4%9B%C5%A5>`_ (česky, velmi zastaralé)


Technická podpora
=================

* *(česky)* Mailing list `FreeGeoCZ
  <http://freegis.fsv.cvut.cz/gwiki/Emailov%C3%A1_konference_FreeGeoCZ>`_ (obecně Open Source GIS, nikoliv pouze GRASS)
 * `registrace
   <http://mailman.fsv.cvut.cz/mailman/listinfo/freegeocz>`_
 * `archiv <http://mailman.fsv.cvut.cz/pipermail/freegeocz/>`_
* *(anglicky)* Mezinárodní mailing list projektu GRASS GIS (zajímavostí je archiv sahající až do roku 1991!)
 * `registrace <http://lists.osgeo.org/mailman/listinfo/grass-user>`_
 * `archiv <http://lists.osgeo.org/pipermail/grass-user/>`_
   
.. *Komerční podpora v ČR*
           
.. * OpenGeoLabs s.r.o. ``podpora@opengeolabs.cz``

Užitečné odkazy
===============

* http://freegis.fsv.cvut.cz
* http://epsg.io

Licence
=======

.. table::
   :class: noborder

   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | .. image:: _static/cc-by-sa.png  | Text školení je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_. |
   |           :width: 125px          |                                                                                                                                                       |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

*Verze textu školení:* |release| (|today|)
