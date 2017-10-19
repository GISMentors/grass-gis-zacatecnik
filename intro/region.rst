.. raw:: latex

   \newpage

.. index::
   pair: region; výpočetní region
   single: g.region
   pair: rozlišení; prostorové rozlišení

.. _region:

Výpočetní region
----------------

Výpočetní region je dán *hraničními souřadnicemi* (sever, jih, východ,
západ) a *prostorovým rozlišením* ve směru sever-jih,
východ-západ. Vzniká tak pravidelná mřížka jejíž buňky mají čtvercový
(prostorové rozlišení ve směru sever-jih a~východ-západ totožnou
hodnotu) nebo obdélníkový tvar, viz :numref:`region2d`.

.. _region2d:
         
.. figure:: images/region2d.png
   :scale-latex: 45
              
   Mřížka výpočetního regionu pro 2D data.

.. note:: Pro 3D data jsou definovány hraniční souřadnice a
   prostorové rozlišení navíc ve vertikálním směru (top-bottom).
          
.. important:: Veškeré rastrové operace jsou v systému GRASS prováděny
   vždy a pouze v rámci aktuálně nastaveného výpočetního regionu!
   Pouze několik málo nástrojů pro zpracování rastrových dat
   (tj. moduly s prefixem ``r.*``) výpočetní region
   ignorují. Například modul :grassCmd:`r.import` pro import
   rastrových dat. Narozdíl od toho drtivá většina nástrojů pro
   zpracování vektorových dat (``v.*``) ignoruje nastavení výpočetního
   regionu zcela.

.. warning:: V případě, že se hraniční souřadnice a rozlišení
   vstupních rastrových dat liší od nastavení výpočetního
   regionu, jsou vstupní rastrová data před výpočtem
   *převzorkována* do výpočetní mřížky metodou
   :wikipedia:`nejbližšího souseda<Nearest-neighbor
   interpolation>`. Mřížka výstupních rastrových dat vždy
   odpovídají aktuálně nastavenému regionu.

.. important:: Změna pohledu v mapovém okně nemá na nastavení regionu
   žádný vliv. Aktuální rozsah území zobrazené v mapovém okně je
   dostupný ze stavové lišty jako volba :item:`Extent`, viz kapitola
   :ref:`region-kontrola`.

   .. figure:: images/wxgui-mapdisp-status-extent.png
      :class: middle
              
      Rozsah zobrazeného území (extent).

.. _nastaveni-regionu:
          
Nastavení výpočetního regionu
=============================

Ve většině případů stačí nastavit výpočetní region na základě rastrové
či vektorové mapy. Toto nastavení je dostupné z~kontextového menu
*správce vrstev*.

.. raw:: latex

   \newpage

.. figure:: images/wxgui-set-region-from-map.png
   :scale-latex: 45

Zároveň je možné vybrat pro nastavení výpočetního regionu i více
rastrových či vektorových map najednou.

.. figure:: images/wxgui-set-region-from-maps.png
   :scale-latex: 50
              
   Nastavení výpočetního regionu na základě více vybraných mapových vrstev.

.. noteadvanced::

   .. notecmd:: Nastavení regionu na základě rastrové mapy

      .. code-block:: bash

         g.region raster=dmt

   .. notecmd:: Nastavení regionu na základě vektorových map

      .. code-block:: bash
                
         g.region vector=ulice,adresnimista_bod
         
.. tip:: Prostorové rozlišení může být nastaveno pomocí modulu
   :grasscmd:`g.region` explicitně (volba :option:`res`) nebo na
   základě rastrových map (:option:`raster`). Pro vektorové mapy nehraje
   prostorové rozlišení žádnou roli a tudíž pro ně není ani
   definováno.

.. _nastaveni-regionu-mapove-okno:
   
Z nástrojové lišty mapového okna |grass-zoom-more| :sup:`Various
zoom options` lze navíc výpočetní region nastavit podle aktuálního
pohledu či zcela interaktivně.

.. figure:: images/zoom-menu.png
   :class: middle
   :scale-latex: 65
              
Pokročilé nastavení výpočetního regionu
=======================================

Pro manipulaci s výpočetním regionem je určen modul
:grassCmd:`g.region` dostupný z menu :menuselection:`Settings -->
Region --> Set region`. Modul umožňuje nastavit region na základě
existujících rastrových, vektorových map či již dříve uloženého
nastavení (parametr :option:`save`).

V níže uvedeném příkladě nastavíme výpočetní region tak, aby pokrýval
vektorové mapy :map:`ulice` a :map:`adresnimista`. Prostorové
rozlišení je určeno z rastrové mapy :map:`dmt` (záložka :item:`Bounds`
volba :option:`align`).

.. figure:: images/wxgui-g-region-existing.png
   :scale-latex: 40
              
   Nastavení regionu na základě existujících dat.

.. raw:: latex

   \newpage
   
.. figure:: images/wxgui-mapdisplay-region.png
   :class: middle
   :scale-latex: 50
              
   Kontrola nastavení výpočetního regionu v mapovém okně.

Dále je možno nastavit hraniční souřadnice explicitně, např. severní
souřadnici na '1000' (v mapových jednotkách) anebo jako offset
's+1000' (aktuálně nastavená jižní souřadnice + 1000 mapových
jednotek). Podobně je možné explicitně definovat hodnoty prostorového
rozlišení ve směru sever-jih (počet řádků) a východ-západ (počet
sloupců). Pro 3D region ještě prostorové rozlišení ve směru Z-ové osy.

.. notecmd:: Nastavení prostorového rozlišení

   Prostorové rozlišení nastaveno na základě rastrové mapy, hraniční
   souřadnice s offsetem 10km od minimálního ohraničujícího obdélníku
   vektorové mapy.
             
   .. code-block:: bash

      g.region align=dmt vector=ulice n=n+10000 s=s-10000 w=w-10000 e=e+10000

   .. figure:: images/wxgui-mapdisplay-region-offset.png
      :class: middle
      :scale-latex: 50

.. _region-kontrola:

Kontrola výpočetního regionu
============================

Aktuální nastavení výpočetního regionu lze vytisknout pomocí modulu
:grassCmd:`g.region`, viz menu :menuselection:`Settings --> Region -->
Display region`.

.. figure:: images/wxgui-display-region-out.png

   Aktuálně nastavený výpočetní region.

.. notecmd:: Zobrazení aktuálně nastaveného regionu

   .. code-block:: bash
                
      g.region -p

Aktuální nastavení výpočetního regionu lze zobrazit i ve stavové liště
mapového okna (volba :item:`Computational region`).

.. figure:: images/wxgui-mapdisp-statusbar-menu.png
   :class: middle
           
   Volby stavové lišty mapového okna.

.. raw:: latex

   \newpage

Formát::

 souřadnice západ - východ, jih - sever (rozlišení západ-východ, jih-sever)

.. tip::

   Rozsah výpočetního regionu lze v mapovém okně i zobrazit. Hraniční
   souřadnice budou zobrazeny jako linie červené barvy, pokud je
   výpočetní region celou plochou uvnitř aktuálního pohledu. V opačném
   případě budou hranice výpočetního regionu zobrazeny modrou barvou.

   .. figure:: images/wxgui-mapdisp-show-reg.png
      :class: middle

      Zobrazení rozsahu výpočetního regionu v mapovém okně.

.. raw:: latex

   \clearpage
