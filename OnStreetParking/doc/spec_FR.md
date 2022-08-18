[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : OnStreetParking  
========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Un emplacement, une zone d'espace libre, sur rue, (avec compteur ou non) avec accès direct depuis une route, destiné au stationnement des véhicules.**.  
version : 0.1.1  

## Liste des propriétés  

- `acceptedPaymentMethod`: Type de prélèvement(s) effectué(s) par le site de stationnement. Enum : "ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm  - `address`: L'adresse postale  - `allowedVehicleType`: Type de véhicule autorisé. Enum :'véhicule agricole, tout véhicule, véhicule articulé, bicyclette, autobus, voiture, caravane, voiture ou véhicule léger, voiture avec caravane, voiture avec remorque, véhicule de construction ou d'entretien, quatre roues motrices, véhicule à flancs hauts, camion, cyclomoteur, motocyclette, motocyclette avec side-car, scooter des mers, camion-citerne, véhicule à trois roues, remorque, tramway, véhicule à deux roues, camionnette, véhicule avec convertisseur catalytique, véhicule sans convertisseur catalytique, véhicule avec caravane, véhicule avec remorque, avec plaques d'immatriculation paires, avec plaques d'immatriculation supplémentaires, autres".  - `alternateName`: Un nom alternatif pour cet élément  - `areBordersMarked`: Indique si les places de stationnement sont délimitées (par des lignes blanches ou autres) ou non.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableSpotNumber`: Le nombre de places disponibles dans l'ensemble, y compris les places réservées, telles que celles destinées aux personnes handicapées, aux personnes stationnant depuis longtemps, etc. Cela peut être plus difficile à estimer sur les emplacements de stationnement où les limites des places ne sont pas clairement marquées par des lignes.  - `averageSpotLength`: La durée moyenne des places de stationnement  - `averageSpotWidth`: La largeur moyenne des places de stationnement  - `category`: Catégorie de stationnement dans la rue. Enum : "blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop".  - `chargeType`: Type de redevance(s) appliquée(s) par le site de stationnement. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `extraSpotNumber`: Le nombre de places supplémentaires disponibles, c'est-à-dire libres. Les places supplémentaires sont celles qui sont réservées à des fins spéciales et nécessitent généralement un permis. Les détails du permis se trouvent au niveau du groupe de stationnement (entité de type `ParkingGroup`). Cette valeur doit regrouper les places libres de tous les groupes consacrés à des conditions de stationnement particulières. Valeurs autorisées : Un nombre entier positif, y compris 0. La somme de `extraSpotNumber` et de `availableSpotNumber` doit être inférieure ou égale à `totalSpotNumber`.  - `fourWheelerSlots`: L'état de disponibilité des places de stationnement pour les véhicules à quatre roues sur le site de stationnement correspond à cette observation.  - `id`: Identifiant unique de l'entité  - `layout`: Classification générique de l'aménagement du parking  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maximumParkingDuration`: Séjour maximal autorisé sur le site, encodé comme une durée ISO8601. Une valeur vide indique une durée indéterminée.  - `municipalityInfo`: Informations sur la municipalité correspondant à cette observation.  - `name`: Le nom de cet élément.  - `observationDateTime`: Dernière heure d'observation signalée.  - `occupancyDetectionType`: Méthode(s) de détection d'occupation. Enum : "équilibrage, manuel, modelBased, none, singleSpaceDetection". Ce qui suit est extrait de DATEX II version 2.3 _OccupancyDetectionTypeEnum_.  - `occupancyModified`: Date à laquelle l'occupation du parking a été modifiée pour la dernière fois.  - `occupiedSpotNumber`: Nombre total de places de stationnement occupées dans le site de stationnement intelligent correspondant à cette observation. Il doit s'agir d'un nombre positif inférieur ou égal au totalSpotNumber.  - `outOfServiceSlotNumber`: Le nombre de supports à vélos ou d'emplacements de stationnement qui sont hors d'usage et ne peuvent être utilisés pour louer ou garer un vélo dans la station d'accueil ou le site de stationnement correspondant à cette observation.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `parkingMode`: Mode(s) de stationnement. Enum : 'echelonParking, parallelParking, perpendicularParking' (en anglais)  - `parkingSiteId`: L'identifiant unique du site ou du parc de stationnement correspondant à cette observation.  - `permitActiveHours`: Cet attribut permet de saisir les situations dans lesquelles un permis n'est nécessaire qu'à certaines heures ou certains jours de la semaine. Il s'agit d'une valeur structurée qui doit contenir une sous-propriété pour chaque permis requis, indiquant quand le permis est actif. Si rien n'est spécifié pour un permis, cela signifie qu'un permis est toujours nécessaire. Un objet JSON vide signifie qu'il est toujours actif. La syntaxe doit être conforme à schema.org.  - `refParkingGroup`: Référence au(x) groupe(s) de stationnement (le cas échéant) appartenant à cette zone de stationnement sur voirie.  - `refParkingSpot`: Des places de stationnement individuelles appartenant à ce site de stationnement sur rue.  - `requiredPermit`: Cet attribut indique le ou les permis qui peuvent être nécessaires pour se garer sur ce site. La sémantique est qu'au moins _un_ de ces permis est nécessaire pour se garer. Lorsqu'un permis est composé de plus d'un élément (et), il peut être combiné avec un ",". Par exemple, 'residentPermit,disabledPermit' signifie qu'il faut à la fois un permis de résident et un permis d'invalide pour stationner. Si la liste est vide, aucun permis n'est nécessaire.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `totalSpotNumber`: Le nombre total de places offertes par ce site de stationnement. Ce nombre peut être difficile à obtenir pour les emplacements de stationnement sur lesquels les places ne sont pas clairement marquées par des lignes. Références normatives : DATEX 2 version 2.3 attribut _parkingNumberOfSpaces_ de la classe _ParkingRecord_.  - `twoWheelerSlots`: L'état de disponibilité des places de stationnement pour les deux roues sur le site de stationnement correspond à cette observation.  - `type`: Type d'entité. Il doit être égal à OnStreetParking.  - `unclassifiedSlots`: Statut de disponibilité des places de stationnement des véhicules non classés ou d'autres véhicules dans le site de stationnement correspondant à cette observation.  - `usageScenario`: Type de charge(s) effectuée(s) par le site de stationnement. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'    
Propriétés requises  
- `id`  - `location`  - `type`    
Dans la terminologie DATEX 2 version 2.3, il correspond à un _UrbanParkingSite_ de type _onStreetParking_. Vous trouverez un dictionnaire de données pour les termes DATEX II à l'adresse [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OnStreetParking:    
  description: 'A site, open space zone, on street, (metered or not) with direct access from a road, intended to park vehicles.'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Type of charge(s) performed by the parking site. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'''    
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
      x-ngsi:    
        type: Property    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).. Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, van, vehicleWithCatalyticConverter, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'''    
      items:    
        enum:    
          - agriculturalVehicle    
          - anyVehicle    
          - articulatedVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carOrLightVehicle    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - fourWheelDrive    
          - highSidedVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - threeWheeledVehicle    
          - trailer    
          - tram    
          - twoWheeledVehicle    
          - van    
          - vehicleWithCatalyticConverter    
          - vehicleWithoutCatalyticConverter    
          - vehicleWithCaravan    
          - vehicleWithTrailer    
          - withEvenNumberedRegistrationPlates    
          - withOddNumberedRegistrationPlates    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines'    
      minvalue: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots'    
      minvalue: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
    averageSpotWidth:    
      description: 'The average width of parking spots'    
      minvalue: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
    category:    
      description: 'Street parking category. Enum:''blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'''    
      items:    
        enum:    
          - barrierAccess    
          - blueZone    
          - feeCharged    
          - forDisabled    
          - forElectricalCharging    
          - forLoadUnload    
          - forResidents    
          - free    
          - greenZone    
          - mediumTerm    
          - onlyWithPermit    
          - public    
          - shortTerm    
          - taxiStop    
          - underground    
        type: string    
      type: array    
      x-ngsi:    
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
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    extraSpotNumber:    
      description: 'The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber'    
      minvalue: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    fourWheelerSlots:    
      description: 'Four wheeler parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &onstreetparking_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    layout:    
      description: 'Generic classification of the layout of the parking'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward ID corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s). Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_'    
      items:    
        enum:    
          - balancing    
          - manual    
          - modelBased    
          - none    
          - singleSpaceDetection    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    occupancyModified:    
      description: 'Date last time the occupancy of the parking has being modified'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    occupiedSpotNumber:    
      description: 'Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    outOfServiceSlotNumber:    
      description: 'The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *onstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parkingMode:    
      description: 'Parking mode(s). Enum:''echelonParking, parallelParking, perpendicularParking'''    
      enum:    
        - echelonParking    
        - parallelParking    
        - perpendicularParking    
      type: string    
      x-ngsi:    
        type: Property    
    parkingSiteId:    
      description: 'The unique ID of the parking site or parking lot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    permitActiveHours:    
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is a structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. An empty JSON Object means always active. The syntax must be conformant with schema.org'    
      type: object    
      x-ngsi:    
        type: Property    
    refParkingGroup:    
      description: 'Reference to the parking group(s) (if any) belonging to this onstreet parking zone.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    refParkingSpot:    
      description: 'Individual parking spots belonging to this on street parking site.'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalSpotNumber:    
      description: 'The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minvalue: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    twoWheelerSlots:    
      description: 'Two wheeler parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'Entity type. It must be equal to OnStreetParking'    
      enum:    
        - OnStreetParking    
      type: string    
      x-ngsi:    
        type: Property    
    unclassifiedSlots:    
      description: 'Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    usageScenario:    
      description: 'Type of charge(s) performed by the parking site. Enum:''carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'''    
      enum:    
        - carSharing    
        - dropOff    
        - kissAndRide    
        - liftShare    
        - loadingBay    
        - overnightParking    
        - parkAndRide    
        - parkAndCycle    
        - parkAndWalk    
        - vehicleLift    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OnStreetParking/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OnStreetParking/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.2    
