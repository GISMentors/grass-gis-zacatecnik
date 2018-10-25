Zobrazení geodat v mapovém okně
-------------------------------

.. index::
   single: správce vrstev
   single: mapové okno
   single: g.gui

Po spuštění grafického uživatelského rozhraní (GUI) systému GRASS se
objeví *správce vrstev* (Layer Manager) a *mapové okno* (Map Display).

.. tip::

   Pokud GUI systému GRASS z nějaké důvodu zhavaruje, lze ho z
   příkazové řádky nastartovat znovu pomocí příkazu :grasscmd:`g.gui`.

   .. code-block:: bash

      g.gui

.. figure:: images/grass-gui-launch.png
            :class: large
            :scale-latex: 85
                 
            Základní komponenty GUI systému GRASS - správce vrstev
            :fignote:`(1)` a mapové okno :fignote:`(2)`.

Rastrová či vektorová data lze do *správce vrstev* (záložka
:item:`Layers`) přidávat z menu :menuselection:`File --> Map display`,
nástrojové lišty či přímo z příkazové řádky *správce vrstev* (záložka
:item:`Console`), viz :ref:`níže <zobrazeni-dat-raster>`.

.. raw:: latex

   \newpage
         
.. tip::

   Pokud se v mapovém okně po přidání vrstvy nezobrazují žádná data,
   je nutné nastavit pohled na aktuálně vybranou mapovou vrstvu
   |grass-zoom-extent| :sup:`Zoom to selected map
   layer(s)`. Automatické nastavení pohledu při přidání každé nové
   mapové vrstvy lze kontrolovat v nastavení |grass-settings|
   :sup:`GUI Settings` anebo z menu :menuselection:`Settings -->
   Preferences`.

   .. figure:: images/wxgui-settings-autozoom.png
      :scale-latex: 50
      
      Nastavení automatické změny pohledu při přidání nové mapové vrstvy.

.. noteadvanced::

   Geodata lze vykreslovat z příkazové řádky či skriptů do
   nejrůznějších formátů od PNG, GIF až po SVG či PDF pomocí modulu
   :grasscmd:`d.mon` v kombinaci s moduly :grasscmd:`d.rast` a
   :grasscmd:`d.vect`. Tyto techniky jsou součástí navazujícího
   :skoleni:`školení pro pokročilé uživatele <grass-gis-pokrocily>`.

   .. only:: html
             
      .. figure:: images/gif-example.gif
         :class: middle
                    
         Příklad vykreslení série prostorových analýz do formátu
         GIF

.. index::
   pair: zobrazení dat; rastrová data
   single: d.rast

.. _zobrazeni-dat-raster:
               
Rastrová data
=============

Rastrová data (v terminologii systému GRASS tzv. *rastrovou mapu*) lze
přidat do správce vrstev, resp. mapového okna různými způsoby:

#. ze záložky :item:`Data` správce vrstev

   .. figure:: images/wxgui-data-display-rast.png

      Zobrazit rastrovou mapu lze z kontextového menu :item:`Display
      layer` anebo jednoduše od verze GRASS GIS 7.4.1 i dvojklikem.
               
#. tradičně z nástrojové lišty správce vrstev |grass-layer-raster-add|
   :sup:`Add raster map layer`

   .. figure:: images/wxgui-d-rast.png
               :scale-latex: 50
                    
               Volba rastrové mapy.

#. z menu :menuselection:`File --> Map display --> Add raster`

#. pomocí klávesové zkratky :kbd:`Ctrl+Shift+R`

#. z příkazové řádky (``Console``) správce vrstev příkazem :grasscmd:`d.rast`

   .. figure:: images/wxgui-console.png

               Příkazová řádka správce vrstev.

   .. figure:: images/wxgui-console-raster.png

               Přidání rastrové mapy z příkazové řádky správce vrstev.

Ostatní mapové vrstvy, které mají rastrový charakter jsou dostupné z
nástrojové lišty |grass-layer-raster-more| :sup:`Add various raster
map layers (RGB, HIS, shaded relief, ...)` nebo z příkazové řádky
správce vrstev.

.. figure:: images/wxgui-toolbar-raster-misc-1.png
            :scale-latex: 50
      
            Menu pro přidání rastrových dat.

.. _d-rast-various:

Jde o následující typy rastrových dat:

* 3D rastrová data
* :wikipedia:`RGB` barevná syntéza - příkaz :grasscmd:`d.rgb`
* :wikipedia:`HIS <HSL>` barevná syntéza - příkaz :grasscmd:`d.his`
* :wikipedia-en:`stínovaný reliéf <Shaded relief>` - příkaz :grasscmd:`d.shade`, viz kapitola :ref:`Stínovaný reliéf <display-shade>`
* rastrová mapa, zobrazení směru - příkaz :grasscmd:`d.rast.arrow`
* rastrová mapa, zobrazení hodnot buněk - příkaz :grasscmd:`d.rast.num`

.. figure:: images/wxgui-d-rgb.png
            :class: large
            :scale-latex: 65
                 
            Příklad zobrazení barevné syntézy kanálů
            :wikipedia:`Landsat 8 ETM <Landsat>` z mapsetu "landsat"
            ve skutečných barvách.

.. index::
   pair: zobrazení dat; vektorová data
   single: d.vect

Vektorová data
==============

Podobně lze přidat vektorová data (tzv. *vektorovou mapu*):

#. ze záložky :item:`Data` správce vrstev

   .. figure:: images/wxgui-data-display-vect.png

      Zobrazit vektorovou mapu lze z kontextového menu :item:`Display
      layer` anebo jednoduše od verze GRASS GIS 7.4.1 i dvojklikem.
               
#. tradičně z nástrojové lišty správce vrstev |grass-layer-vector-add|
   :sup:`Add vector map layer`

   .. figure:: images/wxgui-d-vect.png
               :scale-latex: 50
                             
               Volba vektorové mapy.

#. z menu :menuselection:`File --> Map display --> Add vector`

#. pomocí klávesové zkratky :kbd:`Ctrl+Shift+V`

#. z příkazové řádky (``Console``) správce vrstev příkazem
   :grasscmd:`d.vect`

   .. figure:: images/wxgui-console-vector.png
               
               Přidání vektorové mapy z příkazové řádky správce vrstev.

Ostatní mapové vrstvy, které mají vektorový charakter jsou dostupné z
nástrojové lišty |grass-layer-vector-more| :sup:`Add various raster
map layers (thematic, chart, ...)` nebo z příkazové řádky správce
vrstev.

.. figure:: images/wxgui-toolbar-vector-misc-1.png
	    :class: middle
            :scale-latex: 65

            Menu pro přidání vektorových dat.

Jde o následující typy vektorových dat:

* tématické zobrazení plošných vektorových dat - příkaz
  :grasscmd:`d.thematic.area`
* zobrazení grafů - :grasscmd:`d.vect.chart`
