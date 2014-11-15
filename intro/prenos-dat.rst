Přenost dat
-----------

GRASS disponuje vlastním formátem pro přenost dat. Zabalit rastrovou
mapu do tohoto formátu umožňuje modul :grasscmd:`r.pack`
(:menuselection:`File --> Export raster map --> Pack raster map`), pro
vektorová data je k dispozici modul :grasscmd:`v.pack`
(:menuselection:`File --> Export vector map --> Pack vector
map`). Rozbalit takto vytvořený soubor (tzv. `pack`) umožňují modulu
:grasscmd:`r.unpack` (:menuselection:`File --> Import raster map -->
Unpack raster map`) a :grasscmd:`v.unpack` (:menuselection:`File -->
Import vector map --> Unpack vector map`).

.. figure:: images/pack-from-gui.png
   :class: large
           
   Zabalení rastrové a vektorové mapy z GUI systému GRASS.

.. figure:: images/unpack-from-gui.png
   :class: middle
        
   Funkce rozbalení rastrové či vektorové mapy je dostupné z
   nástrojové lišty správce vrstev

.. important::

   Takto zabalenou rastrovou či vektorovou mapu lze rozbalit pouze v
   lokaci se stejnými souřadnicovým systémem. Pokud tato podmínka není
   splněna, tak rozbalení skončí chybou, viz obr. níže.

   .. figure:: images/r-unpack-proj-match.png

.. note::

   Takto zabalené mapy jsou samozřejmě multiplatformní a lze je
   přenášet mezi různými operačními systémy, např. GNU/Linux na MS
   Windows.

Ṕřenos mapsetů či lokací
========================   

Přenášet mapsety či lokace lze snadno, tak že je zabalíme napřílad
pomocí aplikace :wikipedia:`zip <ZIP (souborový formát)>`.

.. important::

   Při přenášení mapsetů platí pouze jedna podmínka. Mapset může být
   umístěn pouze do lokace se stejným souřadnicovým systém. V opačném
   případě dojde k nekozistenci se kterou si GRASS neporadí.
