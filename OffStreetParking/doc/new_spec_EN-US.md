Entity: OffStreetParking  
========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Off street parking**  

## List of properties  

- `acceptedPaymentMethod`: Accepted payment method(s).  - `accessModified`: Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601  - `address`: The mailing address.  - `aggregateRating`: Aggregated rating for this parking site.  - `allowedVehicleType`:  Vehicle type(s) allowed. The first element of this  
 array _MUST_ be the principal vehicle type allowed. Free spot numbers of  
 other allowed vehicle types might be reported under the attribute  
 `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_,  
 [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)Allowed values (`agriculturalVehicle`, `bicycle`, `bus`, `car`, `caravan`,`carWithCaravan`, `carWithTrailer`,`constructionOrMaintenanceVehicle`, `lorry`, `moped`, `motorcycle`, `motorcycleWithSideCar`, `motorscooter`, `tanker`, `trailer`, `van`,`anyVehicle`)  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `availableSpotNumber`: The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.  - `averageSpotLength`: The average length of parking spots.  - `averageSpotWidth`: The average width of parking spots.  - `category`: Parking site's category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities. Particularities and detailed descriptions should be found under the corresponding specific attributes. Allowed values: -   (`public`, `private`, `publicPrivate`, `urbanDeterrentParking`, `parkingGarage`, `parkingLot`, `shortTerm`, `mediumTerm`,     `longTerm`, `free`, `feeCharged`, `staffed`, `guarded`, `barrierAccess`, `gateAccess`, `freeAccess`, `forElectricalCharging`, `onlyResidents`, `onlyWithPermit`, `forEmployees`, `forVisitors`, `forCustomers`, `forStudents`,     `forMembers`, `forDisabled`, `forResidents`, `underground`, `ground`) -   The semantics of the `forxxx` values is that the parking offers specific spots subject to that particular condition. -   The semantics of the `onlyxxx`values is that the parking only allows     to park on that particular condition. -   Other application-specific  - `chargeType`: Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration:  
 (`flat`, `minimum`, `maximum`, `additionalIntervalPrice`, `seasonTicket` `temporaryPrice` `firstIntervalPrice`, `annualPayment`, `monthlyPayment`, `free`, `other`) or Any other application-specific  - `contactPoint`: Parking site contact point.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `extCategory`:   - `extraSpotNumber`: The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.  - `facilities`: Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3: -   (`toilet`, `shower`, `informationPoint`, `internetWireless`,     `payDesk`, `paymentMachine`, `cashMachine`, `vendingMachine`,     `faxMachineOrService`, `copyMachineOrService`, `safeDeposit`,     `luggageLocker`, `publicPhone`, `elevator`, `dumpingStation`     `freshWater`, `wasteDisposal`, `refuseBin`, `iceFreeScaffold`,     `playground`, `electricChargingStation`, `bikeParking`,     `tollTerminal`, `defibrillator`, `firstAidEquipment` `fireHose`     `fireExtinguisher` `fireHydrant`) -   Any other application-specific  - `firstAvailableFloor`: Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.  - `highestFloor`: For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.  - `id`:   - `image`: A URL containing a photo of this parking site  - `layout`: Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3: (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`, `openSpace`, `covered`, `nested`, `field`, `rooftop`, `sheds`, `carports`, `garageBoxes`, `other`). See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.  - `location`:   - `lowestFloor`: For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.  - `maximumAllowedHeight`: Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.  - `maximumAllowedWidth`: Maximum allowed width for vehicles. If there are  
    multiple zones, it will be the minimum width of all the zones.  - `maximumParkingDuration`: Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration  - `measuresPeriod`: The measures period related to availableSpotNumber and priceRatePerMinute.  - `measuresPeriodUnit`: The measures period unit related to availableSpotNumber and PriceRatePerMinute.  - `name`: The name of this item.  - `occupancy`:   - `occupancyDetectionType`: Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_:`none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`, Or any other application-specific  - `occupancyModified`: Relative value of occupied spots out of the total spots. Allowed values: 0 - 1  - `occupiedSpotNumber`: Number of spots occupied. Allowed values: 0 - `totalSpotNumber`  - `openingHours`: Opening hours of the parking site.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `parkingMode`: Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration: `perpendicularParking`, `parallelParking`, `echelonParking`  - `priceCurrency`: Price currency of price rate per minute  - `priceRatePerMinute`: Price rate per minute.  - `provider`:   - `refParkingAccess`: Parking site's access point(s).  - `refParkingGroup`: Relationship. Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.  - `refParkingSpot`: Relationship. Individual parking spots belonging to this offstreet parking site.  - `requiredPermit`: This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ",". For instance "residentPermit,disabledPermit" stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3.(`employeePermit`, `studentPermit`, `fairPermit`, `governmentPermit`, `residentPermit`, `specificIdentifiedVehiclePermit`, `visitorPermit`, `noPermitNeeded`)orb any other application-specific  - `reservationType`: he following specified by _ReservationTypeEnum_ of DATEX II version 2.3: (`optional`, `mandatory`, `notAvailable`, `partly`).  - `security`: Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3:  (`patrolled`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences`      `areaSeperatedFromSurroundings`) or any other application-specific  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `specialLocation`: If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of   [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a): (`airportTerminal`, `exhibitonCentre`, `shoppingCentre`, `specificFacility`, `trainStation`, `campground`, `themePark`, `ferryTerminal`, `vehicleOnRailTerminal`, `coachStation`,   `cableCarStation`, `publicTransportStation`, `market`, `religiousCentre`, `conventionCentre`, `cinema`, `skilift`, `hotel`, `other`)  - `status`: Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3 :  
 -   _ParkingSiteStatusEnum_  
 -   _OpeningStatusEnum_  
 -   (`open`, `closed`, `closedAbnormal`,`openingTimesInForce`, `full`,  
 `fullAtEntrance`, `spacesAvailable`, `almostFull`)  
 -   Or any other application-specific  - `totalSpotNumber`: The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.  - `type`: It has to be OffStreetParking  - `usageScenario`: Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3:(`truckParking`, `parkAndRide`, `parkAndCycle`, `parkAndWalk`, `kissAndRide`, `liftshare`, `carSharing`, `restArea`, `serviceArea`, `dropOffWithValet`, `dropOffMechanical`, `eventParking`, `automaticParkingGuidance`, `staffGuidesToSpace`, `vehicleLift`, `loadingBay`, `dropOff`, `overnightParking`, `other` Or any other value useful for the application and not covered above.  - `vehicleEntranceCount`: Aggregated number of vehicle that enter the parking site in a period of time.  - `vehicleExitCount`: Aggregated number of vehicle that leave the parking site in a period of time.    
A site, off street, intended to park vehicles, managed independently and with suitable and clearly marked access points (entrances and exits). If necessary, and for management purposes or to deal with multi-location parking sites, it can be divided into different zones modelled by the entity type [ParkingGroup](../ParkingGroup/README.md) . In DATEX 2 version 2.3 terminology it corresponds to a _UrbanParkingSite_ of type _offStreetParking_. A data dictionary for DATEX II terms can be found at [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Data Model description of properties  
Sorted alphabetically  
```yaml  
OffStreetParking:    
  description: 'Off street parking'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Accepted payment method(s).'    
      items:    
        enum:    
          - ByBankTransferInAdvance    
          - ByInvoice    
          - Cash    
          - CheckInAdvance    
          - COD    
          - DirectDebit    
          - GoogleCheckout    
          - PayPal    
          - PaySwarm    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/acceptedPaymentMethod    
    accessModified:    
      description: 'Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    aggregateRating:    
      description: 'Aggregated rating for this parking site.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
    allowedVehicleType:    
      description: |2-    
         Vehicle type(s) allowed. The first element of this    
         array _MUST_ be the principal vehicle type allowed. Free spot numbers of    
         other allowed vehicle types might be reported under the attribute    
         `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_,    
         [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)Allowed values (`agriculturalVehicle`, `bicycle`, `bus`, `car`, `caravan`,`carWithCaravan`, `carWithTrailer`,`constructionOrMaintenanceVehicle`, `lorry`, `moped`, `motorcycle`, `motorcycleWithSideCar`, `motorscooter`, `tanker`, `trailer`, `van`,`anyVehicle`)    
      items:    
        enum:    
          - agriculturalVehicle    
          - anyVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    availableSpotNumber:    
      description: 'The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    averageSpotLength:    
      description: 'The average length of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    category:    
      description: 'Parking site''s category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities. Particularities and detailed descriptions should be found under the corresponding specific attributes. Allowed values: -   (`public`, `private`, `publicPrivate`, `urbanDeterrentParking`, `parkingGarage`, `parkingLot`, `shortTerm`, `mediumTerm`,     `longTerm`, `free`, `feeCharged`, `staffed`, `guarded`, `barrierAccess`, `gateAccess`, `freeAccess`, `forElectricalCharging`, `onlyResidents`, `onlyWithPermit`, `forEmployees`, `forVisitors`, `forCustomers`, `forStudents`,     `forMembers`, `forDisabled`, `forResidents`, `underground`, `ground`) -   The semantics of the `forxxx` values is that the parking offers specific spots subject to that particular condition. -   The semantics of the `onlyxxx`values is that the parking only allows     to park on that particular condition. -   Other application-specific'    
      items:    
        enum:    
          - barrierAccess    
          - feeCharged    
          - forCustomers    
          - forDisabled    
          - forElectricalCharging    
          - forEmployees    
          - forMembers    
          - forResidents    
          - forStudents    
          - forVisitors    
          - free    
          - freeAccess    
          - gateAccess    
          - guarded    
          - ground    
          - longTerm    
          - mediumTerm    
          - onlyResidents    
          - onlyWithPermit    
          - parkingGarage    
          - parkingLot    
          - private    
          - public    
          - publicPrivate    
          - shortTerm    
          - staffed    
          - underground    
          - urbanDeterrentParking    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    chargeType:    
      description: |-    
        Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration:    
         (`flat`, `minimum`, `maximum`, `additionalIntervalPrice`, `seasonTicket` `temporaryPrice` `firstIntervalPrice`, `annualPayment`, `monthlyPayment`, `free`, `other`) or Any other application-specific    
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
          - other    
          - seasonTicket    
          - temporaryPrice    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    contactPoint:    
      description: 'Parking site contact point.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/contactPoint    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    extCategory:    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    facilities:    
      description: 'Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3: -   (`toilet`, `shower`, `informationPoint`, `internetWireless`,     `payDesk`, `paymentMachine`, `cashMachine`, `vendingMachine`,     `faxMachineOrService`, `copyMachineOrService`, `safeDeposit`,     `luggageLocker`, `publicPhone`, `elevator`, `dumpingStation`     `freshWater`, `wasteDisposal`, `refuseBin`, `iceFreeScaffold`,     `playground`, `electricChargingStation`, `bikeParking`,     `tollTerminal`, `defibrillator`, `firstAidEquipment` `fireHose`     `fireExtinguisher` `fireHydrant`) -   Any other application-specific'    
      items:    
        enum:    
          - toilet    
          - shower    
          - informationPoint    
          - internetWireless    
          - payDesk    
          - paymentMachine    
          - cashMachine    
          - vendingMachine    
          - faxMachineOrService    
          - copyMachineOrService    
          - safeDeposit    
          - luggageLocker    
          - publicPhone    
          - elevator    
          - dumpingStation    
          - freshWater    
          - wasteDisposal    
          - refuseBin    
          - iceFreeScaffold    
          - playground    
          - electricChargingStation    
          - bikeParking    
          - tollTerminal    
          - defibrillator    
          - firstAidEquipment    
          - fireHose    
          - fireExtinguisher    
          - fireHydrant    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: ""    
    firstAvailableFloor:    
      description: 'Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    highestFloor:    
      description: 'For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    id:    
      anyOf: &offstreetparking_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/image    
    layout:    
      description: 'Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3: (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`, `openSpace`, `covered`, `nested`, `field`, `rooftop`, `sheds`, `carports`, `garageBoxes`, `other`). See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automatedParkingGarage    
          - surface    
          - multiStorey    
          - singleLevel    
          - multiLevel    
          - openSpace    
          - covered    
          - nested    
          - field    
          - rooftop    
          - sheds    
          - carports    
          - garageBoxes    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
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
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    maximumAllowedWidth:    
      description: |-    
        Maximum allowed width for vehicles. If there are    
            multiple zones, it will be the minimum width of all the zones.    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    measuresPeriod:    
      description: 'The measures period related to availableSpotNumber and priceRatePerMinute.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    measuresPeriodUnit:    
      description: 'The measures period unit related to availableSpotNumber and PriceRatePerMinute.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/unitText    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancy:    
      maximum: 1    
      minimum: 0    
      type: number    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_:`none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`, Or any other application-specific'    
      items:    
        enum:    
          - balancing    
          - manual    
          - modelBased    
          - none    
          - singleSpaceDetection    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: ""    
    occupancyModified:    
      description: 'Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    occupiedSpotNumber:    
      description: 'Number of spots occupied. Allowed values: 0 - `totalSpotNumber`'    
      minimum: 0    
      type: Property    
    openingHours:    
      description: 'Opening hours of the parking site.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    parkingMode:    
      description: 'Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration: `perpendicularParking`, `parallelParking`, `echelonParking`'    
      items:    
        enum:    
          - perpendicularParking    
          - parallelParking    
          - echelonParking    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    priceCurrency:    
      description: 'Price currency of price rate per minute'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
    priceRatePerMinute:    
      description: 'Price rate per minute.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
    provider:    
      type: object    
    refParkingAccess:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site''s access point(s).'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    refParkingGroup:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Relationship. Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
      x-ngsi:    
        model: http://schema.org/Number    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Relationship. Individual parking spots belonging to this offstreet parking site.'    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ",". For instance "residentPermit,disabledPermit" stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3.(`employeePermit`, `studentPermit`, `fairPermit`, `governmentPermit`, `residentPermit`, `specificIdentifiedVehiclePermit`, `visitorPermit`, `noPermitNeeded`)orb any other application-specific'    
      items:    
        enum:    
          - employeePermit    
          - fairPermit    
          - governmentPermit    
          - noPermitNeeded    
          - residentPermit    
          - specificIdentifiedVehiclePermit    
          - studentPermit    
          - visitorPermit    
        type: string    
      minItems: 0    
      type: Property    
      uniqueItems: true    
    reservationType:    
      description: 'he following specified by _ReservationTypeEnum_ of DATEX II version 2.3: (`optional`, `mandatory`, `notAvailable`, `partly`).'    
      items:    
        enum:    
          - optional    
          - mandatory    
          - notAvailable    
          - partly    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    security:    
      description: 'Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3:  (`patrolled`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences`      `areaSeperatedFromSurroundings`) or any other application-specific'    
      items:    
        enum:    
          - patrolled    
          - securityStaff    
          - externalSecurity    
          - cctv    
          - dog    
          - guard24hours    
          - lighting    
          - floodLight    
          - fences    
          - areaSeperatedFromSurroundings    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    specialLocation:    
      description: 'If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of   [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a): (`airportTerminal`, `exhibitonCentre`, `shoppingCentre`, `specificFacility`, `trainStation`, `campground`, `themePark`, `ferryTerminal`, `vehicleOnRailTerminal`, `coachStation`,   `cableCarStation`, `publicTransportStation`, `market`, `religiousCentre`, `conventionCentre`, `cinema`, `skilift`, `hotel`, `other`)'    
      items:    
        enum:    
          - airportTerminal    
          - exhibitonCentre    
          - shoppingCentre    
          - specificFacility    
          - trainStation    
          - campground    
          - themePark    
          - ferryTerminal    
          - vehicleOnRailTerminal    
          - coachStation    
          - cableCarStation    
          - publicTransportStation    
          - market    
          - religiousCentre    
          - conventionCentre    
          - cinema    
          - skilift    
          - hotel    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    status:    
      description: |-    
        Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3 :    
         -   _ParkingSiteStatusEnum_    
         -   _OpeningStatusEnum_    
         -   (`open`, `closed`, `closedAbnormal`,`openingTimesInForce`, `full`,    
         `fullAtEntrance`, `spacesAvailable`, `almostFull`)    
         -   Or any other application-specific    
      items:    
        enum:    
          - open    
          - closed    
          - closedAbnormal    
          - openingTimesInForce    
          - full    
          - fullAtEntrance    
          - spacesAvailable    
          - almostFull    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    totalSpotNumber:    
      description: 'The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    type:    
      description: 'It has to be OffStreetParking'    
      enum:    
        - OffStreetParking    
      type: Property    
    usageScenario:    
      description: 'Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3:(`truckParking`, `parkAndRide`, `parkAndCycle`, `parkAndWalk`, `kissAndRide`, `liftshare`, `carSharing`, `restArea`, `serviceArea`, `dropOffWithValet`, `dropOffMechanical`, `eventParking`, `automaticParkingGuidance`, `staffGuidesToSpace`, `vehicleLift`, `loadingBay`, `dropOff`, `overnightParking`, `other` Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - truckParking    
          - parkAndRide    
          - parkAndCycle    
          - parkAndWalk    
          - kissAndRide    
          - liftshare    
          - carSharing    
          - restArea    
          - serviceArea    
          - dropOffWithValet    
          - dropOffMechanical    
          - eventParking    
          - automaticParkingGuidance    
          - staffGuidesToSpace    
          - vehicleLift    
          - loadingBay    
          - dropOff    
          - overnightParking    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    vehicleEntranceCount:    
      description: 'Aggregated number of vehicle that enter the parking site in a period of time.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    vehicleExitCount:    
      description: 'Aggregated number of vehicle that leave the parking site in a period of time.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
#### OffStreetParking NGSI V2 key-values Example    
Here is an example of a OffStreetParking in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "porto-ParkingLot-23889",  
  "type": "OffStreetParking",  
  "name": "Parque de estacionamento Trindade",  
  "category": [  
    "underground",  
    "public",  
    "feeCharged",  
    "mediumTerm",  
    "barrierAccess"  
  ],  
  "extCategory": ["A"],  
  "chargeType": ["temporaryPrice"],  
  "requiredPermit": [],  
  "layout": ["multiLevel"],  
  "maximumParkingDuration": "PT8H",  
  "location": {  
    "coordinates": [-8.60961198807, 41.150691773],  
    "type": "Point"  
  },  
  "allowedVehicleType": ["car"],  
  "totalSpotNumber": 414,  
  "availableSpotNumber": 132,  
  "occupiedSpotNumber": 282,  
  "occupancyModified": "2018-09-21T12:00:00Z",  
  "occupancy": 0.68,  
  "address": {  
    "streetAddress": "Rua de Fernandes Tomás",  
    "addressLocality": "Porto",  
    "addressCountry": "Portugal"  
  },  
  "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
  "dateModified": "2018-09-21T12:00:05Z",  
  "vehicleEntranceCount": 28,  
  "vehicleExitCount": 12,  
  "accessModified": "2018-09-21T12:00:00Z"  
}  
```  
#### OffStreetParking NGSI V2 normalized Example    
Here is an example of a OffStreetParking in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "porto-ParkingLot-23889",  
  "type": "OffStreetParking",  
  "category": {  
    "value": [  
      "underground",  
      "public",  
      "feeCharged",  
      "mediumTerm",  
      "barrierAccess"  
    ]  
  },  
  "extCategory": ["A"],  
  "layout": {  
    "value": ["multiLevel"]  
  },  
  "name": {  
    "value": "Parque de estacionamento Trindade"  
  },  
  "requiredPermit": {  
    "value": []  
  },  
  "allowedVehicleType": {  
    "value": ["car"]  
  },  
  "availableSpotNumber": {  
    "value": 132,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-21T12:00:00Z"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "value": 414  
  },  
  "occupiedSpotNumber": {  
    "type": "number",  
    "value": 282  
  },  
  "occupancyModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "occupancy": {  
    "type": "number",  
    "value": 0.68  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.60961198807, 41.150691773]  
    }  
  },  
  "chargeType": {  
    "value": ["temporaryPrice"]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Porto",  
      "addressCountry": "Portugal",  
      "streetAddress": "Rua de Fernandes Tom\u00e1s"  
    }  
  },  
  "maximumParkingDuration": {  
    "value": "PT8H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:05Z"  
  },  
  "description": {  
    "value": "Municipal car park located near the Trindade metro station and the Town Hall"  
  },  
  "vehicleEntranceCount": {  
    "type": "number",  
    "value": 28  
  },  
  "vehicleExitCount": {  
    "type": "number",  
    "value": 12  
  },  
  "accessModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  }  
}  
```  
#### OffStreetParking NGSI-LD key-values Example    
Here is an example of a OffStreetParking in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "Portugal",  
             "addressLocality": "Porto",  
             "streetAddress": "Rua de Fernandes TomÃ¡s",  
             "type": "PostalAddress"},  
 "allowedVehicleType": ["car"],  
 "availableSpotNumber": 132,  
 "occupiedSpotNumber": 282,  
 "occupancyModified": "2018-09-21T12:00:00Z",  
 "occupancy": 0.68,  
 "category": ["underground",  
              "public",  
              "feeCharged",  
              "mediumTerm",  
              "barrierAccess"],  
 "chargeType": ["temporaryPrice"],  
 "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
 "extCategory": ["A"],  
 "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
 "layout": ["multiLevel"],  
 "location": {"coordinates": [-8.60961198807, 41.150691773], "type": "Point"},  
 "maximumParkingDuration": "PT8H",  
 "modifiedAt": "2018-09-21T12:00:05Z",  
 "name": "Parque de estacionamento Trindade",  
 "requiredPermit": [],  
 "totalSpotNumber": 414,  
 "vehicleEntranceCount": 28,  
 "vehicleExitCount": 12,  
 "accessModified": "2018-09-21T12:00:00Z",  
 "type": "OffStreetParking"}  
