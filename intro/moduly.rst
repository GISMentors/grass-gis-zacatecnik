Příkazy systému GRASS
---------------------

.. index::
   single: moduly

GRASS GIS je *modulární systém*, který disponuje poměrně rozsáhlou
množinou malých, ale výkonných programů (v~terminologii systému GRASS
*modulů*).

.. note::
   
   To odpovídá koncepci :wikipedia:`Unixu <Unix>` jako
   takového. Daný program má za úkol vyřešit dílčí problém, měl by být co
   nejmenší a poměrně jednoduchý.

Jednotlivé příkazy systému GRASS - moduly - mají konzistentní syntaxi,
jejich názvy se skládají z předpony označující skupinu příkazů a
krátkého názvu napovídající účel modulu (viz tabulka níže). Například
modul :grasscmd:`v.buffer` patří do skupiny *vector* a je určen pro
vytvoření obalové zóny (tzv. bufferu) nad vektorovými daty.

.. only:: latex
          
   .. tabularcolumns:: |p{1.5cm}|p{2cm}|p{8cm}|
                       
.. only:: html
                                 
   .. cssclass:: border

+----------+--------------------------------+-----------------------------------------------+
| prefix   | skupina                        | popis                                         |
+==========+================================+===============================================+
| ``db.``  | :grasscmd:`database`           | práce s atributovými daty a tabulkami         |
+----------+--------------------------------+-----------------------------------------------+
| ``d.``   | :grasscmd:`display`            | grafické výstupy a vizuální dotazy            |
+----------+--------------------------------+-----------------------------------------------+
| ``g.``   | :grasscmd:`general`            | obecné příkazy pro manipulaci s daty          |
+----------+--------------------------------+-----------------------------------------------+
| ``i.``   | :grasscmd:`imagery`            | zpracování obrazových dat                     |
+----------+--------------------------------+-----------------------------------------------+
| ``ps.``  | :grasscmd:`postscript`         | tvorba mapových výstupů ve formátu PostScript |
+----------+--------------------------------+-----------------------------------------------+
| ``r.``   | :grasscmd:`raster`             | zpracování (2D) rastrových dat                |
+----------+--------------------------------+-----------------------------------------------+
| ``r3.``  | :grasscmd:`raster3D`           | zpracování 3D rastrových dat (voxels)         |
+----------+--------------------------------+-----------------------------------------------+
| ``v.``   | :grasscmd:`vector`             | zpracování 2D/3D vektorových dat              |
+----------+--------------------------------+-----------------------------------------------+

Příkazy systému GRASS lze spouštět několika způsoby (příklad pro
:grasscmd:`r.buffer`):

#. z menu správce vrstev

   .. _wxgui-menu-r-buffer:

   .. figure:: images/wxgui-menu-r-buffer.png

               Spuštění modulu :grasscmd:`r.buffer` z menu správce vrstev.

#. z nástroje :item:`Search module` správce vrstev

   .. _wxgui-search-r-buffer:
   
   .. figure:: images/wxgui-search-r-buffer.png
               
               Spuštění modulu :grasscmd:`r.buffer` pomocí nástroje :item:`Search module`.

#. z příkazové řádky správce vrstev

   .. _wxgui-console-r-buffer:

   .. figure:: images/wxgui-console-r-buffer.png
	       :class: middle
	       :scale-latex: 90

               Spuštění modulu :grasscmd:`r.buffer` z příkazové řádky správce vrstev.

   Pokud jsou zadány všechny povinné parametry (v případě modulu
   :grasscmd:`r.buffer` jde o parametry :option:`input`,
   :option:`output` a :option:`distances`), tak se modul spustí
   přímo. Pokud tato podmínka není splněna, zobrazí se dialog
   nástroje.

   .. _wxgui-console-r-buffer-launch:
           
   .. figure:: images/wxgui-console-r-buffer-launch.png

               Spuštění modulu :grasscmd:`r.buffer` včetně zadání parametrů.

#. z :doc:`grafického modeleru <../misc/graficky-modeler>`

.. raw:: latex

     \clearpage

.. index::
   pair: moduly; nápověda
   single: g.manual

Nápověda k modulům
==================

Nápověda systému GRASS je dostupná z menu :menuselection:`Help --> GRASS help`.

.. figure:: images/grass-help.png
   :class: large
   :scale-latex: 80
              
   Nápověda systému GRASS v okně webového prohlížeče.

.. notecmd:: Zobrazení nápovědy

   Nápovědu lze spustit pomocí modulu :grasscmd:`g.manual`:

   .. code-block:: bash

      g.manual -i

   .. code-block:: bash
                
      g.manual r.buffer
                   
.. figure:: images/r-buffer-help.png
   :scale-latex: 50

   Nápověda k jednotlivým modulům je dostupná i z dialogového okna.

