# dataModel.Parking
These data models are intended to model entities relevant for parking use cases in smart cities scenarios. When feasible these models reuse types, properties and enumerations from [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). A data dictionary for DATEX II terms can be found at [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).
Nonetheless, these data models are intended to NGSI-based systems and many simplifications has been made with respect to DATEX II version 2.3.

The following entity types are available:
- [OffStreetParking](https://github.com/smart-data-models/dataModel.Parking/blob/master/OffStreetParking/README.md). A site, off street, intended to park vehicles, managed independently and with suitable and clearly marked access points (entrances and exits). 
If necessary, and for management purposes or to deal with multi-location parking sites, 
it can be divided into different zones modelled by the entity type ParkingGroup .
In DATEX 2 version 2.3 terminology it corresponds to a UrbanParkingSite of type offStreetParking.


- [OnStreetParking](https://github.com/smart-data-models/dataModel.Parking/blob/master/OnStreetParking/README.md). A site, open space zone, on street, (metered or not) with direct access from a road, 
intended to park vehicles. In DATEX 2 version 2.3 terminology 
it corresponds to a UrbanParkingSite of type onStreetParking.


- [ParkingAccess](https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingAccess/README.md). Represents an access point to a parking site, normally an offstreet parking.


- [ParkingGroup](https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingGroup/README.md). A group of parking spots. Granularity level can vary. It can be an storey on a parking garage, 
an specific zone belonging to a big parking lot, or just a group of spots intended for parking a certain vehicle type or 
subject to certain restrictions (disabled, residents, ...).
For the sake of simplicity only one vehicle type per parking group is allowed. Similarly,
one required permit is only allowed per group type.


- [ParkingSpot](https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingSpot/README.md). A parking spot is an area well delimited where one vehicle can be parked.
The aim of this entity type is to monitor the status of parking spots
individually. Thus, an entity of type ParkingSpot cannot exist without a
containing entity of type (OnStreetParking, OffStreetParking). A parking
spot might belong to one group.



[Link](https://github.com/smart-data-models/dataModel.Parking/blob/master/CONTRIBUTORS.yaml) to the 5 current contributors of the data models of this Subject.

You can raise an [issue](https://github.com/smart-data-models/dataModel.Parking/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Parking/pulls) on existing data models