```  
</details>    
## Exemples de charges utiles  
#### OnStreetParking NGSI-v2 key-values Exemple  
Voici un exemple d'un OnStreetParking au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "allowedVehicleType": [  
    "car"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "requiredPermit": [  
    "blueZonePermit",  
    "disabledPermit"  
  ],  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "maximumParkingDuration": "PT2H",  
  "availableSpotNumber": 3,  
  "occupiedSpotNumber": 3,  
  "totalSpotNumber": 6,  
  "extraSpotNumber": 2,  
  "dateModified": "2016-06-02T09:25:55.00Z",  
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
  "areaServed": "Zona Centro",  
  "refParkingGroup": [  
    "daoiz-velarde-1-5-main",  
    "daoiz-velarde-1-5-disabled"  
  ],  
  "outOfServiceSlotNumber": 0,  
  "parkingSiteId": "P2",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "fourWheelerSlots": {  
    "availableSpotNumber": 25,  
    "totalSpotNumber": 25,  
    "occupiedSpotNumber": 0  
  },  
  "unclassifiedSlots": {  
    "availableSpotNumber": 0,  
    "totalSpotNumber": 0,  
    "occupiedSpotNumber": 0  
  },  
  "twoWheelerSlots": {  
    "availableSpotNumber": 20,  
    "totalSpotNumber": 20,  
    "occupiedSpotNumber": 0  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
#### OnStreetParking NGSI-v2 normalisé Exemple  
Voici un exemple d'un OnStreetParking au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "type": "array",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "permitActiveHours": {  
    "type": "array",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "type": "array",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "Text",  
    "value": [  
      "car"  
    ]  
  },  
  "chargeType": {  
    "type": "array",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
    "value": [  
      "daoiz-velarde-1-5-main",  
      "daoiz-velarde-1-5-disabled"  
    ]  
  },  
  "totalSpotNumber": {  
    "type": "Number",  
    "value": 6  
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
  "areaServed": {  
    "type": "Text",  
    "value": "Zona Centro"  
  },  
  "maximumAllowedStay": {  
    "type": "Text",  
    "value": "PT2H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-02T09:25:55.00Z"  
  },  
  "extraSpotNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "availableSpotNumber": {  
    "type": "Number",  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  },  
  "occupiedSpotNumber": {  
    "type": "Number",  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "fourWheelerSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 25,  
      "totalSpotNumber": 25,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "unclassifiedSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 0,  
      "totalSpotNumber": 0,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "twoWheelerSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 20,  
      "totalSpotNumber": 20,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
#### OnStreetParking Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un OnStreetParking au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "allowedVehicleType": [  
    "car"  
  ],  
  "areaServed": "Zona Centro",  
  "availableSpotNumber": 3,  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "extraSpotNumber": 2,  
  "fourWheelerSlots": {  
    "availableSpotNumber": 25,  
    "totalSpotNumber": 25,  
    "occupiedSpotNumber": 0  
  },  
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
  "maximumAllowedStay": "PT2H",  
  "modifiedAt": "2016-06-02T09:25:55.00Z",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "occupiedSpotNumber": 3,  
  "parkingSiteId": "P2",  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "refParkingGroup": [  
    "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
    "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
  ],  
  "requiredPermit": [  
    "blueZonePermit",  
    "disabledPermit"  
  ],  
  "totalSpotNumber": 6,  
  "twoWheelerSlots": {  
    "availableSpotNumber": 20,  
    "totalSpotNumber": 20,  
    "occupiedSpotNumber": 0  
  },  
  "unclassifiedSlots": {  
    "availableSpotNumber": 0,  
    "totalSpotNumber": 0,  
    "occupiedSpotNumber": 0  
  },  
  "@context": [  
    "iudx:SmartParking",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
  ]  
}  
```  
#### OnStreetParking NGSI-LD normalisé Exemple  
Voici un exemple d'un OnStreetParking au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": [  
      "car"  
    ]  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Zona Centro"  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 3,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "chargeType": {  
    "type": "Property",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "extraSpotNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "location": {  
    "type": "Geoproperty",  
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
  "maximumAllowedStay": {  
    "type": "Property",  
    "value": "PT2H"  
  },  
  "occupiedSpotNumber": {  
    "type": "Property",  
    "value": 3,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "permitActiveHours": {  
    "type": "Property",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
      "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
    ]  
  },  
  "requiredPermit": {  
    "type": "Property",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "totalSpotNumber": {  
    "type": "Property",  
    "value": 6  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
