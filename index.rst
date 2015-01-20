.. only:: latex
                         
   Obsah
   =====

Úvod
====

.. only:: html

   .. image:: images/grass-logo.png
      :width: 140px
      :align: left

.. index::
   single: GIS
   single: geografický informační systém
       
**GRASS** (Geographic Resources Analysis Support System) je
multiplatformní desktopový *geografický informační systém*
(:wikipedia:`GIS`) určený pro správu geografických 2D/3D rastrových a
vektorových dat, obrazových záznamů, produkci vysoce kvalitních
grafických výstupů, časoprostorové modelování a vizualizaci dat.

.. only:: latex

   .. figure:: images/grass-logo.png
      :scale-latex: 80

      Logo projektu GRASS GIS

.. index::
   pair: free software; open source
   single: GNU
   pair: GPL; General Public License

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
               <http://grass.osgeo.org/download/software/#g70x>`_. Nicméně
               pokud není uvedeno jinak, tak všechny uvedené postupy
               jsou funkční i ve verzi GRASS 6.4. Případné rozdíly mezi
               těmito verzemi jsou vždy explicitně zdůrazněny. Dále
               předpokládáme zapnutou *anglickou lokalizaci*,
               viz :ref:`volba lokalizace <volba-lokalizace>`.

První kroky
===========
          
.. toctree::
   :maxdepth: 1

   instalace/index
   intro/prvni-kroky
   intro/struktura-dat
   intro/zobrazeni-geodat
   intro/moduly

Základní pojmy
==============

.. toctree::
   :maxdepth: 1
	      
   raster/index
   vector/index 
   intro/region
   
Dotazování
==========

.. toctree::
   :maxdepth: 1

   intro/interaktivni-dotazovani
   intro/atributove-dotazy
   intro/prostorove-dotazy

Rastrové analýzy
================

.. toctree::
   :maxdepth: 1
	      
   raster/statistika
   raster/mask
   raster/tabulka-barev
   raster/analyzy-povrchu
   raster/rastrova-algebra
   raster/reklasifikace
   raster/analyza-nakladu

Vektorové analýzy
=================

.. toctree::
   :maxdepth: 1

   vector/editace
   vector/prostorove-funkce
   vector/topologie
   vector/atributy
   vector/sitove-analyzy
                 
Import, export geodat
=====================
          
.. toctree::
   :maxdepth: 1
	      
   intro/import
   intro/export
   intro/prenos-dat
   intro/tvorba-lokace
   intro/transformace
   misc/georeferencovani
         
Mapové výstupy
==============

.. toctree::
   :maxdepth: 1
                 
   misc/mapove-elementy
   misc/mapove-vystupy

Různé
=====

.. toctree::
   :maxdepth: 1
	      
   misc/graficky-modeler
   misc/lokalizace

          
Dodatky
=======

Související materiály
---------------------

.. rubric:: Česky:

* `Školení GRASS GIS na Les-ejk.cz <http://les-ejk.cz/skoleni/grass/>`_
* `GRASS GIS na portálu FreeGIS <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS>`_

.. rubric:: Anglicky:

* `Dokumentace systému GRASS 7.0 <http://grass.osgeo.org/grass70/manuals/index.html>`_

.. rubric:: Literatura:

* `Open Source GIS: A GRASS GIS Approach <http://www.grassbook.org/>`_ (anglicky)
* `GIS GRASS - Praktická rukověť <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Praktick%C3%A1_rukov%C4%9B%C5%A5>`_ (česky, velmi zastaralé)

Technická podpora
-----------------

* *(česky)* Mailing list `FreeGeoCZ
  <http://freegis.fsv.cvut.cz/gwiki/Emailov%C3%A1_konference_FreeGeoCZ>`_ (obecně Open Source GIS, nikoliv pouze GRASS)

  * `registrace <http://mailman.fsv.cvut.cz/mailman/listinfo/freegeocz>`_
  * `archiv <http://mailman.fsv.cvut.cz/pipermail/freegeocz/>`_
  
* *(anglicky)* Mezinárodní mailing list projektu GRASS GIS (zajímavostí je archiv sahající až do roku 1991!)
       
  * `registrace <http://lists.osgeo.org/mailman/listinfo/grass-user>`_
  * `archiv <http://lists.osgeo.org/pipermail/grass-user/>`_
   
.. *Komerční podpora v ČR*
           
.. * OpenGeoLabs s.r.o. ``podpora@opengeolabs.cz``

Užitečné odkazy
---------------

* http://freegis.fsv.cvut.cz
* http://epsg.io
  
Licence dokumentu
-----------------

Text školení je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
   :scale: 60
   :scale-latex: 100
              
*Verze textu školení:* |release| (|today|)

Autoři
^^^^^^

Za `GISMentors <http://www.gismentors.eu/>`_:

* Martin Landa ``<martin.landa opengeolabs.cz>``
* Jáchym Čepický ``<jachym.cepicky opengeolabs.cz>``
