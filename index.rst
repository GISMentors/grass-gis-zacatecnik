.. only:: latex
                         
   Obsah
   =====

####   
Úvod
####

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

GRASS GIS (http://grass.osgeo.org) je *free software* a *open source*
publikovaný pod všeobecnou licencí GNU :abbr:`GPL (General Public
License)`. Tato licence nejenže umožňuje software použít k libovolným
účelům včetně komerčních, dovoluje také studovat jeho zdrojový kód,
upravovat ho a tyto změny či opravy šířit dál.

.. Softwarové knihovny systému GRASS a jeho nástroje (tzv. *moduly*) jsou z větší
   části implementovány v programovacím jazyce :abbr:`ANSI (American
   National Standards Institute)` :wikipedia:`C <Programovací jazyk
   C>`. Několik málo modulů je potom implementováno v programovacím
   jazyce :wikipedia:`C++`, jiné jsou dostupné v podobě skriptů v jazyce
   :wikipedia:`Python`.

.. only:: html

   .. tip::

      Text školení je dostupný i v tisknutelné formě `PDF
      <./skoleni-grass-gis-zacatecnik.pdf>`_.
   
.. warning:: :red:`Toto je pracovní verze školení, která je aktuálně ve vývoji!`

.. important:: Školení je zaměřeno na aktuální verzi `GRASS 7.0
               <http://grass.osgeo.org/download/software/#g70x>`_. Ve
               starší verzi GRASS 6.4 není zaručena funkčnost
               uvedených příkladů, případné rozdíly mezi těmito
               verzemi jsou vždy explicitně zdůrazněny. Dále
               předpokládáme zapnutou *anglickou lokalizaci*, viz
               :ref:`volba lokalizace <volba-lokalizace>`.

.. index::
   pair: datové sady; ke stažení

.. note::

   Pro účely školení byl vytvořena vlastní lokace s daty pocházejících
   z otevřených či veřejných zdrojů jako je `EU-DEM
   <http://www.eea.europa.eu/data-and-maps/data/eu-dem>`_, `RÚIAN
   <http://www.cuzk.cz/ruian/RUIAN.aspx>`_, `OpenStreetMap
   <http://wiki.openstreetmap.org/wiki/Main_Page>`_ a `Dibavod
   <http://www.dibavod.cz/>`_.

   **GRASS lokace pro školení** je stažitelná jako `zip archiv
   <http://training.gismentors.eu/geodata/grass/gismentors.zip>`_ (830
   MB), družicové snímky `Landsat
   <http://training.gismentors.eu/geodata/grass/gismentors-landsat.zip>`_
   (985 MB).

#####   
Obsah
#####

.. toctree::
   :maxdepth: 2

   intro/index
   raster/index
   vector/index
   data/index
   misc/index

#######   
Dodatky
#######

Související materiály
=====================

.. rubric:: Česky:

* `Školení GRASS GIS na Les-ejk.cz <http://les-ejk.cz/skoleni/grass/>`_
* `GRASS GIS na portálu FreeGIS <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS>`_

.. rubric:: Slovensky:

* `GRASS GIS pre geovedné aplikácie
  <http://staryweb.fns.uniba.sk/fileadmin/user_upload/editors/geog/kfg/Katedra/Studium/Vyuzitie_PC_vo_FGV_2/skripta_burian_et_al_grassgis_2015.zip>`_
              
.. rubric:: Anglicky:

* `Dokumentace systému GRASS 7.0 <http://grass.osgeo.org/grass70/manuals/index.html>`_

.. rubric:: Literatura:

* `Open Source GIS: A GRASS GIS Approach <http://www.grassbook.org/>`_ (anglicky)
* `GIS GRASS - Praktická rukověť <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Praktick%C3%A1_rukov%C4%9B%C5%A5>`_ (česky, velmi zastaralé)

Technická podpora
=================

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
===============

* http://freegis.fsv.cvut.cz
* http://epsg.io
  
O dokumentu
===========

Text dokumentu je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
   :width: 130px
   :scale-latex: 120
              
*Verze textu dokumentu:* |release| (sestaveno |today|)

Autoři
------

Za `GISMentors <http://www.gismentors.cz/>`_:

* `Martin Landa <http://www.gismentors.cz/mentors/landa>`_ ``<martin.landa opengeolabs.cz>``
* `Jáchym Čepický <http://www.gismentors.cz/mentors/cepicky>`_ ``<jachym.cepicky opengeolabs.cz>``

Text dokumentu
--------------

.. only:: latex

   Online HTML verze textu školení je dostupná na adrese:

   * http://training.gismentors.eu/grass-gis-zacatecnik/

Zdrojové texty školení jsou dostupné na adrese:

* https://github.com/GISMentors/grass-gis-zacatecnik
