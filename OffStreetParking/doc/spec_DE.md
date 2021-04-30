Entität: OffStreetParking  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
Globale Beschreibung: **Parken auf der Straße**  

## Liste der Eigenschaften  

- `acceptedPaymentMethod`: Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'. Akzeptierte Zahlungsmethode(n).  - `accessModified`: Zeitstempel, wann `vehicleEntranceCount` und `vehicleExitCount` aktualisiert wurde. Erlaubte Werte: ISO8601  - `address`: Die Postanschrift.  - `aggregateRating`: Aggregierte Bewertung für diesen Stellplatz.  - `allowedVehicleType`:  Erlaubte(r) Fahrzeugtyp(en). Das erste Element dieses Arrays _MUSS_ der erlaubte Hauptfahrzeugtyp sein. Freie Stellplatznummern anderer erlaubter Fahrzeugtypen können unter dem Attribut `extraSpotNumber` und durch spezifische Entitäten des Typs _ParkingGroup_ gemeldet werden. Die folgenden Werte sind durch _VehicleTypeEnum_ definiert, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `availableSpotNumber`: Die Anzahl der verfügbaren Stellplätze (_inklusive_ aller Fahrzeugtypen oder reservierter Plätze, z. B. für Behinderte, Dauerparker usw.). Dies kann bei Parkplätzen, bei denen die Grenzen der Stellplätze nicht eindeutig durch Linien markiert sind, schwieriger zu schätzen sein. Erlaubte Werte: Eine positive ganze Zahl, einschließlich 0. Sie muss kleiner oder gleich sein als `totalSpotNumber`.  - `averageSpotLength`: Die durchschnittliche Länge von Parkplätzen.  - `averageSpotWidth`: Die durchschnittliche Breite von Parkplätzen.  - `category`: Die Kategorie(n) des Parkplatzes. Der Zweck dieses Feldes ist die Kennzeichnung von Parkplätzen abseits der Straße im Allgemeinen  - `chargeType`: Art(en) der vom Parkplatz durchgeführten Gebühren. Erlaubte Werte: Einige der in der DATEX II Version 2.3 _ ChargeTypeEnum_ Aufzählung definierten. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'. Oder jede andere anwendungsspezifische  - `contactPoint`: Kontaktstelle für den Parkplatz.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `extCategory`: Externe Kategorie zu Kategorie ergänzen.  - `extraSpotNumber`: Die Anzahl der zusätzlichen Spots, die _verfügbar_, d. h. frei sind. Dieser Wert muss freie Plätze aus allen unten genannten Gruppen zusammenfassen: A/ Diejenigen, die für besondere Zwecke reserviert sind und normalerweise eine Genehmigung erfordern. Die Details zu den Genehmigungen finden Sie auf der Ebene der Parkgruppe (Entität vom Typ `ParkingGroup`). B/ Diejenigen, die für andere Fahrzeugtypen reserviert sind, die sich vom erlaubten Hauptfahrzeugtyp unterscheiden. C/ Jede andere Gruppe von Parkplätzen, die nicht den durch diese Entität vermittelten allgemeinen Bedingungsregeln unterliegen.  - `facilities`: Erlaubte Werte: Die folgenden, definiert durch die Aufzählung _EquipmentTypeEnum_ von DATEX II Version 2.3. Enum:'bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, eisfreiesGerüst, Informationspunkt, InternetWireless, Gepäckaufbewahrung, PayDesk, Zahlungsautomat, Spielplatz, öffentlichesTelefon, refuseBin, safeDeposit, Dusche, Toilette, tollTerminal, vendingMachine, wasteDisposal' . Jede andere anwendungsspezifische  - `firstAvailableFloor`: Nummer der Etage, die dem Boden am nächsten liegt und in der aktuell freie Parkplätze vorhanden sind. Erlaubte Werte: Stockwerke werden zwischen -n und n nummeriert, wobei 0 Erdgeschoss ist.  - `highestFloor`: Bei Parkplätzen mit mehreren Etagen die höchste Etage. Eine ganzzahlige Zahl. 0 ist Erdgeschoss. Obere Etagen sind positive Zahlen. Untere Etagen sind negative Zahlen.  - `id`: Eindeutiger Bezeichner der Entität  - `images`: Eine URL, die ein Foto dieses Parkplatzes enthält  - `layout`: Parkplatz-Layout. Gibt dem Attribut `category` mehr Details. Erlaubte Werte: Entsprechend dem _ParkingLayoutEnum_ von DATEX II Version 2.3. Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'. Siehe auch [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Oder jeder andere Wert, der für die Anwendung nützlich ist und oben nicht behandelt wurde.  - `location`:   - `lowestFloor`: Bei Parkplätzen mit mehreren Stockwerken, unterstes Stockwerk. Erlaubte Werte: Eine ganzzahlige Zahl.  - `maximumAllowedHeight`: Maximal zulässige Höhe für Fahrzeuge. Wenn es mehrere Zonen gibt, ist es die Mindesthöhe aller Zonen.  - `maximumAllowedWidth`: Maximal zulässige Breite für Fahrzeuge. Wenn es mehrere Zonen gibt, ist es die Mindestbreite aller Zonen.  - `maximumParkingDuration`: Maximal zulässige Aufenthaltsdauer am Standort, auf allgemeiner Basis, kodiert als ISO8601-Dauer oder mit einer beliebigen anderen für das Parken relevanten Zeichenfolge.  Ein leerer Wert oder ein nicht vorhandener Wert bedeutet eine unbestimmte Dauer  - `measuresPeriod`: Der Maßnahmenzeitraum bezieht sich auf availableSpotNumber und priceRatePerMinute.  - `measuresPeriodUnit`: Die Maßnahmen Periodeneinheit bezogen auf availableSpotNumber und PriceRatePerMinute.  - `name`: Der Name dieses Elements.  - `occupancy`: Relativer Wert der belegten Spots im Verhältnis zu den gesamten Spots.  - `occupancyDetectionType`: Methode(n) der Belegungserkennung.  Erlaubte Werte: Die folgenden aus DATEX II Version 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Oder beliebige andere anwendungsspezifische  - `occupancyModified`: Relativer Wert der belegten Spots im Verhältnis zu den gesamten Spots. Erlaubte Werte: 0 - 1  - `occupiedSpotNumber`: Anzahl der belegten Plätze. Erlaubte Werte: 0 - `totalSpotNumber`  - `openingHours`: Öffnungszeiten des Parkplatzes.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `parkingMode`: Parkmodus(e). Erlaubte Werte: Die durch die DATEX II Version 2.3 _ParkingModeEnum_ Aufzählung definierten. Enum:'echelonParking, parallelParking, perpendicularParking'  - `priceCurrency`: Preiswährung der Preisrate pro Minute  - `priceRatePerMinute`: Preistarif pro Minute.  - `provider`: Parkplatz-Dienstleister  - `refParkingAccess`: Zugangspunkt(e) des Parkplatzes.  - `refParkingGroup`: Identifizierte Gruppe(n) von Stellplätzen. Eine Gruppe kann einer Zone, einer kompletten Etage, einer Gruppe von Stellplätzen usw. entsprechen.  - `refParkingSpot`: Einzelne Stellplätze, die zu diesem OffStreet-Parkplatz gehören.  - `requiredPermit`: Mit diesem Attribut wird erfasst, welche Genehmigung(en) zum Parken an diesem Standort erforderlich sein könnte(n). Die Semantik ist, dass mindestens _eine_ dieser Genehmigungen zum Parken benötigt wird. Wenn eine Genehmigung aus mehr als einem Element (und) besteht, können sie mit einem ',' kombiniert werden. Zum Beispiel bedeutet 'residentPermit,disabledPermit', dass sowohl eine Anwohner- als auch eine Behindertengenehmigung zum Parken benötigt wird. Wenn die Liste leer ist, wird keine Genehmigung benötigt. Erlaubte Werte: Die folgenden, definiert durch die _PermitTypeEnum_-Enumeration von DATEX II Version 2.3. Enum:'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'. Oder jede andere anwendungsspezifische  - `reservationType`: as Folgende wird durch _ReservationTypeEnum_ von DATEX II Version 2.3 spezifiziert. Enum:'mandatory, notAvailable, optional, partly'  - `security`: Sicherheitsaspekte, die dieser Stellplatz bietet. Erlaubte Werte: Die folgenden, einige davon, definiert durch _ParkingSecurityEnum_ von DATEX II Version 2.3. Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' . oder jede andere anwendungsspezifische  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `specialLocation`: Wenn sich der Parkplatz an einem besonderen Ort befindet (Flughafen, Kaufhaus usw.), gibt er an, was ein solcher besonderer Ort ist.  Erlaubte Werte: Die durch _ParkingSpecialLocationEnum_ von [DATEX II Version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a) definierten. Enum:'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'  - `status`: Status des Stellplatzes. Erlaubte Werte: Die folgenden, die durch die folgenden, in DATEX II Version 2.3 definierten Aufzählungen festgelegt sind. Enum:'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'. Oder jede andere anwendungsspezifische  - `totalSpotNumber`: Die Gesamtzahl der von diesem Parkplatz angebotenen Plätze.  Diese Zahl kann bei Parkplätzen, auf denen die Plätze nicht eindeutig durch Linien gekennzeichnet sind, schwer zu ermitteln sein. Erlaubte Werte: Jede positive ganze Zahl oder 0. Normative Verweise: DATEX 2 Version 2.3 Attribut _parkingNumberOfSpaces_ der Klasse _ParkingRecord_.  - `type`: Es muss OffStreetParking sein  - `usageScenario`: Verwendungsszenario(s). Gibt dem Attribut `category` mehr Details. Erlaubte Werte: Die durch die Aufzählung _ParkingUsageScenarioEnum_ von DATEX II Version 2.3 definierten. Enum:'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'. Oder jeder andere Wert, der für die Anwendung nützlich ist und oben nicht behandelt wurde.  - `vehicleEntranceCount`: Aggregierte Anzahl der Fahrzeuge, die in einem bestimmten Zeitraum auf den Parkplatz fahren.  - `vehicleExitCount`: Aggregierte Anzahl von Fahrzeugen, die den Parkplatz in einem bestimmten Zeitraum verlassen.    
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`    
Ein Stellplatz abseits der Straße, der für das Abstellen von Fahrzeugen vorgesehen ist, unabhängig verwaltet wird und über geeignete und deutlich gekennzeichnete Zufahrten (Ein- und Ausfahrten) verfügt. Bei Bedarf und zu Verwaltungszwecken oder zur Behandlung von Parkplätzen mit mehreren Standorten kann er in verschiedene Zonen unterteilt werden, die durch den Entitätstyp [ParkingGroup] (../ParkingGroup/README.md) modelliert werden. In der Terminologie von DATEX 2 Version 2.3 entspricht sie einem _UrbanParkingSite_ vom Typ _offStreetParking_. Ein Datenwörterbuch für DATEX II-Begriffe finden Sie unter [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OffStreetParking:    
  description: 'Off street parking'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm''. Accepted payment method(s).'    
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
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    aggregateRating:    
      description: 'Aggregated rating for this parking site.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
    allowedVehicleType:    
      description: ' Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. Free spot numbers of other allowed vehicle types might be reported under the attribute `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:''agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'''    
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
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
        model: http://schema.org/length    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/width    
        units: meters    
    category:    
      description: 'Parking site''s category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities'    
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
      description: 'Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration. Enum:''additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice''. Or any other application-specific'    
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
      description: 'External category to complement category.'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    facilities:    
      description: 'Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3. Enum:''bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, iceFreeScaffold, informationPoint, internetWireless, luggageLocker, payDesk, paymentMachine, playground, publicPhone, refuseBin, safeDeposit, shower, toilet, tollTerminal, vendingMachine, wasteDisposal'' . Any other application-specific'    
      items:    
        enum:    
          - bikeParking    
          - cashMachine    
          - copyMachineOrService    
          - defibrillator    
          - dumpingStation    
          - electricChargingStation    
          - elevator    
          - faxMachineOrService    
          - fireHose    
          - fireExtinguisher    
          - fireHydrant    
          - firstAidEquipment    
          - freshWater    
          - iceFreeScaffold    
          - informationPoint    
          - internetWireless    
          - luggageLocker    
          - payDesk    
          - paymentMachine    
          - playground    
          - publicPhone    
          - refuseBin    
          - safeDeposit    
          - shower    
          - toilet    
          - tollTerminal    
          - vendingMachine    
          - wasteDisposal    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    images:    
      description: 'A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/image    
    layout:    
      description: 'Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3. Enum:''automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other''. See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automatedParkingGarage    
          - carports    
          - covered    
          - field    
          - garageBoxes    
          - multiLevel    
          - multiStorey    
          - nested    
          - openSpace    
          - rooftop    
          - sheds    
          - singleLevel    
          - surface    
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
        model: http://schema.org/heigth    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/width    
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
      description: 'Relative value of occupied spots out of the total spots.'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. Or any other application-specific'    
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
        model: http://schema.org/Text    
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
      x-ngsi:    
        model: http://schema.org/Number    
    openingHours:    
      description: 'Opening hours of the parking site.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parkingMode:    
      description: 'Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:''echelonParking, parallelParking, perpendicularParking'''    
      items:    
        enum:    
          - echelonParking    
          - parallelParking    
          - perpendicularParking    
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
      description: 'Parking site service provider'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/provider    
    refParkingAccess:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site''s access point(s).'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    refParkingGroup:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Individual parking spots belonging to this offStreet parking site.'    
      type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3. Enum:''employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit''. Or any other application-specific'    
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
      description: 'he following specified by _ReservationTypeEnum_ of DATEX II version 2.3. Enum:''mandatory, notAvailable, optional, partly'''    
      items:    
        enum:    
          - mandatory    
          - notAvailable    
          - optional    
          - partly    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    security:    
      description: 'Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3. Enum:''areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff'' . or any other application-specific'    
      items:    
        enum:    
          - areaSeparatedFromSurroundings    
          - cctv    
          - dog    
          - externalSecurity    
          - fences    
          - floodLight    
          - guard24hours    
          - lighting    
          - patrolled    
          - securityStaff    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    specialLocation:    
      description: 'If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:''airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'''    
      items:    
        enum:    
          - airportTerminal    
          - cableCarStation    
          - campground    
          - cinema    
          - coachStation    
          - conventionCentre    
          - exhibitionCentre    
          - ferryTerminal    
          - hotel    
          - market    
          - publicTransportStation    
          - religiousCentre    
          - shoppingCentre    
          - skilift    
          - specificFacility    
          - themePark    
          - trainStation    
          - vehicleOnRailTerminal    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    status:    
      description: 'Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3. Enum:''almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable''. Or any other application-specific'    
      items:    
        enum:    
          - almostFull    
          - closed    
          - closedAbnormal    
          - full    
          - fullAtEntrance    
          - open    
          - openingTimesInForce    
          - spacesAvailable    
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
      description: 'Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3. Enum:''automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other''. Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automaticParkingGuidance    
          - carSharing    
          - dropOffWithValet    
          - dropOffMechanical    
          - dropOff    
          - eventParking    
          - kissAndRide    
          - liftShare    
          - loadingBay    
          - overnightParking    
          - parkAndCycle    
          - parkAndRide    
          - parkAndWalk    
          - restArea    
          - serviceArea    
          - staffGuidesToSpace    
          - truckParking    
          - vehicleLift    
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
</details>    
## Beispiel-Nutzlasten  
#### OffStreetParking NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein OffStreetParking im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### OffStreetParking NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein OffStreetParking im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### OffStreetParking NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein OffStreetParking im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": [  
      "A"  
    ]  
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
      "streetAddress": "Rua de Fernandes Tom\u00e1s",  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### OffStreetParking NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein OffStreetParking im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "Portugal",  
    "addressLocality": "Porto",  
    "streetAddress": "Rua de Fernandes Tom\u00e1s",  
    "type": "PostalAddress"  
  },  
  "allowedVehicleType": [  
    "car"  
  ],  
  "availableSpotNumber": 132,  
  "occupiedSpotNumber": 282,  
  "occupancyModified": "2018-09-21T12:00:00Z",  
  "occupancy": 0.68,  
  "category": [  
    "underground",  
    "public",  
    "feeCharged",  
    "mediumTerm",  
    "barrierAccess"  
  ],  
  "chargeType": [  
    "temporaryPrice"  
  ],  
  "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
  "extCategory": [  
    "A"  
  ],  
  "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
  "layout": [  
    "multiLevel"  
  ],  
  "location": {  
    "coordinates": [  
      -8.60961198807,  
      41.150691773  
    ],  
    "type": "Point"  
  },  
  "maximumParkingDuration": "PT8H",  
  "modifiedAt": "2018-09-21T12:00:05Z",  
  "name": "Parque de estacionamento Trindade",  
  "requiredPermit": [],  
  "totalSpotNumber": 414,  
  "vehicleEntranceCount": 28,  
  "vehicleExitCount": 12,  
  "accessModified": "2018-09-21T12:00:00Z",  
  "type": "OffStreetParking"  
}  
```  
