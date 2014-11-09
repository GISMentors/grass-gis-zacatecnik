Vytvoření nové vektorové mapy
-----------------------------
Grafickou editaci vektorových dat spustíme z menu  
:menuselection:`Vector --> Develop vector map --> Create new vector map`.

.. figure:: images/create-vector.png

   Vytvoření nové vektorové vrstvy

V konfiguračním okně ponecháme název vazby mezi geometrickou částí a
identifikátorem záznamu v atributové databázi ``cat``.

.. note:: V příkazovém řádku můžeme nový prázný vektor vytvořit
    :grassCmd:`v.edit` 

    .. code-block:: bash 
    
        v.edit map=novy_vektor tool=create`

Vytvoření a úprava atributové tabulky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nástroj pro editaci atributové tabulky spustíme z kontextového menu vrtstvy
:guilabel:`Show attribute data`

.. figure:: images/edit-attributes-01.png

    Spuštění tabulky atributů

V záložce :guilabel:`Manage attributes` můžeme přidávat a přejmenovávat
atributové sloupečky

.. figure:: images/attribute-table.png

    Přidání sloupečku s názvem ``popis``


Editace vektorové vrstvy
------------------------
Existující vektorovou vrstvu můžeme začít editovat z kontextového menu vrtvy
:guilabel:`Start editing`

.. figure:: images/edit-vector-01.png

    Start editace 

Nyní můžeme v mapovém okně zvolit nástroj kreslení linie (nebo kterýkoliv jiný)
a nakreslit požadovaný tvar.

.. note:: Mapové okno bude zobrazovat podkladové mapy, které v něm byly načteny
    dříve

Po ukončení editace objektu (pravým tlačítkem) se objeví formulář pro vyplnění
atributů

.. figure:: images/edit-vector-02.png

    Editace vektorových objektů

Počáteční a koncové body linií a ploch na se na sebe budou přichytávat (výchozí
hodnota je 10px). Počáteční a koncové body linií a polygonů jsou vykresleny
různě, podle toho jsou-li přichyceny k dalšímu bodu či nikoliv.

Při editaci ploch je každá plocha automaticky *zaplochována* centroidem. K
centroidu se naváží požadované atributy. Hranice plochy a jejich centroidy lze
editovat i zvlášť.

Mazání vybraných prvů je potřeba vždy potvrdit pravým tlačítkem myši.

Přiřazování atributů novým prvkům
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V nastavení editace můžeme nastavit zobrazení editovaných prvků (šířka, barvy),
snapping, automatické přiřazování atributů novým prkvům, a další.

.. figure:: images/editing-settings.png

    Nastavení editace

.. note:: Editovat vektorové objekty lze také v příkazové řádce pomocí modulu
    :grassCmd:`v.edit` 
