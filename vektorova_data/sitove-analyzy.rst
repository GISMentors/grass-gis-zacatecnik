.. index::
   pair: vektorová data; síťové analýzy
   pair: nejkratší cesta; shortest path
   see: nejkratší cesta; síťové analýzy

.. raw:: latex

   \newpage

Síťové analýzy
--------------

GRASS nabízí řadu modulů pro tzv. *síťové analýzy*. Jedná se o typy
úloh nad síťovým grafem (v tomto případě cestní sítě).

* :grasscmd:`v.net` - správa vektorové sítě
* :grasscmd:`v.net.alloc` - alokace zdrojů (vytvoření podsítí, např. policejní okrsky)
* :grasscmd:`v.net.allpairs` - počítá nejkratší cesty mezi všemi páry uzlů v síti
* :grasscmd:`v.net.bridge` - hledá mosty a artikulační body
* :grasscmd:`v.net.centrality` - zjišťuje centralitu (užitečnost) uzlů v síti
* :grasscmd:`v.net.components` - hledá silné a slabé komponenty v síti (grafu)
* :grasscmd:`v.net.connectivity` - zjišťuje úroveň spojitosti sítě
* :grasscmd:`v.net.distance` - výpočet vzdáleností po síti mezi dvěma skupinami prvků
* :grasscmd:`v.net.flow` - nalezení minimálního toku v síti mezi dvěma skupinami uzlů
* :grasscmd:`v.net.iso` - analýza nákladů pohybu od zdroje
* :grasscmd:`v.net.path` - hledání nejkratší cesty
* :grasscmd:`v.net.salesman` - problém obchodního cestujícího
* :grasscmd:`v.net.spanningtree` - hledá minimální kostru sítě (grafu)
* :grasscmd:`v.net.steiner` - problém minimálního Steinerova stromu
* :grasscmd:`v.net.timetable` - hledá nejkratší cesty s užitím časových plánů
* :grasscmd:`v.net.visibility` - konstrukce grafu viditelnosti
* :grasscmd:`v.net.turntable` - připravovaný modul, v němž bude možné definovat ceny za odbočování v jednotlivých směrech

.. note:: Síťové analýzy jsou založeny na heuristických algoritmech,
    což znamená, že nebude pravděpodobně nalezeno optimální řešení,
    ale pouze suboptimální (kompromis mezi optimálním řešením a
    omezením výpočetního času na přípustnou dobu).

.. raw:: latex

   \newpage
         
Ukázka
======

.. figure:: images/wxgui-vnet.png
   :class: large
   :scale-latex: 90

   Příklad nalezení nejkratší cesty pomocí GUI nástroje pro síťové
   analýzy.
            
.. youtube:: McOrMauPc_I

   Příklad síťových analýz v GUI systému GRASS

.. noteadvanced::

   Je možné rozlišovat směr linie tam *(forward)* a zpět *(backward)*.
   Všechny moduly totiž obsahují parametry, které dovolují definovat ceny
   pro pohyb jednotlivými směry. Zakázané směry jsou reprezentovány
   negativními cenami (např. jednosměrné komunikace, uzavírky silnic,
   atd.).
   
   Příprava dat je náročná a je náplní navazujícího
   `školení pro pokročilé uživatele
   <http://www.gismentors.eu/skoleni/grass-gis.html#pokrocily>`_.

