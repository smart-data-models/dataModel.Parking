<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: ParkingGroup    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Parking Group **    
version: 0.1.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Number identifying a specific property on a public street      
- `allowedVehicleType[string]`: Vehicle type allowed (a parking group only allows one vehicle type). Enum:'bicycle, bus, car, caravan, motorcycle, motorscooter, truck'   . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: An alternative name for this item  - `areBordersMarked[boolean]`: Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: The number of spots available in this group. It must lower or equal than `totalSpotNumber`  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: Parking Group's category. Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  . Model: [http://schema.org/Text](http://schema.org/Text)- `chargeType[array]`: Type of charge(s) performed by the parking site. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maximumAllowedHeight[number]`: Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[date-time]`: Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  - `name[string]`: The name of this item  - `occupancyDetectionType[array]`: Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Or any other application-specific  . Model: [http://schema.org/Text](http://schema.org/Text)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `parkingMode[array]`: Parking mode(s). Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined. Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:'echelonParking, parallelParking, perpendicularParking'  . Model: [http://schema.org/Text](http://schema.org/Text)- `permitActiveHours[object]`: This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. Empty object means always active. The syntax must be conformant with schema.org [opening hours specification](https://schema.org/openingHours). For instance, a blue zone which is only active on dayweeks will be encoded as 'blueZonePermit': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `refParkingSite[*]`: Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking  - `refParkingSpot[*]`: Individual parking spots belonging to this parking group  - `requiredPermit[array]`: This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ','. For instance 'residentPermit,disabledPermit' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed  . Model: [http://schema.org/Text](http://schema.org/Text)- `reservationType[string]`: Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined. Enum:'mandatory, notAvailable, optional, partly'  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `totalSpotNumber[number]`: The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI Entity type. It has to be ParkingGroup  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `refParkingSite`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
A group of parking spots. Granularity level can vary. It can be an storey on a parking garage, an specific zone belonging to a big parking lot, or just a group of spots intended for parking a certain vehicle type or subject to certain restrictions (disabled, residents, ...). For the sake of simplicity only one vehicle type per parking group is allowed. Similarly, one required permit is only allowed per group type.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ParkingGroup:      
  description: 'Parking Group '      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    allowedVehicleType:      
      description: 'Vehicle type allowed (a parking group only allows one vehicle type). Enum:''bicycle, bus, car, caravan, motorcycle, motorscooter, truck'' '      
      enum:      
        - bicycle      
        - bus      
        - car      
        - caravan      
        - motorcycle      
        - motorscooter      
        - truck      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areBordersMarked:      
      description: Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    availableSpotNumber:      
      description: The number of spots available in this group. It must lower or equal than `totalSpotNumber`      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    averageSpotLength:      
      description: The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/length      
        type: Property      
        units: meters      
    averageSpotWidth:      
      description: The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/width      
        type: Property      
        units: meters      
    category:      
      description: 'Parking Group''s category. Enum:''adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'''      
      items:      
        enum:      
          - adjacentSpaces      
          - blueZone      
          - completeFloor      
          - free      
          - feeCharged      
          - greenZone      
          - loadUnloadZone      
          - nonAdjacentSpaces      
          - offStreet      
          - onlyDisabled      
          - onlyElectricalCharging      
          - onlyResidents      
          - onlyWithPermit      
          - onStreet      
          - particularConditionsSpaces      
          - shortTermMediumTermLongTerm      
          - statisticsOnly      
          - vehicleTypeSpaces      
        type: string      
      type: array      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    chargeType:      
      description: 'Type of charge(s) performed by the parking site. Enum:''additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'''      
      items:      
        enum:      
          - additionalIntervalPrice      
          - annualPayment      
          - firstIntervalPrice      
          - flat      
          - free      
          - minimum      
          - maximum      
          - monthlyPayment      
          - seasonTicket      
          - temporaryFee      
          - temporaryPrice      
          - unknown      
          - other      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    maximumAllowedHeight:      
      description: Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/heigth      
        type: Property      
        units: meters      
    maximumAllowedWidth:      
      description: Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/width      
        type: Property      
        units: Meters      
    maximumParkingDuration:      
      description: Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    occupancyDetectionType:      
      description: 'Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. Or any other application-specific'      
      items:      
        enum:      
          - balancing      
          - manual      
          - modelBased      
          - none      
          - singleSpaceDetection      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    parkingMode:      
      description: 'Parking mode(s). Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:''echelonParking, parallelParking, perpendicularParking'''      
      items:      
        enum:      
          - echelonParking      
          - parallelParking      
          - perpendicularParking      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    permitActiveHours:      
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. Empty object means always active. The syntax must be conformant with schema.org [opening hours specification](https://schema.org/openingHours). For instance, a blue zone which is only active on dayweeks will be encoded as ''blueZonePermit'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00''. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'      
      type: object      
      x-ngsi:      
        model: https://schema.org/openingHours      
        type: Property      
    refParkingSite:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking      
      x-ngsi:      
        type: Relationship      
    refParkingSpot:      
      anyOf:      
        - maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
        - format: uri      
          type: string      
      description: Individual parking spots belonging to this parking group      
      x-ngsi:      
        type: Relationship      
    requiredPermit:      
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed'      
      items:      
        enum:      
          - employeePermit      
          - studentPermit      
          - fairPermit      
          - governmentPermit      
          - residentPermit      
          - specificIdentifiedVehiclePermit      
          - disabledPermit      
          - visitorPermit      
          - blueZonePermit      
          - careTakingPermit      
          - carpoolingPermit      
          - carSharingPermit      
          - emergencyVehiclePermit      
          - maintenanceVehiclePermit      
          - roadWorksPermit      
          - taxiPermit      
          - transportationPermit      
          - noPermitNeeded      
        type: string      
      type: array      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    reservationType:      
      description: 'Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Enum:''mandatory, notAvailable, optional, partly'''      
      enum:      
        - mandatory      
        - notAvailable      
        - optional      
        - partly      
      type: string      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    totalSpotNumber:      
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class'      
      minimum: 1      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be ParkingGroup      
      enum:      
        - ParkingGroup      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - refParkingSite      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingGroup/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/ParkingGroup/schema.json      
  x-model-tags: ""      
  x-version: 0.1.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### ParkingGroup NGSI-v2 key-values Example      
Here is an example of a ParkingGroup in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": [  
    "onStreet",  
    "adjacentSpaces",  
    "onlyDisabled"  
  ],  
  "allowedVehicleType": "car",  
  "chargeType": [  
    "free"  
  ],  
  "refParkingSite": "daoiz-velarde-1-5",  
  "description": "Two parking spots reserved for disabled people",  
  "totalSpotNumber": 2,  
  "availableSpotNumber": 1,  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -3.80356167695194,  
          43.46296641666926  
        ],  
        [  
          -3.803161973253841,  
          43.46301091092682  
        ],  
        [  
          -3.803147082548618,  
          43.462879859445884  
        ],  
        [  
          -3.803536474744068,  
          43.462838666196674  
        ],  
        [  
          -3.80356167695194,  
          43.46296641666926  
        ]  
      ]  
    ]  
  },  
  "requiredPermit": [  
    "disabledPermit"  
  ],  
  "permitActiveHours": {  
    "Monday": "null"  
  }  
}  
```  
</details>    
#### ParkingGroup NGSI-v2 normalized Example      
Here is an example of a ParkingGroup in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "onStreet",  
      "adjacentSpaces",  
      "onlyDisabled"  
    ]  
  },  
  "refParkingSite": {  
    "type": "Text",  
    "value": "daoiz-velarde-1-5"  
  },  
  "permitActiveHours": {  
    "type": "StructuredValue",  
    "value": {  
      "Monday": "null"  
    }  
  },  
  "requiredPermit": {  
    "type": "StructuredValue",  
    "value": [  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "Text",  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "type": "Boolean",  
    "value": true,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-12T12:00:00"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.80356167695194,  
            43.46296641666926  
          ],  
          [  
            -3.803161973253841,  
            43.46301091092682  
          ],  
          [  
            -3.803147082548618,  
            43.462879859445884  
          ],  
          [  
            -3.803536474744068,  
            43.462838666196674  
          ],  
          [  
            -3.80356167695194,  
            43.46296641666926  
          ]  
        ]  
      ]  
    }  
  },  
  "chargeType": {  
    "type": "StructuredValue",  
    "value": [  
      "free"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Two parking spots reserved for disabled people"  
  }  
}  
```  
</details>    
#### ParkingGroup NGSI-LD key-values Example      
Here is an example of a ParkingGroup in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "allowedVehicleType": "car",  
  "availableSpotNumber": 1,  
  "category": [  
    "onStreet",  
    "adjacentSpaces",  
    "onlyDisabled"  
  ],  
  "chargeType": [  
    "free"  
  ],  
  "description": "Two parking spots reserved for disabled people",  
  "location": {  
    "coordinates": [  
      [  
        [  
          -3.80356167695194,  
          43.46296641666926  
        ],  
        [  
          -3.803161973253841,  
          43.46301091092682  
        ],  
        [  
          -3.803147082548618,  
          43.462879859445884  
        ],  
        [  
          -3.803536474744068,  
          43.462838666196674  
        ],  
        [  
          -3.80356167695194,  
          43.46296641666926  
        ]  
      ]  
    ],  
    "type": "Polygon"  
  },  
  "permitActiveHours": {  
    "Monday": "null"  
  },  
  "refParkingSite": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5",  
  "requiredPermit": [  
    "disabledPermit"  
  ],  
  "totalSpotNumber": 2,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ParkingGroup NGSI-LD normalized Example      
Here is an example of a ParkingGroup in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 1,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "onstreet",  
      "adjacentSpaces",  
      "onlyDisabled"  
    ]  
  },  
  "chargeType": {  
    "type": "Property",  
    "value": [  
      "free"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Two parking spots reserved for disabled people"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            -3.80356167695194,  
            43.46296641666926  
          ],  
          [  
            -3.803161973253841,  
            43.46301091092682  
          ],  
          [  
            -3.803147082548618,  
            43.462879859445884  
          ],  
          [  
            -3.803536474744068,  
            43.462838666196674  
          ],  
          [  
            -3.80356167695194,  
            43.46296641666926  
          ]  
        ]  
      ]  
    }  
  },  
  "permitActiveHours": {  
    "type": "Property",  
    "value": "null"  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5"  
  },  
  "requiredPermit": {  
    "type": "Property",  
    "value": "disabledPermit"  
  },  
  "totalSpotNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
