Entité : OffStreetParking  
=========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Parking hors rue**  

## Liste des biens  

`acceptedPaymentMethod`: Mode(s) de paiement accepté(s).  `accessModified`: Horodatage de la mise à jour du "compte d'entrée des véhicules" et du "compte de sortie des véhicules". Valeurs autorisées : ISO8601  `address`: L'adresse postale.  `aggregateRating`: Cote agrégée pour ce parking.  `allowedVehicleType`:  Type(s) de véhicule(s) autorisé(s). Le premier élément de cette  
 tableau _Doit_ être le principal type de véhicule autorisé. Les numéros d'emplacement libres de  
 d'autres types de véhicules autorisés peuvent être déclarés sous l'attribut  
 `extraSpotNumber` et par des entités spécifiques de type _ParkingGroup_. Les valeurs suivantes définies par _VehicleTypeEnum_,  
 [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)Valeurs autorisées (`véhicule agricole`, `bicyclette`, `bus`, `voiture`, `caravane`, `carWithCaravan`, `carWithTrailer`,Véhicule de construction ou d'entretien, camion, cyclomoteur, moto, moto avec side-car, scooter, camion-citerne, remorque, fourgon, tout véhicule)  `alternateName`: Un autre nom pour cet article  `areaServed`: La zone géographique où un service ou un article offert est fourni.  `availableSpotNumber`: Le nombre de places disponibles (_y compris_ tous les types de véhicules ou les places réservées, comme celles pour les personnes handicapées, les parqueurs de longue durée, etc.) ). Ce nombre peut être plus difficile à estimer dans les lieux de stationnement où les limites des places ne sont pas clairement indiquées par des lignes. Valeurs autorisées : Un nombre entier positif, y compris 0, qui doit être inférieur ou égal à "totalSpotNumber".  `averageSpotLength`: La longueur moyenne des places de stationnement.  `averageSpotWidth`: La largeur moyenne des places de stationnement.  `category`: Catégorie(s) du site de stationnement. Le but de ce champ est de permettre de marquer, d'une manière générale, les entités de stationnement hors rue. Les particularités et les descriptions détaillées doivent être trouvées sous les attributs spécifiques correspondants. Valeurs autorisées : - (`public`, `private`, `publicPrivate`, `urbanDeterrentParking`, `parkingGarage`, `parkingLot`, `shortTerm`, `mediumTerm`, `longTerm`, Gratuit, payant, avec du personnel, gardé, avec barrière, avec porte, gratuit, avec charge électrique, réservé aux résidents, Uniquement avec permis", "pour les employés", "pour les visiteurs", "pour les clients", "pour les étudiants", "pour les membres", "pour les personnes handicapées", "pour les résidents", "en sous-sol", "au sol") - La sémantique des valeurs "pourxxx" est que le parking offre des places spécifiques soumises à cette condition particulière. - La sémantique des valeurs "seulementxxx" est que le parking ne permet de se garer qu'à cette condition particulière. - Autres applications spécifiques  `chargeType`: Le(s) type(s) de charge effectué(s) par le site de stationnement. Valeurs autorisées : Certaines de celles définies par l'énumération DATEX II version 2.3 _ ChargeTypeEnum_ :  
 (`flat`, `minimum`, `maximum`, `additionalIntervalPrice`, `seasonTicket` `temporaryPrice` `firstIntervalPrice`, `annualPayment`, `monthlyPayment`, `free`, `other`) ou toute autre application spécifique  `contactPoint`: Point de contact du site de stationnement.  `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`: Une description de cet article  `extCategory`:   `extraSpotNumber`: Le nombre de places supplémentaires _disponibles_, c'est-à-dire gratuites. Cette valeur doit agréger les spots gratuits de tous les groupes mentionnés ci-dessous : A/ Ceux qui sont réservés à des fins spéciales et qui nécessitent généralement une autorisation. Les détails des permis se trouvent au niveau du groupe de stationnement (entité de type "groupe de stationnement"). B/ Celles réservées à d'autres types de véhicules que le type de véhicule principal autorisé. C/ Tout autre groupe de places de stationnement non soumis aux règles générales d'état véhiculées par cette entité.  `facilities`: Valeurs autorisées : Ce qui suit est défini par l'énumération _EquipmentTypeEnum_ de DATEX II version 2.3 : - (`toilet`, `shower`, `informationPoint`, `internetWireless`, `payDesk`, `paymentMachine`, `cashMachine`, `vendingMachine`,     faxMachineOrService", "copyMachineOrService", "safeDeposit", "luggageLocker", "publicPhone", "elevator", "dumpingStation" "freshWater", Élimination des déchets, poubelle, échafaudage sans glace, terrain de jeu, station de recharge électrique, parking à vélos, terminal de péage, défibrillateur, équipement de premiers secours, tuyau d'incendie, extincteur, bouche d'incendie, toute autre application spécifique  `firstAvailableFloor`: Numéro de l'étage le plus proche du sol qui dispose actuellement de places de parking disponibles. Valeurs autorisées : Les étages sont numérotés entre -n et n, soit 0 rez-de-chaussée.  `highestFloor`: Pour les sites de stationnement à plusieurs étages, l'étage le plus élevé. Un nombre entier. 0 est le niveau du sol. Les étages supérieurs sont des nombres positifs. Les étages inférieurs sont des nombres négatifs.  `id`:   `image`: Une URL contenant une photo de ce parking  `layout`: Aménagement du parking. Donne plus de détails sur l'attribut "catégorie". Valeurs autorisées : Selon le _ParkingLayoutEnum_ de DATEX II version 2.3 : (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`, `openSpace`, `covered`, `nested`, `field`, `rooftop`, `sheds`, `carports`, `garageBoxes`, `other`). Voir également [OpenStreetMap] (http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Ou toute autre valeur utile pour l'application et non couverte ci-dessus.  `location`:   `lowestFloor`: Pour les sites de stationnement à plusieurs étages, l'étage le plus bas. Valeurs autorisées : Un nombre entier.  `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules. S'il y a plusieurs zones, ce sera la hauteur minimale de toutes les zones.  `maximumAllowedWidth`: Largeur maximale autorisée pour les véhicules. S'il y a  
    zones multiples, elle sera la largeur minimale de toutes les zones.  `maximumParkingDuration`: Séjour maximum autorisé sur le site, sur une base générale, encodé comme une durée ISO8601 ou avec toute autre chaîne pertinente pour le stationnement.  Une valeur vide ou une absence indique une durée indéterminée  `measuresPeriod`: La durée des mesures était liée au nombre de points disponibles et au taux de prix par minute.  `measuresPeriodUnit`: L'unité de la période de mesures se rapportait au nombre de points disponibles et au taux de prix par minute.  `name`: Le nom de cet article.  `occupancy`:   `occupancyDetectionType`: Méthode(s) de détection d'occupation.  Valeurs autorisées : Les méthodes suivantes de DATEX II version 2.3 _OccupancyDetectionTypeEnum_ : `none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`, ou toute autre méthode spécifique à une application  `occupancyModified`: Valeur relative des places occupées sur le total des places. Valeurs autorisées : 0 - 1  `occupiedSpotNumber`: Nombre de places occupées. Valeurs autorisées : 0 - `totalSpotNumber` (nombre total de places)  `openingHours`: Heures d'ouverture du parking.  `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `parkingMode`: Mode(s) de stationnement. Valeurs autorisées : Celles définies par l'énumération _ParkingModeEnum_ de DATEX II version 2.3 : `perpendicularParking`, `parallelParking`, `echelonParking`.  `priceCurrency`: Monnaie de prix du tarif par minute  `priceRatePerMinute`: Prix par minute.  `provider`:   `refParkingAccess`: Point(s) d'accès au(x) site(s) de stationnement.  `refParkingGroup`: Relation. Site de stationnement identifié groupe(s). Un groupe peut correspondre à une zone, un étage complet, un groupe de places, etc.  `refParkingSpot`: Relation. Places de stationnement individuelles appartenant à ce site de stationnement hors rue.  `requiredPermit`: Cet attribut indique le ou les permis qui pourraient être nécessaires pour se garer sur ce site. La sémantique est qu'au moins _un de_ ces permis est nécessaire pour se garer. Lorsqu'un permis est composé de plusieurs éléments (et) ils peuvent être combinés avec un ",". Par exemple, "permis de séjour, permis pour handicapés" signifie qu'il faut à la fois un permis de séjour et un permis pour handicapés pour se garer. Si la liste est vide, aucun permis n'est nécessaire. Valeurs autorisées : Ce qui suit, défini par l'énumération _PermitTypeEnum_ de DATEX II version 2.3 (`permis d'employé`, `permis d'étudiant`, `permis équitable`, `permis du gouvernement`, `permis de résident`, `permis spécifique de véhicule identifié`, `permis de visiteur`, `pas besoin de permis`)ou toute autre application spécifique  `reservationType`: le suivant spécifié par _ReservationTypeEnum_ de DATEX II version 2.3 : (`optionnel`, `obligatoire`, `non disponible`, `partiellement`).  `security`: Les aspects de sécurité fournis par ce site de stationnement. Valeurs autorisées : Les éléments suivants, dont certains sont définis par le _ParkingSecurityEnum_ de DATEX II version 2.3 : (`patrolled`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences``areaSeperatedFromSurroundings`) ou tout autre élément spécifique à l'application  `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `specialLocation`: Si le parking se trouve à un endroit particulier (aéroport, grand magasin, etc.), il indique ce qu'est cet endroit particulier.  Valeurs autorisées : Celles définies par _ParkingSpecialLocationEnum_ de [DATEX II version 2.3](http://www.datex2.eu/contenu/parking-publications-extension-v10a) : (terminal d'aéroport, centre d'exposition, centre commercial, installation spécifique, gare, terrain de camping, parc à thème, terminal de ferry, terminal de véhicules sur rail, CoachStation, CableCarStation, PublicTransportStation, Market, ReligiousCentre, ConventionCentre, Cinéma, Skilift, Hôtel, Autres)  `status`: Statut du site de stationnement. Valeurs autorisées : Les valeurs suivantes sont définies par les énumérations suivantes définies par DATEX II version 2.3 :  
 - _ParkingSiteStatusEnum_ (statut du site de stationnement)  
 - Ouverture de l'Enumération de statut  
 - ("ouvert", "fermé", "fermé normal", "temps d'ouverture en vigueur", "plein",  
 Pleine entrée", "espaces disponibles", "presque pleine")  
 - Ou toute autre application spécifique  `totalSpotNumber`: Le nombre total de places offertes par ce site de stationnement.  Ce nombre peut être difficile à obtenir pour les emplacements de stationnement sur lesquels les places ne sont pas clairement indiquées par des lignes. Valeurs autorisées : Tout nombre entier positif ou 0. Références normatives : Attribut _parkingNumberOfSpaces_ de la classe _ParkingRecord_ de DATEX 2 version 2.3.  `type`: Il doit s'agir d'un stationnement hors rue  `usageScenario`: Scénario(s) d'utilisation. Donne plus de détails sur l'attribut "category". Valeurs autorisées : Celles définies par l'énumération _ParkingUsageScenarioEnum_ de DATEX II version 2.3 :(`truckParking`, `parkAndRide`, `parkAndCycle`, `parkAndWalk`, `kissAndRide`, `liftshare`, `carSharing`, `restArea`, `serviceArea`, `dropOffWithValet`, `dropOffMechanical`, `eventParking`, Guide automatique de stationnement, Guide du personnel pour l'espace, Ascenseur de véhicule, Baie de chargement, Dépôt, Stationnement de nuit, Autre, ou toute autre valeur utile pour l'application et non couverte ci-dessus.  `vehicleEntranceCount`: Nombre total de véhicules qui entrent sur le site de stationnement au cours d'une période donnée.  `vehicleExitCount`: Nombre total de véhicules qui quittent le parking au cours d'une période donnée.    
Un site, hors rue, destiné au stationnement des véhicules, géré de manière autonome et disposant de points d'accès (entrées et sorties) adaptés et clairement signalés. Si nécessaire, et à des fins de gestion ou pour traiter des sites de stationnement à emplacements multiples, il peut être divisé en différentes zones modélisées par le type d'entité [ParkingGroup](../ParkingGroup/README.md) . Dans la terminologie de DATEX 2 version 2.3, elle correspond à un _UrbanParkingSite_ de type _offStreetParking_. Un dictionnaire de données pour les termes de DATEX II peut être consulté à l'adresse suivante : [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Modèle de données description des biens  
Classement par ordre alphabétique  
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
Voici un exemple d'un OffStreetParking au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de parking hors rue au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'un OffStreetParking au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de parking hors rue au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