```  
#### OffStreetParking NGSI-LD normalized Example    
Here is an example of a OffStreetParking in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
    "type": "OffStreetParking",  
    "modifiedAt": "2018-09-21T12:00:05Z",  
    "category": {  
        "type": "Property",  
        "value": [  
            "underground",  
            "public",  
            "feeCharged",  
            "mediumTerm",  
            "barrierAccess"  
        ]  
    },  
    "extCategory": {  
        "type": "Property",  
        "value": ["A"]  
    },  
    "layout": {  
        "type": "Property",  
        "value": [  
            "multiLevel"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "Parque de estacionamento Trindade"  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": []  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car"  
        ]  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 132,  
        "observedAt": "2018-09-21T12:00:00Z"  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 414  
    },  
    "occupiedSpotNumber": {  
        "type": "Property",  
        "value": 282  
    },  
    "occupancyModified": {  
        "type": "Property",  
        "value": "2018-09-21T12:00:00Z"  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.68  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -8.60961198807,  
                41.150691773  
            ]  
        }  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "temporaryPrice"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Porto",  
            "addressCountry": "Portugal",  
            "streetAddress": "Rua de Fernandes TomÃ¡s",  
            "type": "PostalAddress"  
        }  
    },  
    "maximumParkingDuration": {  
        "type": "Property",  
        "value": "PT8H"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Municipal car park located near the Trindade metro station and the Town Hall"  
    },  
    "vehicleEntranceCount": {  
        "type": "Property",  
        "value": 28  
    },  
      "vehicleExitCount": {  
        "type": "Property",  
        "value": 12  
    },  
      "accessModified": {  
        "type": "Property",  
        "value": "2018-09-21T12:00:00Z"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
