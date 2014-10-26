Prostorové dotazy
-----------------

Prostorové dotazy, tj. výběr geoprvků na základě jejich prostorových
vztahů, zajišťuje modul :grasscmd:`v.select`. Nativně tento modul
podporuje pouze jeden prostorový operátor:

* *overlap* - geoprvky se částečně či úplně překrývají

Pokud je GRASS :ref:`zkompilován <kompilace>` s podporou knihovny `GEOS
<http://trac.osgeo.org/geos>`_, tak je množina prostorových operátorů
rozšířena o:

* *equals* - geoprvky jsou totožné
* *disjoint* - geoprvky jsou prostorově různé 
* *intersects* - geoprvky se prostorově protínají
* *touches* - geoprvky se prostorově dotýkají
* *crosses* - geoprvky se kříží
* *within* - vektorový prvek je prostorově lokalizován uvnitř jiného prvku
* *contains* - vektorový prvek je prostorově obsažen v jiném prvku
* *overlaps* - geoprvky se prostorově překrývají
* *relate* - obecný prostorový vztah definovaný jako vztahová matice

Knihovna GEOS implementuje prostorové operátory dle :wikipedia:`OGC`
specifikace `Simple Features Access
<http://www.opengeospatial.org/standards/sfa>`_ více o této
specifikaci `zde <http://geo.fsv.cvut.cz/~gin/uzpd/uzpd.pdf#18>`_.

.. rubric:: :secnotoc:`Příklad`

Výběr komunikací (vektorová mapa :map:`streets_wake`), které kříží (v
tomto případě může použít např. prostorový operátor *crosses*)
železnice (vektorová mapa :map:`railroads`).

.. youtube:: teA-x-vmXYc

             Prostorový dotaz - výběr komunikací, které kříží železnice
