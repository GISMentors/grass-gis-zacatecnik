Rastrová data
-------------

Rastrová data jsou v systému GRASS uložena v podobě tzv. **rastrových
map**. Jde o:

* Reprezentaci v podobě pravidelné mřížky hodnot (GRASS nepodporuje
  nepravidlé mřížky)
* Ideální pro reprezentaci spojitých jevů jako nadmořská výška, teplota povrchu a pod.
* Elementem mřížky je buňka či tzv. *pixel*, jehož tvar může být buď
  čtvercový nebo obdélníkový
* Velikost pixelu je dána *prostorovým rozlišením*
* K hodnotě buňky lze přiřadit textový popisek (tzv. *label*)

.. _raster-metadata:

Metadata
========

Základní metadata o rastrových datech vypisuje modul
:grasscmd:`r.info` dostupný z menu :menuselection:`Raster --> Reports
and statistics --> Basic raster metadata` anebo z kontextového menu
rastrové mapy ve *správci vrstev*.

.. figure:: images/lmgr-r-info.png
	    
.. figure:: images/lmgr-r-info-example.png

	    Příklad výpisu metadat rastrové mapy
	    :map:`dmt`.

.. _raster-types:
                 
Typy rastrových map
===================

GRASS rozlišuje tři typy rastrových map podle datové typu buňky:

* ``CELL`` (celé číslo, :wikipedia-en:`integer <Integer (computer
  science)>`)

.. figure:: images/rast-num.png

* ``FCELL`` (hodnoty s plovoucí desetinnou čárkou,
  :wikipedia-en:`float <Single-precision floating-point format>`)
* ``DCELL`` (hodnoty s plovoucí desetinout čárkou s dvojnásobnou
  přesností, :wikipedia-en:`double precision`)

.. figure:: images/rast-num-float.png

.. note::

   Kromě 2D rastrových dat GRASS podporuje i 3D rastrová data
   (tzv. *volumes*) a nad nimi postavené analýzy. Tato problematika je
   ale nad rámec tohoto školení a je probírána v navazující `školení
   pro pokročilé uživatele <http://www.gismentors.eu/skoleni/grass-gis.html#pokrocily>`_.
