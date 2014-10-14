MS Windows
----------

Systém GRASS je možné pod MS Windows nainstalovat *dvěma způsoby*:

#. pomocí :ref:`nativního instalátoru<nativni-instalator>`
   (doporučujeme *pro začátečníky*, kdy nepředpokládáme častou
   aktualizaci softwaru)
#. v rámci :ref:`OSGeo4W frameworku <osgeo4w-instalator>` (pro
   pokročilejší uživatele, komplexnější řešení umožňující instalaci
   dalšího softwaru distribuovaného pod hlavičkou `OSGeo
   <http://www.osgeo.org/>`_, vhodné při předpokladu časté aktualizace
   softwaru)

.. _nativni-instalator:

Nativní instalátor
==================

**Nativní instalátor** je dostupný na adrese
http://grass.osgeo.org/grass70/binary/mswindows/native/.

.. admonition:: Poznámka pro pokročilé uživatele

                V případě nutnosti aktuálnější verze či testování nových vlastností je
                možné využít denní snapshoty instalátoru na adrese
                http://wingrass.fsv.cvut.cz/grass70.

Image:wingrass-install-0.png
Image:wingrass-install-1.png
Image:wingrass-install-2.png
Image:wingrass-install-3.png
Image:wingrass-install-4.png
Image:wingrass-install-5.png
Image:wingrass-install-6.png

.. _osgeo4w-instalator:

OSGeo4W
=======

Instalátor ke stažení na adrese http://download.osgeo.org/osgeo4w/osgeo4w-setup.exe.

Image:osgeo4w-0.png
Image:osgeo4w-1.png
Image:osgeo4w-2.png
Image:osgeo4w-3.png

V rámci OSGeo4W frameworku je možné nainstalovat i denní snapshoty.

Image:osgeo4w-dev-0.png
Image:osgeo4w-dev-1.png
Image:osgeo4w-dev-2.png
Image:osgeo4w-dev-3.png
Image:osgeo4w-dev-4.png
Image:osgeo4w-dev-5.png
Image:osgeo4w-dev-6.png
Image:osgeo4w-dev-7.png

Automatická aktualizace (pro pokročilé uživatele)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aktualizovat instalaci OSGeo4W (včetně instalace systému GRASS) lze provádět automaticky v rámci plánovače úloh OS MS Windows.

Stačí umístit do zvoleného adresáře níže uvedený skript s příponou
{{wikipedia|Batch file|bat|lang=en}} (předpokládejme, že je framework
OSGeo4W nainstalován v adrešáři <code>C:\OSGeo4W</code>):

.. code-block:: dos

                @echo off

                set PATH=C:\OSGeo4W\bin;%PATH%
                call o4w_env.bat

                apt update
                apt upgrade

a nastavit spuštění skriptu jako úlohu (příklad pro spuštění aktualizace OSGeo4W každý den v 8h ráno).

Image:osgeo4w-cronjob-0.png
Image:osgeo4w-cronjob-1.png
Image:osgeo4w-cronjob-2.png
