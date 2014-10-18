Struktura dat - koncept lokací a mapsetů
----------------------------------------

Pokud není definováno jinak, tak v případě MS Windows je GRASS [[GRASS
GIS / Struktura dat#Databanka | databanka]] umístěna v adresáři
{{path|%USERPROFILE%\Documents\grassdata}}, kde
{{env|USERPROFILE|platform=windows}} odpovídá domovskému adresáři
uživatele. V případě UNIXových operačních systémů jako je
{{wikipedia|Linux|GNU/Linux}} či {{wikipedia|Mac_OS|Mac OS X}} je
GRASS databanka nejčastěji umisťována do adresáře
{{path|$HOME/grassdata}}, kde
{{wikipedia|Environment_variable|proměnná prostředí|lang=en}}
{{env|HOME}} odkazuje na domovský adresář uživatele.

Příklad vytvoření GRASS databanky, stažení datasetu ''North Carolina'' z prostředí příkazové řádky:

{{bashScript|
 # založení adresáře
 mkdir $HOME/grassdata
 cd $HOME/grassdata
 
 # stažení dat
 wget http://grass.osgeo.org/sampledata/nc_spm_latest.tar.gz
 
 # dekomprimace archivu
 tar xvzf nc_spm_latest.tar.gz
}}
