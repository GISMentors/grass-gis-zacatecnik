Editace vektorových dat
-----------------------

Vytvoření nové vektorové mapy
=============================

Novou vektorovou mapu vytvoříme z menu  
:menuselection:`Vector --> Develop vector map --> Create new vector map`.

.. figure:: images/create-vector.png

   Vytvoření nové vektorové mapy

.. noteadvanced::
      
   V dialogovém okně ponecháme název vazby mezi geometrickou částí a
   identifikátorem záznamu v atributové databázi ``cat``.

.. notecmd:: Vytvoření prázdné vektorové mapy

    .. code-block:: bash 
    
        v.edit map=novy_vektor tool=create`

Vytvoření a úprava atributové tabulky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nástroj pro editaci atributové tabulky spustíme z kontextového menu vektorové mapy
:guilabel:`Show attribute data`

.. figure:: images/edit-attributes-01.png
   :class: middle
           
   Spuštění tabulky atributů

V záložce :guilabel:`Manage attributes` můžeme přidávat a
přejmenovávat atributové sloupečky, více v sekci :ref:`editace
atributových dat <editace-atributovych-dat>`.

.. figure:: images/attribute-table.png
   :class: middle
           
   Přidání sloupečku s názvem ``popis``


Editace vektorové mapy
======================

Existující vektorovou mapu můžeme začít editovat z kontextového menu 
:guilabel:`Start editing`.

.. figure:: images/edit-vector-01.png
   :class: middle
        
   Start editace vektorových dat
    
Nyní můžeme v mapovém okně zvolit nástroj kreslení linie (nebo kterýkoliv jiný)
a nakreslit požadovaný tvar.

.. note:: Mapové okno bude zobrazovat podkladové mapy, které v něm byly načteny
    dříve

Po ukončení editace geoprvku (pravým tlačítkem) se objeví formulář pro vyplnění
atributů

.. figure:: images/edit-vector-02.png

    Definice atributů pro nově vytvořený vektorový geoprvek

Počáteční a koncové body linií a ploch se budou na sebe přichytávat
(výchozí hodnota je `10px`). Počáteční a koncové body linií a polygonů
jsou vykresleny různou barvou, podle toho jsou-li přichyceny k dalšímu
bodu či nikoliv.

Při editaci ploch je každá plocha automaticky *zaplochována* centroidem. K
centroidu se naváží požadované atributy. Hranice plochy a jejich centroidy lze
editovat i zvlášť.

Mazání vybraných geoprvků je potřeba vždy potvrdit pravým tlačítkem myši.

Přiřazování atributů novým prvkům
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V nastavení editace můžeme nastavit zobrazení editovaných prvků (šířka, barvy),
snapping, automatické přiřazování atributů novým prkvům, a další.

.. figure:: images/editing-settings.png

    Nastavení editace

.. noteadvanced:: Editovat vektorové objekty lze také v příkazové řádce pomocí modulu
    :grassCmd:`v.edit` 
