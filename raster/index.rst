Rastrová data
-------------

* Reprezentace v podobě pravidelné mřížky hodnot (GRASS nepodporuje
  nepravidlé mřížky)
* Elementem mřížky je buňka či tzv. *pixel* jehož tvar může být buď
  čtvercový nebo obdélníkový
* Velikost pixele je dán *prostorovým rozlišením*
* K hodnotě buňky lze přiřadit textový popisek (tzv. *label*)
* Ideální pro reprezentaci spojitých jevů jako nadmořská výška, teplota povrchu a pod.

Rastrová data jsou v systému uložena v podobě tzv. *rastrových map*.

.. rubric:: Typy rastrových map v systému GRASS
	    :class: secnotoc

GRASS rozlišuje tři typy rastrových map podle datové typu buňky, který
může být:

* ``CELL`` (celé číslo, `integer`)
* ``FCELL`` (hodnoty s plovoucí desetinnou čárkou, `float`)
* ``DCELL`` (hodnoty s plovoucí desetinout čárkou s dvojnásobnou
  přesností, `doble precision`)

.. note::

   Kromě 2D rastrových dat GRASS podporuje i 3D rastrová data
   (tzv. *volumes) a nad nimi postavené analýzy. Tato problematika je
   ale nad rámec tohoto školení a je probírána v navazující `školení
   pro pokročilé uživatele <http://www.gismentors.eu/skoleni/grass-gis.html#pokrocily>`_.
