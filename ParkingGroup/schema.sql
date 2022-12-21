/* (Beta) Export of data model ParkingGroup of the subject dataModel.Parking for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE allowedVehicleType_type AS ENUM ('bicycle', 'bus', 'car', 'caravan', 'motorcycle', 'motorscooter', 'truck');CREATE TYPE reservationType_type AS ENUM ('mandatory', 'notAvailable', 'optional', 'partly');CREATE TYPE ParkingGroup_type AS ENUM ('ParkingGroup');
CREATE TABLE ParkingGroup (address json, allowedVehicleType allowedVehicleType_type, alternateName text, areBordersMarked text, areaServed text, availableSpotNumber integer, averageSpotLength text, averageSpotWidth text, category json, chargeType json, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, maximumAllowedHeight text, maximumAllowedWidth text, maximumParkingDuration timestamp, name text, occupancyDetectionType json, owner json, parkingMode json, permitActiveHours json, refParkingSite text, refParkingSpot text, requiredPermit json, reservationType reservationType_type, seeAlso json, source text, totalSpotNumber integer, type ParkingGroup_type);