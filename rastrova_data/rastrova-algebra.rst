.. index::
   pair: algebra; rastrová algebra
   pair: algebra; mapová algebra
   single: r.mapcalc
   see: mapová algebra; r.mapcalc

.. _rastrova-algebra:

Rastrová algebra
----------------

Základním nástrojem pro rastrovou algebru je v systému GRASS modul
:grasscmd:`r.mapcalc`. Jeho grafická nadstavba - **Rastrový kalkulátor**
je dostupný z menu :menuselection:`Raster --> Raster Map Calculator`
anebo z nástrojové lišty *správce vrstev* |grass-raster-calculator|
:sup:`Raster Map Calculator`.

Postup
======

#. zadání výstupní rastrové mapy
#. zadání výrazu pro :grasscmd:`r.mapcalc`
#. spuštění vypočtu

.. raw:: latex

   \newpage
   
.. figure:: images/grass-r-mapcalc-dialog.png
   :scale-latex: 50

   Dialog rastrového kalkulátoru.

.. figure:: images/grass-r-mapcalc-report.png
   :class: large
   :scale-latex: 90

   Příklad určení výměry území s nadmořskou výšku větší než 700 metrů.

.. tip:: Zvolenou hodnotu ve výstupní rastrové mapě lze nahradit
         hodnotou NULL (no-data) pomocí kombinace funkcí ``if()`` a
         ``null()``. Např. výrazem

         ::

            if( dmt > 700, 1, null() )

         vytvoříme rastrovou mapu s hodnotami 1 a NULL (žádná data).

..         
   .. youtube:: zADAJD3sytI

   Příklad výběru oblasti s nadmořskou výškou větší než 1000m.

.. noteadvanced::
   
   .. notecmd:: Použití 

      Modul :grassCmd:`r.mapcalc` lze spustit z příkazové řádky
      podobně jako ostatní moduly systému GRASS. Výraz pro výpočet
      může být předán jako parametr :option:`expression`, např.

      .. code-block:: bash

         r.mapcalc expression="dmt_1000 = if(dmt > 1000, 1, null())"
    
      Výrazy lze uložit také do souboru (na každý řádek jeden výraz) a soubor
      předat jako parametr :option:`file`.
   
      .. code-block:: bash
                   
         r.mapcalc file=vyrazy.txt
                   
      V tomto případě :grasscmd:`r.mapcalc` vykoná příkazy sekvenčně,
      tak jak jsou uloženy v souboru.
