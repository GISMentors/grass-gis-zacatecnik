.. index::
   single: mapové elementy

.. _mapove-elementy:

Mapové elementy
---------------

Do mapové okna lze přidat základní mapové elementy jako je *legenda*,
*směrová růžice*, *měřítko* či *textový popisek*. Tato funkcionalita
je dostupná z nástrojové lišky mapového okna.

.. figure:: images/add-map-element.png
   :class: large
   :scale-latex: 50
			  
   Mapové elementy.

.. note::

   Mapové okno není určeno pro tvorbu plnohodnotných mapových
   výstupů. K tomuto účelu je určen :grasscmd:`Cartographic Composer
   <wxGUI.psmap>`, více v kapitole :ref:`mapové výstupy
   <mapove-vystupy>`.

.. index::
   pair: mapové elementy; legenda
   single: d.legend

.. _map-legend:

Legenda
=======

Legendu pro rastrová data lze do mapového okna přidat z jeho nástroje
lišty.

.. figure:: images/add-legend.png
   :class: middle
   :scale-latex: 65

   Přidání legendy rastrových mapových vrstev do mapového okna.

.. raw:: latex
            
   \newpage

.. figure:: images/add-legend-0.png

   Pokud je ve *správci vrstev* aktuálně vybraná rastrová mapa, tak se
   automaticky legenda zobrazí pro ni.

.. figure:: images/add-legend-1.png
   :class: large
   :scale-latex: 75

   Zobrazená legenda rastrové mapy.

Legendu můžete v mapovém okně **skrýt** z kontextového menu legendy
(pravé tlačítko myši nad legendou):
                     
.. figure:: images/remove-legend.png
   :class: small
   :scale-latex: 50

   Skrytí legendy.

Z tohoto menu lze také **změnit velikost** legendy i její orientaci.

.. raw:: latex

   \newpage

.. figure:: images/resize-legend-0.png
   :scale-latex: 50
   
   Změna velikosti legendy.

.. figure:: images/resize-legend-1.png
   :class: small
           
   Příklad změněné orientace legendy.

**Vlastnosti legendy** můžeme změnit z dialogu modulu
:grasscmd:`d.legend` dostupného pomocí dvojkliku nad legendou
umístěnou v mapovém okně.

.. figure:: images/legend-prop-flip.png
   :class: middle
   :scale-latex: 50

   Přiklad změny legendy - otočení škály.

.. figure:: images/legend-flip.png
   :class: small

   Výsledek otočení škály legendy.

.. note::

   Podobně lze přidat do mapového okna legendu pro vektorová data.
   
.. raw:: latex

   \newpage

.. tip::

   Pokud se popisky legenda nezobrazují korektně, je potřeba změnit
   font legendy.

   .. figure:: images/legend-broken.png
      :class: small
      :scale-latex: 40

      Chybně vykreslená legenda.
      
   Písmo změníme v dialogu nastavení dostupného z menu
   :menuselection:`Settings --> Preferences` anebo z nástrojové lišty
   *správce vrstev* |grass-settings| :sup:`GUI settings`.

   .. figure:: images/settings-font.png            
      :class: middle
      :scale-latex: 60

      V záložce :item:`Map display` zvolíme vhodný font.

   .. figure:: images/font-dialog.png
      :class: small
      :scale-latex: 40
                 
      Kromě typu písma změníme kodóvání na UTF-8.

   Pokud se změna v nastavení neprojevuje, tak mapové okno překreslíme
   |grass-layer-redraw| :sup:`Render map`.
   
   .. raw:: latex

      \newpage

   .. figure:: images/legend-ok.png
      :class: small
      :scale-latex: 35

      Výsledek po změně nastavení písma.

.. index::
   pair: mapové elementy; směrová růžice
   single: d.northarrow

Směrová růžice
==============

Směrovou růžici lze do mapového okna přidat z jeho nástroje lišty:

.. figure:: images/add-narrow.png
   :class: middle
   :scale-latex: 70

   Přidání směrové růžice do mapového okna.

Do mapové okna se umístí výchozí směrová růžice:

.. figure:: images/narrow.png
            :class: small
	    :scale-latex: 50

	    Příklad směrové růžice.
	    
**Podobu směrové růřice** lze změnit z dialogu modulu
:grasscmd:`d.northarrow` přes dvojklik nad směrovou růžicí umístěnou v
mapovém okně.

.. figure:: images/narrow-prop.png
   :class: middle
   :scale-latex: 55

   Příklad změny stylu směrové růžice.

.. figure:: images/narrow-1.png
   :class: small
   :scale-latex: 50

   Výsledek změny stylu směrové růžice.

.. raw:: latex
	 
   \newpage
	 
Směrovou růžici můžete v mapovém okně **skrýt** z kontextového menu
směrové růžice (pravé tlačítko myši nad směrovou růžicí):
                     
.. figure:: images/remove-narrow.png
   :class: small
   :scale-latex: 50

   Skrytí směrové růžice.

.. index::
   pair: mapové elementy; měřítko
   single: d.barscale

Měřítko
=======

Měřítko lze do mapového okna přidat z jeho nástroje lišty:

.. figure:: images/add-scalebar.png
   :class: middle
   :scale-latex: 60

   Přidání měřítka do mapového okna.

Do mapové okna se umístí výchozí měřitko:

.. figure:: images/scalebar.png
   :class: small
   :scale-latex: 60

   Vychozí měřítko.
   
**Podobu měřítka** lze změnit z dialogu modulu :grasscmd:`d.barscale`
přes dvojklik nad měřítkem umístěným v mapovém okně.

.. figure:: images/scalebar-prop.png
   :class: middle
   :scale-latex: 40
     
   Příklad změny stylu měřítka.

.. figure:: images/scalebar-1.png
   :class: small
   :scale-latex: 50

   Výsledek změny stylu měřítka.

.. raw:: latex

   \newpage

Měřítko můžete v mapovém okně **skrýt** z kontextového menu měřítka
(pravé tlačítko myši nad měřítkem):
                     
.. figure:: images/remove-scalebar.png
   :class: small
   :scale-latex: 50

   Skrytí měřítka.

.. index::
   pair: mapové elementy; textový popisek
   single: d.text

Textový popisek
===============

Textový popisek lze do mapového okna přidat z jeho nástroje lišty:

.. figure:: images/add-text.png
   :class: middle
   :scale-latex: 65

   Přidání textového popisku do mapového okna.
   
V následující dialogu modulu :grasscmd:`d.text` uvedeme text. Případně
můžeme v záložce :item:`Font settings` můžeme nastavit velikost a typ
písma.
      
.. figure:: images/text-prop.png
        
   Po nastavení textu v dialogu :grasscmd:`d.text`.

.. figure:: images/text-example.png
   :class: large
   :scale-latex: 80

   Příklad textového popisku v mapovém okně.
            
Popisek lze **skrýt** z kontextového menu textového objektu.

.. figure:: images/remove-text.png
   :class: small
   :scale-latex: 50
              
   Odstranění textového popisku z mapového okna.
