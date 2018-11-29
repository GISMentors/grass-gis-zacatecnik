.. index::
   single: r.pack
   single: v.pack
   pair: rastrová data; přenos dat
   pair: vektorová data; přenos dat
   
Přenost dat mezi lokacemi
-------------------------

Kopírování
==========

GUI umožňuje rastrové či vektorové mapy kopírovat mezi lokacemi v
záložce :item:`Data`.

.. figure:: images/copy-data-tab.png
   :class: large

   Kopírování datových vrstev mezi lokacemi.

.. note:: Při této operaci dochází k transformaci dat i v případě, že
   je souřadnicový systém zdrojové a cílové, tj. *aktuální* lokace
   neliší.

.. figure:: images/copy-data-tab-raster.png
   :class: small

   Při transformaci rastrových dat lze nastavit cílové prostorové
   rozlišení a metodu pro převzorkování.

.. figure:: images/copy-data-tab-vector.png
   :class: small

   Při transformaci vektorových dat lze nastavit maximální délku
   segmentu (v mapových jednotkách).

Výměnný formát (pack)
=====================

GRASS disponuje vlastním formátem pro přenost dat. Zabalit rastrovou
mapu umožňuje modul :grasscmd:`r.pack` (:menuselection:`File -->
Export raster map --> Pack raster map`), pro vektorová data je k
dispozici modul :grasscmd:`v.pack` (:menuselection:`File --> Export
vector map --> Pack vector map`). 

.. figure:: images/pack-from-gui.png
   :class: large
   :scale-latex: 80

   Zabalení rastrové či vektorové mapy z kontextového menu správce
   vrstev.

Rozbalit takto vytvořený archiv
(tzv. `pack`) umožňují moduly :grasscmd:`r.unpack`
(:menuselection:`File --> Import raster map --> Unpack raster map`) a
:grasscmd:`v.unpack` (:menuselection:`File --> Import vector map -->
Unpack vector map`).

.. figure:: images/unpack-from-gui.png
   :scale-latex: 55
     
   Funkce rozbalení rastrové či vektorové mapy je dostupná z
   nástrojové lišty správce vrstev.

.. raw:: latex

   \newpage
   
.. important::

   Takto zabalenou rastrovou či vektorovou mapu lze rozbalit pouze v
   lokaci se stejnými souřadnicovým systémem. Pokud tato podmínka není
   splněna, tak rozbalení skončí chybou.

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

Přenášet mapsety či lokace mezi jednotlivými počítači lze
snadno. Adresář lokace, resp. mapsetu stačí zabalit do klasického
archivu, např. :wikipedia:`zip <ZIP (souborový formát)>`.

.. important::

   Při přenášení mapsetů platí jedna důležitá podmínka. Mapset může
   být umístěn pouze do lokace se stejným souřadnicovým systém. V
   opačném případě dojde k nekozistenci dat, se kterou si GRASS
   neporadí.
