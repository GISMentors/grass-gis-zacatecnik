.. index::
   single: r.pack
   single: v.pack
   pair: rastrová data; přenos dat
   pair: vektorová data; přenos dat
   
Přenost dat
-----------

GRASS disponuje vlastním formátem pro přenost dat. Zabalit rastrovou
mapu do tohoto formátu umožňuje modul :grasscmd:`r.pack`
(:menuselection:`File --> Export raster map --> Pack raster map`), pro
vektorová data je k dispozici modul :grasscmd:`v.pack`
(:menuselection:`File --> Export vector map --> Pack vector
map`). Rozbalit takto vytvořený soubor (tzv. `pack`) umožňují moduly
:grasscmd:`r.unpack` (:menuselection:`File --> Import raster map -->
Unpack raster map`) a :grasscmd:`v.unpack` (:menuselection:`File -->
Import vector map --> Unpack vector map`).

.. figure:: images/pack-from-gui.png
   :class: large
   :scale-latex: 80

   Zabalení rastrové a vektorové mapy z GUI systému GRASS.

.. figure:: images/unpack-from-gui.png
   :class: middle
   :scale-latex: 55
     
   Funkce rozbalení rastrové či vektorové mapy je dostupné z
   nástrojové lišty správce vrstev.

.. raw:: latex

   \newpage
   
.. important::

   Takto zabalenou rastrovou či vektorovou mapu lze rozbalit pouze v
   lokaci se stejnými souřadnicovým systémem. Pokud tato podmínka není
   splněna, tak rozbalení skončí chybou, viz
   :num:`#r-unpack-proj-match`.

   .. _r-unpack-proj-match:

   .. figure:: images/r-unpack-proj-match.png
      :scale-latex: 55

      Kontrola souřadnicového systému při rozbalení dat.

.. note::

   Takto zabalené mapy jsou samozřejmě multiplatformní a lze je
   přenášet mezi různými operačními systémy, např. z GNU/Linux na MS
   Windows.

Přenos mapsetů či lokací
========================   

Přenášet mapsety či lokace lze snadno, tak že je zabalíme například
pomocí aplikace :wikipedia:`zip <ZIP (souborový formát)>`.

.. important::

   Při přenášení mapsetů platí pouze jedna podmínka. Mapset může být
   umístěn pouze do lokace se stejným souřadnicovým systém. V opačném
   případě dojde k nekozistenci dat, se kterou si GRASS neporadí.
