Entité : OffStreetParking  
=========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Stationnement dans la rue**  

## Liste des propriétés  

- `acceptedPaymentMethod`: Enum : 'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'. Méthode(s) de paiement acceptée(s).  - `accessModified`: Horodatage de la mise à jour de `vehicleEntranceCount` et `vehicleExitCount`. Valeurs autorisées : ISO8601  - `address`: L'adresse postale  - `aggregateRating`: Note agrégée pour ce site de stationnement.  - `allowedVehicleType`:  Type(s) de véhicule(s) autorisé(s). Le premier élément de ce tableau _Doit_ être le principal type de véhicule autorisé. Les numéros d'emplacements libres d'autres types de véhicules autorisés peuvent être signalés par l'attribut `extraSpotNumber` et par des entités spécifiques de type _ParkingGroup_. Les valeurs suivantes sont définies par _VehicleTypeEnum_, [DATEX 2 version 2.3] (http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum : 'agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'.  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableSpotNumber`: Le nombre de places disponibles (_y compris_ tous les types de véhicules ou les places réservées, telles que celles destinées aux personnes handicapées, aux personnes en stationnement de longue durée, etc.) Il peut être plus difficile d'estimer le nombre de places disponibles dans les parkings où les limites des places ne sont pas clairement marquées par des lignes. Valeurs autorisées : Un nombre entier positif, y compris 0. Il doit être inférieur ou égal à `totalSpotNumber`.  - `averageSpotLength`: La durée moyenne des places de stationnement.  - `averageSpotWidth`: La largeur moyenne des places de stationnement.  - `category`: Catégorie(s) du site de stationnement. L'objectif de ce champ est de permettre de marquer, d'une manière générale, les entités de stationnement hors voirie.  - `chargeType`: Type(s) de frais effectués par le site de stationnement. Valeurs autorisées : Certaines de celles définies par l'énumération DATEX II version 2.3 _ ChargeTypeEnum_. Enum : 'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'. Ou toute autre application spécifique  - `contactPoint`: Point de contact du site de stationnement.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `extCategory`: Catégorie externe à la catégorie complémentaire.  - `extraSpotNumber`: Le nombre de places supplémentaires _disponibles_, c'est-à-dire libres. Cette valeur doit agréger les emplacements libres de tous les groupes mentionnés ci-dessous : A/ Ceux qui sont réservés à des fins spéciales et qui nécessitent généralement un permis. Les détails du permis se trouvent au niveau du groupe de stationnement (entité de type `ParkingGroup`). B/ Ceux réservés à d'autres types de véhicules que le principal type de véhicule autorisé. C/ Tout autre groupe de places de stationnement qui n'est pas soumis aux règles de conditions générales véhiculées par cette entité.  - `facilities`: Valeurs autorisées : Les valeurs suivantes définies par l'énumération _EquipmentTypeEnum_ de DATEX II version 2.3. Enum :'bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, échafaudage sans glace, point d'information, internet sans fil, consigne à bagages, caisse de paiement, machine de paiement, aire de jeux, téléphone public, poubelle, coffre-fort, douche, toilettes, terminal de péage, distributeur automatique, élimination des déchets' . Toute autre application spécifique  - `firstAvailableFloor`: Numéro de l'étage le plus proche du sol qui dispose actuellement de places de parking disponibles. Valeurs autorisées : Les étages sont numérotés entre -n et n, étant 0 rez-de-chaussée.  - `highestFloor`: Pour les parkings à étages multiples, l'étage le plus élevé. Il s'agit d'un nombre entier. 0 est le niveau du sol. Les étages supérieurs sont des nombres positifs. Les étages inférieurs sont des nombres négatifs.  - `id`: Identifiant unique de l'entité  - `images`: Une URL contenant une photo de ce site de stationnement  - `layout`: Mise en page du parking. Donne plus de détails à l'attribut `category`. Valeurs autorisées : Selon le _ParkingLayoutEnum_ de DATEX II version 2.3. Enum : 'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'. Voir également [OpenStreetMap] (http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Ou toute autre valeur utile pour l'application et non couverte ci-dessus.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `lowestFloor`: Pour les sites de stationnement avec plusieurs niveaux de plancher, le plancher le plus bas. Valeurs autorisées : Un nombre entier.  - `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules. S'il y a plusieurs zones, il s'agira de la hauteur minimale de toutes les zones.  - `maximumAllowedWidth`: Largeur maximale autorisée pour les véhicules. S'il y a plusieurs zones, il s'agira de la largeur minimale de toutes les zones.  - `maximumParkingDuration`: Séjour maximal autorisé sur le site, en général, encodé sous forme de durée ISO8601 ou de toute autre chaîne de caractères pertinente pour le stationnement.  Une valeur vide ou non présente indique une durée indéterminée.  - `measuresPeriod`: La période de mesure est liée à availableSpotNumber et priceRatePerMinute.  - `measuresPeriodUnit`: L'unité de période de mesure liée à availableSpotNumber et PriceRatePerMinute.  - `name`: Le nom de cet élément.  - `occupancy`: Valeur relative des emplacements occupés par rapport à l'ensemble des emplacements.  - `occupancyDetectionType`: Méthode(s) de détection de l'occupation.  Valeurs autorisées : Les valeurs suivantes de DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum : "équilibrage, manuel, modelBased, none, singleSpaceDetection". Ou toute autre application spécifique  - `occupancyModified`: Valeur relative des emplacements occupés par rapport à l'ensemble des emplacements. Valeurs autorisées : 0 - 1  - `occupiedSpotNumber`: Nombre de places occupées. Valeurs autorisées : 0 - `totalSpotNumber`  - `openingHours`: Heures d'ouverture du site de stationnement.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `parkingMode`: Mode(s) de stationnement. Valeurs autorisées : Celles définies par l'énumération _ParkingModeEnum_ de DATEX II version 2.3. Enum : 'echelonParking, parallelParking, perpendicularParking'.  - `priceCurrency`: Devise du prix du tarif par minute  - `priceRatePerMinute`: Tarif par minute.  - `provider`: Fournisseur de services pour les sites de stationnement  - `refParkingAccess`: Point(s) d'accès du site de stationnement.  - `refParkingGroup`: Groupe(s) identifié(s) du site de stationnement. Un groupe peut correspondre à une zone, un étage complet, un groupe de places, etc.  - `refParkingSpot`: Places de stationnement individuelles appartenant à ce site de stationnement hors voirie.  - `requiredPermit`: Cet attribut indique le ou les permis qui peuvent être nécessaires pour se garer sur ce site. La sémantique est qu'au moins _un_ de ces permis est nécessaire pour se garer. Lorsqu'un permis est composé de plus d'un élément (et), il peut être combiné avec un ','. Par exemple, 'residentPermit,disabledPermit' signifie qu'il faut à la fois un permis de résident et un permis d'invalide pour stationner. Si la liste est vide, aucun permis n'est nécessaire. Valeurs autorisées : Les suivantes, définies par l'énumération _PermitTypeEnum_ de DATEX II version 2.3. Enum : 'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'. Ou toute autre application spécifique  - `reservationType`: e qui suit est spécifié par _ReservationTypeEnum_ de DATEX II version 2.3. Enum : "obligatoire, non disponible, facultatif, partiellement".  - `security`: Aspects sécuritaires fournis par ce site de stationnement. Valeurs autorisées : Les suivantes, dont certaines sont définies par _ParkingSecurityEnum_ de DATEX II version 2.3. Enum : 'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' . ou toute autre valeur spécifique à l'application.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `specialLocation`: Si le site de stationnement se trouve à un endroit particulier (aéroport, grand magasin, etc.), il indique en quoi consiste cet endroit particulier.  Valeurs autorisées : Celles définies par _ParkingSpecialLocationEnum_ de [DATEX II version 2.3] (http://www.datex2.eu/content/parking-publications-extension-v10a). Enum : 'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other' (terminal d'aéroport, station de téléphérique, terrain de camping, cinéma, station d'autocar, centre de congrès, centre d'exposition, terminal de ferry, autre)  - `status`: Statut du site de stationnement. Valeurs autorisées : Les valeurs suivantes définies par les énumérations suivantes définies par DATEX II version 2.3. Enum : "almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable". Ou toute autre application spécifique  - `totalSpotNumber`: Le nombre total de places offertes par ce site de stationnement.  Ce nombre peut être difficile à obtenir pour les parkings sur lesquels les places ne sont pas clairement marquées par des lignes. Valeurs autorisées : Tout nombre entier positif ou 0. Références normatives : DATEX 2 version 2.3 attribut _parkingNumberOfSpaces_ de la classe _ParkingRecord_.  - `type`: Il doit s'agir du stationnement hors voirie.  - `usageScenario`: Scénario d'utilisation(s). Donne plus de détails à l'attribut `category`. Valeurs autorisées : Celles définies par l'énumération _ParkingUsageScenarioEnum_ de DATEX II version 2.3. Enum : 'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'. Ou toute autre valeur utile pour l'application et non couverte ci-dessus.  - `vehicleEntranceCount`: Nombre agrégé de véhicules qui entrent dans le site de stationnement pendant une période donnée.  - `vehicleExitCount`: Nombre agrégé de véhicules qui quittent le site de stationnement au cours d'une période donnée.    
Propriétés requises  
- `id`  - `location`  - `type`    
Un site, hors de la rue, destiné au stationnement des véhicules, géré de manière indépendante et avec des points d'accès (entrées et sorties) appropriés et clairement indiqués. Si nécessaire, et à des fins de gestion ou pour traiter des sites de stationnement à emplacements multiples, il peut être divisé en différentes zones modélisées par le type d'entité [ParkingGroup](../ParkingGroup/README.md) . Dans la terminologie de DATEX 2 version 2.3, il correspond à un _UrbanParkingSite_ de type _offStreetParking_. Un dictionnaire de données pour les termes DATEX II se trouve à l'adresse [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
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
            format: uri    
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
## Exemples de charges utiles  
#### OffStreetParking Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un OffStreetParking au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Stationnement hors voirie NGSI-v2 normalisé Exemple  
Voici un exemple d'un OffStreetParking au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### OffStreetParking Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un OffStreetParking au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Stationnement hors rue NGSI-LD normalisé Exemple  
Voici un exemple d'un OffStreetParking au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
