.. _topologie:

Topologie vektorových dat
-------------------------

Jak již bylo uvedeno v :ref:`úvodní části <import-topologie>`,
vektorová data jsou v prostředí GRASS uložena v topologickém
formátu. Znamená to, že nad nimi můžeme rychleji provádět celou řadu
operací, které v netopologickém formátu jsou daleko náročnější. Toto
je na druhou stranu vyváženo náročnější správou dat a potenciálně
větším nebezpečím jejich poškození.

Pokaždé když je vytvořena nová vektorová mapa či je změněna již
existující mapa, je vždy nově vytvořena topologie vektorových prvků v
mapě. Tu můžeme znovu vybudovat také manuálně modulem
:grasscmd:`v.build`, který můžete spustit z menu
:menuselection:`Vector --> Topology maintenance --> Create or rebuild
topology`.

.. _kopie-vektorove-mapy:

.. note:: Data lze modifikovat (včetně sestavení topologie) pouze v
          aktuálním mapsetu. Pro řešení níže uvedené úlohy nejprve
          pomocí modulu :grasscmd:`g.copy` či z kontextového menu
          správce vrstev (viz obr. níže) si v aktuálním mapsetu
          vytvoříme lokální kopii vektorové mapy :map:`obce_polygon`
          (mapset `ruian`).

          .. figure:: images/vector-make-copy.png
                      
.. figure:: images/v-build-01.png
   :class: large

   Znovu vybudování topologie pro vektorovou mapu :map:`obce_polygon`
   (lokální kopie - :fignote:`1`). Chyby v topologii uložíme do nové
   vektorové mapy :fignote:`(2)`.

.. _oprava-topologie:
           
Oprava topologických chyb
=========================

Pro práci s topologií vektorových dat slouží především modul
:grasscmd:`v.clean` (:menuselection:`Vector --> Topology maintenance
--> Clean vector map`). Tento modul je zásadní v okamžiku, kdy
vektorová mapa obsahuje topologické chyby např. :ref:`po importu dat
<import-topologie>` z formátu Esri Shapefile .

::
   
   WARNING: 3742 areas represent more (overlapping) features, because polygons
         overlap in input layer(s). Such areas are linked to more than 1
         row in attribute table. The number of features for those areas is
         stored as category in layer 2
   6361 input polygons
   Total area: 7.891444e+10 (13448 areas)
   Overlapping area: 4.078277e+02 (3742 areas)
   Area without category: 3.879863e+02 (3327 areas)

Data obsahující topologické chyby je potřeba před dalšími analýzami
opravit. V opačném případě budou výsledkem opět chybová
data. Například v případě spojení polygonů obcí v ČR nevznikne
celistvá plocha reprezentující území ČR, ale několik děr a to díky
mezerami mezi vstupními polygony. Vstupní data v tomto případě
obsahuje nejen překrývající se polygony ale i tzv. mezery.

.. figure:: images/dissolve-errors.png

            Výsledek spojení polygonů obcí nad daty, které obsahují
            topologické chyby

Co se týče polygonových dat, většina topologických chyb může být
opravena odstraněním ploch s relativně malou výměrou, tj. ploch, které
reprezentují části, kde dochází k překryvu či mezerám mezi vstupními
polygony. V našem případě bude stačit odstranit plochy s výměrou menší
než 10km\ :sup:`2`.

.. code-block:: bash

   v.clean input=obce_broken output=obce type=area tool=rmarea thresh=10

.. figure:: images/dissolve-ok.png

            Výsledek spojení polygonů obcí po opravě topologických
            chyb

Tato problematika je více rozebrána na `portálu FreeGIS
<http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Konzistence_vektorov%C3%BDch_dat>`_.
