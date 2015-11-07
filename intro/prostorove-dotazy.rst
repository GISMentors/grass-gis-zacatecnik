.. index::
   pair: dotazování; prostorové dotazy
   single: v.select

Prostorové dotazy
-----------------

Prostorové dotazy, tj. výběr geoprvků na základě jejich prostorových
vztahů, zajišťuje modul :grasscmd:`v.select` (:menuselection:`Vector
--> Feature selection --> Select by another map`).

.. figure:: images/wxgui-v-select-menu.png
            :class: middle

Systém GRASS podporuje následující prostorové operátory:
                    
* *equals* - geoprvky jsou totožné
* *disjoint* - geoprvky jsou prostorově různé 
* *intersects* - geoprvky se prostorově protínají
* *touches* - geoprvky se prostorově dotýkají
* *crosses* - geoprvky se kříží
* *within* - geoprvek je prostorově lokalizován uvnitř jiného geoprvku
* *contains* - geoprvek je prostorově obsažen v jiném geoprvku
* *overlaps* - geoprvky se prostorově překrývají
* *relate* - obecný prostorový vztah definovaný jako vztahová matice

Podrobný popis prostorových operátorů je k nalezení v :wikipedia:`OGC`
specifikaci `Simple Features Access
<http://www.opengeospatial.org/standards/sfa>`_ více informací
specifikaci `zde <http://geo.fsv.cvut.cz/~gin/uzpd/uzpd.pdf#18>`_.

.. note::

   Nativně :grasscmd:`v.select` podporuje pouze jeden prostorový
   operátor: *overlap* - geoprvky se částečně či úplně
   překrývají. Ostatní výše zmíněné operátory jsou implementovány v
   knihovně `GEOS <http://trac.osgeo.org/geos>`_, kterou systém GRASS používá.

.. rubric:: :secnotoc:`Příklad`

Výběr obcí (vektorová mapa :map:`obce_polygon@ruian`), ve kterých je
umístěna alespoň jedna (v tomto případě může použít např. prostorový
operátor *contains*) požární stanice (vektorová mapa
:map:`pozarni_stanice@osm`).

.. figure:: images/v-select.png

   Spuštění modulu :grasscmd:`v.select`.

.. figure:: images/wxgui-v-select-result.png
   :class: large
   
   Výsledek prostorového dotazu.

.. youtube:: teA-x-vmXYc

   Příklad dalšího prostorového dotazu - výběr komunikací, které kříží železnice.
