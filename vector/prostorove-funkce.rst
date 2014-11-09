Prostorové funkce
-----------------


.. youtube:: YWRHFylZCuo

             Příklad základních prostorových funkcí (buffer, clip,
             erase) v kombinaci s atributovými dotazy

Výběr z vektorové mapy
~~~~~~~~~~~~~~~~~~~~~~
Z vektorové mapy můžeme vybrat některé prvky a uložit je do nové mapy. Vybírat
můžeme selektivně podle identifikátorů objektu a nebo podle jejich atributů.
Nástroj pro výběr :grassCmd:`v.extract` můžeme spustit z
:menuselection:`Vector --> Feature selection --> Select by attributes`.

.. note:: Ujistěte se, že máte v pracovní cestě přidány všechny *mapsety*,
    abyste mohli pracovat s daty v nich obsaženými. :grassCmd:`g.mapsets` vám
    umožní mapsety do cesty přidat.

Vyberte z vrstvy :map:`doprava` z mapsetu :map:`osm` a zní všechny dálnice (vektory
splňující podmínku ``highway = 'motorway'``. Uložte výsledek do vrstvy
:map:`dalnice`.

.. figure:: images/v-extract.png

    Tvoření vrstvy ``dalnice`` z OpenStreetMap roads.


Obalová zóna
~~~~~~~~~~~~
Vytvoříme obalovou zónu 500m okolo dálnic. :menuselection:`Vector --> Buffer vector`

.. figure:: images/v-buffer-result.png

    Buffer 500m okolo dálnic, modul :grasscmd:`v.buffer`

Překrytí, průnik, spojení, vyloučení
------------------------------------
Zjistíme, jak moc zasahuje zóna 500m okolo dálnic do velkoplošných a
maloplošných chráněných území. Nejprve spojíme velkoplošná a maloplošná území do
jedné vrstvy.

Spustíme modul :grasscmd:`v.overlay`, který nám umožní práci s vektory
:menuselection:`Vector --> Overlay vector maps --> Overlay vector maps [v.overlay]`

Spojení
~~~~~~~
Vytvoříme mapu :map:`chranena_uzemi` spojením velkoplošných a maloplošných
chráněných území.

.. figure:: images/v-overlay-01.png

    Vytvoření vrstvy maloplošných a velkoplošných chráněných území

Výsledná vrstva má spojenou tabulku atributů z obou vrstev, ve které jsou
atributy první vrstvy označeny prefixem ``a_`` a atributy druhé vrstvy prefixem
``b_``.

.. figure:: images/v-overlay-01-table.png

    Atributy vrstvy :map:`chranene_uzemi`

Průnik
~~~~~~
Zjistíme, jak obalová zóna zasahuje do chráněných území. Opět spustíme modul
:grasscmd:`v.overlay` a použijeme operaci průnik (operátor ``AND``).

.. figure:: images/v-overlay-02.png

    Dálniční obalová zóna, procházející chráněným územím.


.. figure:: images/dalnice500buffer_chranena_uzemi-01.png

    Hluková oblast zasahující maloplošné chráněné území Černovický hájek u Brna

.. figure:: images/dalnice500buffer_chranena_uzemi-02.png

    Hluková oblast zasahující vlkoplošné chráněné území CHKO Česká kras a CHKO
    Křivoklátsko

Podobně fungují i operátory ``XOR`` a ``NOT``.

Spojení vektorových map
-----------------------
Alternativním způsobem spojení vektorových map je modul :grasscmd:`v.patch`. Na
rozdíl od :grasscmd:`v.overlay` tento modul pozná, pokud jsou tabulky atributů
stejné a místo aby rozšiřoval jejich počet, sloučí je automaticky dohromady.

V tomto příkladu si vytvoříme novou mapu :map:`silnice`, která bude obsahovat
mapy :map:`dalnice, I_trida, II_trida, III_trida` sloučené dohromady.

Spustíme modul :grasscmd:`v.patch` například z menu 
:menuselection:`Vector --> Overlay vector maps --> Patch vector maps [v.patch]`

.. figure:: images/v-patch-01.png

    V modulu :grasscmd:`v.patch` jsme nastavili jako vstupní vrstvy dalnice,
    :map:`I_trida, II_trida` a :map:`III_trida` z mapsetu ``osm`` a výstup jsme pojmenovali
    :map:`silnice`
