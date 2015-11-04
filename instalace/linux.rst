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

Přehled balíčků GRASS dostupných pro :wikipedia:`Debian GNU/Linux` (viz
projekt `DebianGIS <http://wiki.debian.org/DebianGis>`_):

* http://packages.debian.org/search?keywords=grass&searchon=names&suite=all&section=all

.. notecmd:: Instalace
   
   .. code-block:: bash

      sudo apt-get install grass grass-gui grass-doc

.. index::
   single: Ubuntu
   see: Ubuntu; Instalace
   
Postup instalace pro Ubuntu
===========================

Přehled balíčků GRASS dostupných pro :wikipedia:`Ubuntu` (viz
`Launchpad <https://launchpad.net/~grass>`_):

.. * http://packages.ubuntu.com/search?keywords=grass&searchon=names&suite=all&section=all

.. notecmd:: Instalace
               
   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      sudo apt-get update
      sudo apt-get install grass

.. figure:: images/grass-ubuntu-launch.png
            :class: middle
            :scale-latex: 70
                 
            Spuštění systému GRASS v Ubuntu

.. rubric:: `Poznámky pod čarou`
   :class: secnotoc
           
.. [#f1]
         `http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Instalace_GNU/Linux#Kompilace
         <http://freegis.fsv.cvut.cz/gwiki/GRASS_GIS_/_Instalace_GNU/Linux#Kompilace>`_

.. raw:: latex

   \newpage

