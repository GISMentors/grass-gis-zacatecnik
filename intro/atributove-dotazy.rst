.. index::
   pair: dotazování; atributové dotazy
   see: atributové dotazy; atributy
   single: g.gui.dbmgr
   single: SQL builder
   single: SQL

.. _atributove-dotazy:

Atributové dotazy
-----------------

Atributové dotazy, tj. výběr geoprvků na základě jejich popisných
vlastností, lze provádět pomocí `správce atributových dat`.

.. noteadvanced::
   
   Pokročilejší uživatelé mohou ve svých skriptech využít
   specializované moduly ze skupiny ``db.*``, viz kapitola
   :ref:`db-select`.

.. _wxgui-dbmgr:

:grasscmd:`Správce atributových dat <wxGUI.dbmgr>` (*Attribute Table
Manager*) je základním nástrojem pro práci s atributovými daty v
:abbr:`GUI (Grafické uživatelské rozhraní)` systému GRASS. Lze jej
spustit z nástrojové lišty *správce vrstev* |grass-table| :sup:`Show
attribute data for selected vector map` anebo z kontextového menu:

.. figure:: images/wxgui-dbmgr-menu.png

   Spuštění správce atributových dat z kontextového menu.

.. noteadvanced::
      
   Správce atributových dat lze spustit i z příkazové řádky jako modul
   :grasscmd:`g.gui.dbmgr`:

   .. code-block:: bash

      g.gui.dbmgr map=okresy

Dialogové okno správce atributových dat má *tři záložky*:

:item:`Browse data`
      Prohlížení, dotazování a :ref:`editace
      <editace-atributovych-dat>` atributových dat (záznamů v tabulce)

:item:`Manage tables`
      Přidání, přejmenování, odebraní sloupce v atributové tabulce

:item:`Manage layers`
      Správa atributových tabulek připojených k
      vektorové mapě. Tato problematika je ale nad rámec tohoto
      školení a je probírána v navazující :skoleni:`školení pro
      pokročilé uživatele <grass-gis-pokrocily>`.

Dotazování
^^^^^^^^^^

Dotazovat se na atributová data je možné v záložce :item:`Browse data`
a to buď v základním (*Simple*) anebo interaktivním (*Builder*) módu,
viz kapitola :ref:`sql-builder`.

*Základní mód* umožňuje definovat jednoduchou `where` podmínku typu
``sloupec <operator> hodnota``.

.. figure:: images/wxgui-dbmgr-simple-0.png

   Jednoduchý atributový doraz (krok 1 - výběr sloupce pro where
   podmínku).

.. figure:: images/wxgui-dbmgr-simple-1.png

   Jednoduchý atributový doraz (krok 2 - výběr operátoru pro where
   podmínku).

.. figure:: images/wxgui-dbmgr-simple-2.png

   Jednoduchý atributový doraz (krok 3 - určení hodnoty pro where
   podmínku).

.. raw:: latex

   \clearpage

.. figure:: images/wxgui-dbmgr-simple-3.png
   :class: large
        
   Jednoduchý atributový doraz. Výsledek dotazu je automaticky
   zvýrazněn i mapovém okně.
            
.. note:: Vybírat vektorové geoprvky na základě jejich atributů lze i
          pomocí modulu :grasscmd:`v.extract`, více informací v
          kapitole :ref:`v-extract`.

.. tip:: Výběr lze zrušit přes tlačítko :item:`Clear`.

.. _sql-builder:

SQL Builder
^^^^^^^^^^^

*Interaktivní* (Builder) mód umožňuje zadat :abbr:`SQL (Structured Query
Language)` SELECT dotazy přímo.

.. figure:: images/wxgui-dbmgr-adv-edit.png

   Pokročilé dotazování, :abbr:`SQL (Structured Query Language)`
   SELECT dotaz (výběr se provede pro stisknutí klávesy :kbd:`Enter`).

:abbr:`SQL (Structured Query Language)` dotaz lze sestavit pohodlně
pomocí *SQL Builderu*:

.. figure:: images/wxgui-dbmgr-sq-0.png

.. figure:: images/wxgui-dbmgr-sq-1.png
            :class: large
            :scale-latex: 85
                 
            Správce atributových dat a sestavení dotazu v okně SQL
            Builderu.

.. raw:: latex

   \newpage
