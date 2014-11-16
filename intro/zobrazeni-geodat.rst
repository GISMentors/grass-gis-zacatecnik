Zobrazení geodat v mapovém okně
-------------------------------
Po spuštění systému GRASS se objeví *správce vrstev* (Layer Manager) a
*mapové okno* (Map Display).

.. note::

   Pokud se GUI z nějaké důvodu spadne, lze ho z příkazové řádky
   nastartovat znovu pomocí příkazu :grasscmd:`g.gui`.

.. figure:: images/grass-gui-launch.png
            :class: large

            Základní komponenty GUI systému GRASS - správce vrstev
            :fignote:`(1)` a mapové okno :fignote:`(2)`.

Rastrová či vektorová data lze do *stromu vrstev* (viz záložka :item:`Map
layers`) přidávat z menu :menuselection:`File --> Map display`, nástrojové lišty či
přímo z příkazové řádky *správce vrstev*.

.. note::

   Pokud se v mapovém okně nezobrazují žádná data, je nutné nastavit
   pohled na aktuálně vybranou mapu.

   .. figure:: images/map-display-full-zoom.png
               :class: middle

               Nastavení pohledu mapového okna na vybranou mapovou vrstvu

   Automatické nastavení pohledu při přidání nové mapové vrstvy lze
   nastavit v :menuselection:`Settings --> Preferences`.

   .. figure:: images/wxgui-settings-autozoom.png

               Nastavení automatické změny pohledu při přidání nové mapové vrstvy

.. noteadvanced::

   Geodata lze vykreslovat z příkazové řádky či skriptů do
   nejrůznějších formátů od PNG, GIF až po SVG či PDF pomocí modulu
   :grasscmd:`d.mon` v kombinaci s :grasscmd:`d.rast` a
   :grasscmd:`d.vect`.

   .. figure:: images/gif-example.gif
               
               Příklad vykreslení série prostorových analýz do formátu
               GIF
                  
Rastrová data
=============

*Rastrovou mapu* lze přidat čtyřmi různými způsoby:

* z nástrojové lišty

.. figure:: images/wxgui-toolbar-raster.png
            
            Přidání rastrové mapy z nástrojové lišty správce vrstev

.. figure:: images/wxgui-d-rast.png

            Volba rastrové mapy

* z menu :menuselection:`File --> Map display --> Add raster`

* pomocí klávesové zkratky :kbd:`Ctrl+Shift+R`

* z příkazové řádky (``Command console``) správce vrstev příkazem :grasscmd:`d.rast`

.. figure:: images/wxgui-console.png

            Příkazová řádka správce vrstev

.. figure:: images/wxgui-console-raster.png

            Přidání rastrové mapy z příkazové řádky správce vrstev

Ostatní mapové vrstvy, které mají rastrový charakter jsou dostupné z
nástrojové lišty nebo z příkazové řádky správce vrstev.

.. figure:: images/wxgui-toolbar-raster-misc.png
            :class: middle

            Přidání ostatních rastrových dat z nástrojové lišty správce vrstev

.. figure:: images/wxgui-toolbar-raster-misc-1.png

            Menu pro přidání rastrových dat

Jde o následující typy rastrových dat:

* 3D rastrová data
* :wikipedia:`RGB` barevná syntéza - příkaz :grasscmd:`d.rgb`
* :wikipedia:`HIS <HSL>` barevná syntéza - příkaz :grasscmd:`d.his`
* :wikipedia-en:`Stínovaný reliéf <Shapeded relief>` - příkaz :grasscmd:`d.shadedmap`
* rastrová mapa, zobrazení směru - příkaz :grasscmd:`d.rast.arrow`
* rastrová mapa, zobrazení hodnot buněk - příkaz :grasscmd:`d.rast.num`

.. figure:: images/wxgui-d-rgb.png
            :class: large

            Příklad barevné syntézy kanálů :wikipedia:`Landsat 5` TM ve skutečných barvách

Vektorová data
==============

Podobně lze přidat *vektorovou mapu*:

* z nástrojové lišty:

.. figure:: images/wxgui-toolbar-vector.png

            Přidání vektorové mapy z nástrojové lišty správce vrstev

.. figure:: images/wxgui-d-vect.png

            Volba vektorové mapy

* z menu :menuselection:`File --> Map display --> Add vector`

* pomocí klávesové zkratky :kbd:`Ctrl+Shift+V`

* z příkazové řádky (``Command console``) správce vrstev příkazem :grasscmd:`d.vect`

.. figure:: images/wxgui-console-vector.png

            Přidání vektorové mapy z příkazové řádky správce vrstev

Ostatní mapové vrstvy, které mají vektorový charakter jsou dostupné z
nástrojové lišty nebo z příkazové řádky správce vrstev.

.. figure:: images/wxgui-toolbar-vector-misc.png
            :class: middle

            Přidání ostatních vektorových dat z nástrojové lišty správce vrstev

.. figure:: images/wxgui-toolbar-vector-misc-1.png
            :class: middle

            Menu pro přidání vektorových dat

Jde o následující typy vektorových dat:

* tématické zobrazení plošných vektorových dat - příkaz :grasscmd:`d.thematic.area`
* zobrazení grafů - :grasscmd:`d.vect.chart`
