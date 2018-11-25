.. _label: instalace-linux

.. index::
   single: Linux
   see: Linux; Instalace

GNU/Linux
---------

Systém GRASS je dostupný ve většině rozšířených linuxových distribucí
jako tzv. *balíček (package)*.

.. noteadvanced::

   Pokud balíčkovací systém dané linuxové distribuce neobsahuje GRASS
   nebo nabízí jeho zastaralou verzi lze systém GRASS poměrně
   jednoduše zkompilovat [#f1]_ vlastními silami.

.. index::
   single: Debian
   see: Debian; Instalace

Postup instalace pro Debian GNU/Linux
=====================================

Systém GRASS můžete nainstalovat běžným způsobem, viz `přehled verzí
<http://packages.debian.org/search?keywords=grass&searchon=names&suite=all&section=all>`__.

.. note:: Údržbu balíčku systému GRASS a ostatních GIS software
   zajišťuje projekt `DebianGIS <http://wiki.debian.org/DebianGis>`_.

.. notecmd:: Instalace
   
   .. code-block:: bash

      sudo apt-get install grass grass-gui grass-doc

.. index::
   single: Ubuntu
   see: Ubuntu; Instalace
   
Postup instalace pro Ubuntu
===========================

Systém GRASS můžete nainstalovat běžným způsobem, viz `přehled verzí
<http://packages.ubuntu.com/search?keywords=grass&searchon=names&suite=all&section=all>`__.

.. tip:: Pokud chcete používat co možná nejaktuálnější verzi systému
   GRASS, tak použijte balíčky z projektu `UbuntuGIS
   <https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable>`__:

   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      sudo apt-get update
      sudo apt-get install grass

.. figure:: images/grass-ubuntu-launch.png
   :class: large
   :scale-latex: 85
                 
   Příklad spuštění systému GRASS na OS Linux.

.. rubric:: `Poznámky pod čarou`
   :class: secnotoc
           
.. [#f1]
         `http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Instalace_GNU/Linux#Kompilace
         <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Instalace_GNU/Linux#Kompilace>`_

.. raw:: latex

   \newpage

