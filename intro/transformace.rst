.. _transformace:

Práce s geodaty v různých souřadnicových systémech
--------------------------------------------------

V případě, že chcete do aktuální lokace importovat geodata jejichž
souřadnicový systém se liší od souřadnicového systému aktuální lokace
(viz :item:`Projection match` na obr. níže) je třeba několik kroků:

.. figure:: images/import-no-proj.png

Postup
======
   
#. vytvořit novou lokaci s souřadnicovým systémem vstupních geodat
#. do této nové lokaci se přepnout a geodata tam naimportovat
#. dále se vrátit opět do původní lokace a do této naimportovaná
   geodata transformovat

Vytvoření nové lokace
^^^^^^^^^^^^^^^^^^^^^

Z menu *Strávce vrstev* spusťte z menu :menuselection:`Settings -->
GRASS working environment --> Create new location` průvodce tvorby
lokace, novou lokaci můžete :ref:`vytvořit více způsoby
<tvorba-lokace>`, nejrychlejší je v tomto připadě :ref:`tvorba na
základě vstupních geodat <lokace-srtm>`. Po vytvoření nové lokace se
objeví dialog, který umožňuje se do této lokace přepnout.

.. figure:: images/new-loc-switch.png
            :class: small
           
.. figure:: images/new-loc-switch-confirm.png
            :class: small
           
Import geodat do nové lokace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Geodata do nově vytvořené lokace :ref:`naimportuje standardní cestou
<import-vector>`, položka :item:`Projection match` by měla obsahovat
již hodnotu ``Yes``.

.. figure:: images/import-osm.png

Po importu dat se vrátíme do původní lokace :menuselection:`Settings
--> GRASS working environment --> Change location and mapset`.

.. figure:: images/change-loc-map.png
            :class: small

Aktuální nastavení lokace můžeme volitelně uložit do souboru s
projektem (tzv. *workspace file*).

.. figure:: images/loc-switch-save.png
            :class: small

Poté se objeví dialog, který potvrzuje, že aktuální lokace je opět ta
cílová.

.. figure:: images/loc-switch-back.png
            :class: small
                    
Transformace dat do cílové lokace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transformovat **rastrová data** umožňuje modul :grasscmd:`r.proj`
dostupný z menu *správce vrstev* :menuselection:`Raster --> Develop
raster map --> Reproject raster map from different GRASS location`,
podopně pro **vektorová data** existuje :grasscmd:`v.proj` dosupný z
:menuselection:`Vector --> Develop vector map --> Reproject vector map
from different GRASS location`.

Následuje příklad pro transformaci vektorových dat.

.. figure:: images/v-proj-0.png
   
            V dialogu modulu :grasscmd:`v.proj` nejprve vybereme
            lokaci se vstupními daty :fignote:`(1)`.

.. figure:: images/v-proj-1.png

            Dále v záložce :item:`Source` vybereme mapset, ve kterém
            jsou vstupní data uložena :fignote:`(2)`, vybereme vstupní
            vektorovou mapu :fignote:`(3)`. Pokud by lokace byly
            umístěny v odlišných adresářích, je potřeba definovat
            adresář se vstupní lokace :fignote:`(4)`.

.. figure:: images/v-proj-2.png

            Případně můžeme v záložce :item:`Target` zvolit název pro
            výstupní mapu :fignote:`(5)`. Transformaci spustíme
            :fignote:`(6)`.

Po úspěšné transformaci se vytvořená vrstva automaticky přídá do
*správce vrstev* a zobrazí v mapovém okně.

.. figure:: images/proj-result.png
            :class: large
            

               
