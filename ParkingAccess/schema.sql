/* (Beta) Export of data model ParkingAccess of the subject dataModel.Parking for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ParkingAccess_type AS ENUM ('ParkingAccess');
CREATE TABLE ParkingAccess (address JSON, alternateName TEXT, areaServed TEXT, category JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, features JSON, height NUMERIC, name TEXT, owner JSON, slope NUMERIC, source TEXT, type ParkingAccess_type, width NUMERIC);