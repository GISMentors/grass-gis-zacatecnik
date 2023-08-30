.. index::
   single: MS Windows
   see: MS Windows; Instalace

MS Windows
----------

.. important:: Pokud máte nainstalován na svém počítači `QGIS
   <https://www.qgis.org>`__, tak máte systém GRASS již k dispozici a
   nemusíte ho instalovat.
               
Systém GRASS je možné pod MS Windows nainstalovat *dvěma způsoby*:

#. pomocí tradičního :ref:`nativního instalátoru<nativni-instalator>`

   * vhodné *pro naprosté začátečníky*
   * nepředpokládáme častou aktualizaci softwaru

#. pomocí síťového instalátoru :ref:`OSGeo4W <osgeo4w-instalator>` (*doporučeno*)

   * komplexní řešení umožňující instalaci i dalšího softwaru
     distribuovaného pod hlavičkou `OSGeo <http://www.osgeo.org/>`_
     (jako je např. `QGIS <http://qgis.org>`_, `MapServer
     <http://mapserver.org>`_ a další)
   * vhodné při předpokladu časté aktualizace softwaru

.. note:: Na většině dnešních počítačů zvolte instalaci 64bitové verze softwaru.
          
.. _nativni-instalator:

Nativní instalátor
==================

Nativní instalátor je dostupný na adrese: https://grass.osgeo.org/download/software/ms-windows/#stand-alone. Následující obrazová dokumentace dokresluje proces instatalace.

..
   .. noteadvanced:: 

      V případě nutnosti aktuálnější verze či testování
      nových vlastností je možné využít denní snapshoty
      instalátoru dostupných na adrese
      http://wingrass.fsv.cvut.cz/grass70.

.. figure:: images/wingrass-0.png
            :scale-latex: 60

            Spustíme instalátor.
   
.. figure:: images/wingrass-1.png
            :scale-latex: 49

            Potvrdíme licenci.
   
.. figure:: images/wingrass-2.png
            :scale-latex: 49
   
            Potvrdíme adresář, kam se má GRASS nainstalovat.

.. _nativni-instalator-data:

.. figure:: images/wingrass-3.png
            :scale-latex: 49
           
	    Důrazně doporučujeme (vyhnete se problémům při spuštení
	    systému GRASS v případě chybějících knihoven MS Windows)
	    nainstalovat také "Important Microsoft Runtime Libraries"
	    a pokud nemáte vlastní data tak i ukázkovou geografickou
	    datovou sadu pro GRASS "North Carolina".

.. figure:: images/wingrass-4.png
            :class: small
            :scale-latex: 50
            
            GRASS můžeme spustit z nabídky Start.
            
.. figure:: images/wingrass-5.png
            :scale-latex: 60
            
            Po startu se objeví úvodní obrazovka systému GRASS pro
	    výběr tzv. lokace a mapsetu, viz kapitola
	    :doc:`../intro/struktura-dat`.

.. raw:: latex

   \clearpage

.. index::
   single: OSGeo4W
   see: OSGeo4W; Instalace

.. _osgeo4w-instalator:

OSGeo4W
=======

Síťový instalátor je ke stažení pro `32 bitovou
<http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86.exe>`_ a `64
bitovou <http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86_64.exe>`_
platformu.

.. figure:: images/osgeo4w-0.png
            :scale-latex: 45
                 
	    GRASS nainstalujeme ze sekce ``Express Desktop Install``.

.. figure:: images/osgeo4w-1.png
            :scale-latex: 45

            V následující části necháme povolené balíčky GDAL a GRASS GIS.
   
.. noteadvanced::

   V rámci OSGeo4W je možné nainstalovat i *denní snapshoty* vývojové
   verze systému GRASS. To se hodí v případě, že potřebujete otestovat
   např. novou funkcionalitu, která není součástí stabilní verze.

   .. figure:: images/osgeo4w-2.png
      :scale-latex: 50
               
      Zvolíme ``Advanced Install``.
      
   .. figure:: images/osgeo4w-3.png
      :scale-latex: 50
               
      Ze sekce ``Desktop`` vybereme balíček ``grass-daily``
      (denní snapshoty aktuální vývojové verze systému GRASS).

.. raw:: latex

   \newpage
         
Poznámky
^^^^^^^^

Nastavení velikosti písma terminálu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V novějších verzích Windows bývá výchozí velikost písma terminálu
příliš malá.

.. figure:: images/winterminal-small.png
   :class: small

Velikost písma můžete změnit ve vlastnostech okna (pravé tlačítko myši
nad titulkem okna, :menuselection:`Vlastnosti`).

.. figure:: images/winterminal-font.png
   :class: small

..
   Automatická aktualizace (pro velmi pokročilé uživatele)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Aktualizovat instalaci OSGeo4W (včetně instalace systému GRASS) lze
   provádět automaticky v rámci plánovače úloh MS Windows.
   
   Stačí umístit do zvoleného adresáře níže uvedený skript s příponou
   :wikipedia-en:`bat <Batch file>` (předpokládejme, že je framework
   OSGeo4W nainstalován v adresáři ``C:\OSGeo4W``):

   .. code-block:: bat

                @echo off

                set PATH=C:\OSGeo4W\bin;%PATH%
                call o4w_env.bat

                apt update
                apt upgrade

   a nastavit spuštění skriptu jako úlohu.

   .. figure:: images/osgeo4w-cronjob-0.png
      :scale-latex: 50

   .. figure:: images/osgeo4w-cronjob-1.png
      :scale-latex: 50
            
      Příklad pro spuštění aktualizace OSGeo4W každý den v 8h ráno.

   .. figure:: images/osgeo4w-cronjob-2.png
               :scale-latex: 50
