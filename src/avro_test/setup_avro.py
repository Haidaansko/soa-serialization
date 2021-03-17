import io

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

d = {
    'PackageID' : 1539,
    'PersonID' : 33,
    'Name' : """MEGA_GAMER_2222""",
    'Inventory': dict((str(i),i) for i in iter(range(1, 100))),  

    'CurrentLocation': """
		Pentos is a large port city, more populous than Astapor on Slaver Bay, 
		and may be one of the most populous of the Free Cities. 
		It lies on the bay of Pentos off the narrow sea, with the Flatlands 
		plains and Velvet Hills to the east.
		The city has many square brick towers, controlled by the spice traders. 
		Most of the roofing is done in tiles. There is a large red temple in 
		Pentos, along with the manse of Illyrio Mopatis and the Sunrise Gate 
		allows the traveler to exit the city to the east, 
		in the direction of the Rhoyne.
		"""
}

PATH_AVSC = "avro_test/myobject.avsc"
PATH_AVRO = "avro_test/myobject.avro"

schema = avro.schema.parse(open(PATH_AVSC, "r").read())

with DataFileWriter(open(PATH_AVRO, 'wb'), DatumWriter(), schema) as writer: writer.append(d)
with open(PATH_AVRO, 'rb') as f: src = f.read()