Entità: OffStreetParking  
========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Parcheggio fuori strada**  

## Elenco delle proprietà  

- `acceptedPaymentMethod`: Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'. Metodi di pagamento accettati.  - `accessModified`: Timestamp quando `vehicleEntranceCount` e `vehicleExitCount` sono stati aggiornati. Valori consentiti: ISO8601  - `address`: L'indirizzo postale  - `aggregateRating`: Valutazione aggregata per questo sito di parcheggio.  - `allowedVehicleType`:  Tipo(i) di veicolo consentito(i). Il primo elemento di questo array _DOVREBBE_ essere il principale tipo di veicolo permesso. I numeri di posto libero di altri tipi di veicolo permessi possono essere riportati sotto l'attributo `extraSpotNumber` e attraverso entità specifiche di tipo _ParkingGroup_. I seguenti valori definiti da _VehicleTypeEnum_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `availableSpotNumber`: Il numero di posti disponibili (_inclusi_ tutti i tipi di veicoli o gli spazi riservati, come quelli per i disabili, i parcheggiatori di lunga durata e così via). Questo potrebbe essere più difficile da stimare in quei parcheggi in cui i confini dei posti non sono chiaramente segnati da linee. Valori consentiti: Un numero intero positivo, incluso 0. Deve essere inferiore o uguale a `totalSpotNumber`.  - `averageSpotLength`: La lunghezza media dei parcheggi.  - `averageSpotWidth`: La larghezza media dei posti auto.  - `category`: Categoria(i) del sito di parcheggio. Lo scopo di questo campo è di permettere di etichettare, in generale, le entità di parcheggio fuori strada  - `chargeType`: Tipo(i) di carica eseguita dal sito di parcheggio. Valori consentiti: Alcuni di quelli definiti dall'enumerazione DATEX II versione 2.3 _ ChargeTypeEnum_. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'. O qualsiasi altra applicazione specifica  - `contactPoint`: Punto di contatto del sito di parcheggio.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `extCategory`: Categoria esterna per completare la categoria.  - `extraSpotNumber`: Il numero di posti extra _disponibili_, cioè liberi. Questo valore deve aggregare i posti liberi di tutti i gruppi menzionati qui sotto: A/ Quelli riservati per scopi speciali e che di solito richiedono un permesso. I dettagli del permesso si trovano a livello di gruppo di parcheggio (entità di tipo `ParkingGroup`). B/ Quelli riservati ad altri tipi di veicoli diversi dal tipo di veicolo principale consentito. C/ Qualsiasi altro gruppo di posti auto non soggetto alle regole di condizione generale trasmesse da questa entità.  - `facilities`: Valori consentiti: I seguenti definiti dall'enumerazione _EquipmentTypeEnum_ di DATEX II versione 2.3. Enum:'bikeParking, cashMachine, copyMachineOrService, defibrillatore, dumpingStation, electricChargingStation, ascensore, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, iceFreeScaffold, informationPoint, internetWireless, luggageLocker, payDesk, paymentMachine, playground, publicPhone, refuseBin, safeDeposit, shower, toilet, tollTerminal, vendingMachine, wasteDisposition' . Qualsiasi altra applicazione specifica  - `firstAvailableFloor`: Numero del piano più vicino al suolo che ha attualmente posti auto disponibili. Valori consentiti: Le storie sono numerate tra -n e n, essendo 0 il piano terra.  - `highestFloor`: Per i siti di parcheggio con più livelli di piano, il piano più alto. Un numero intero. 0 è il livello del suolo. I piani superiori sono numeri positivi. I piani inferiori sono numeri negativi.  - `id`: Identificatore unico dell'entità  - `images`: Un URL contenente una foto di questo parcheggio  - `layout`: Layout del parcheggio. Dà più dettagli all'attributo `categoria`. Valori consentiti: Come per il _ParkingLayoutEnum_ di DATEX II versione 2.3. Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'. Vedi anche [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). O qualsiasi altro valore utile per l'applicazione e non coperto sopra.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `lowestFloor`: Per i siti di parcheggio con più livelli di piano, il piano più basso. Valori consentiti: Un numero intero.  - `maximumAllowedHeight`: Altezza massima consentita per i veicoli. Se ci sono più zone, sarà l'altezza minima di tutte le zone.  - `maximumAllowedWidth`: Larghezza massima consentita per i veicoli. Se ci sono più zone, sarà la larghezza minima di tutte le zone.  - `maximumParkingDuration`: Permanenza massima consentita nel sito, su base generale, codificata come durata ISO8601 o con qualsiasi altra stringa pertinente per il parcheggio.  Un valore vuoto o non presente indica una durata indefinita  - `measuresPeriod`: Il periodo delle misure relative a availableSpotNumber e priceRatePerMinute.  - `measuresPeriodUnit`: L'unità di misura del periodo relativa a availableSpotNumber e PriceRatePerMinute.  - `name`: Il nome di questo articolo.  - `occupancy`: Valore relativo dei posti occupati sul totale dei posti.  - `occupancyDetectionType`: Metodo(i) di rilevamento dell'occupazione.  Valori consentiti: I seguenti da DATEX II versione 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. O qualsiasi altra applicazione specifica  - `occupancyModified`: Valore relativo degli spot occupati rispetto agli spot totali. Valori consentiti: 0 - 1  - `occupiedSpotNumber`: Numero di posti occupati. Valori consentiti: 0 - `totalSpotNumber`.  - `openingHours`: Orari di apertura del parcheggio.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `parkingMode`: Modalità di parcheggio. Valori consentiti: Quelli definiti dall'enumerazione _ParkingModeEnum_ di DATEX II versione 2.3. Enum:'echelonParking, parallelParking, perpendicularParking'.  - `priceCurrency`: Prezzo valuta del tasso di prezzo al minuto  - `priceRatePerMinute`: Prezzo al minuto.  - `provider`: Fornitore di servizi di parcheggio  - `refParkingAccess`: Punto/i di accesso al parcheggio.  - `refParkingGroup`: Gruppo(i) identificato(i) del sito di parcheggio. Un gruppo può corrispondere a una zona, un piano completo, un gruppo di posti, ecc.  - `refParkingSpot`: Posti auto individuali appartenenti a questo parcheggio offStreet.  - `requiredPermit`: Questo attributo cattura quali permessi potrebbero essere necessari per parcheggiare in questo sito. La semantica è che almeno _uno_ di questi permessi è necessario per parcheggiare. Quando un permesso è composto da più di un elemento (e) possono essere combinati con un ','. Per esempio 'residentPermit,disabledPermit' significa che sia un permesso per residenti che uno per disabili sono necessari per parcheggiare. Se l'elenco è vuoto non è necessario alcun permesso. Valori consentiti: I seguenti, definiti dall'enumerazione _PermitTypeEnum_ di DATEX II versione 2.3. Enum:'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'. O qualsiasi altra applicazione specifica  - `reservationType`: l seguente specificato da _ReservationTypeEnum_ di DATEX II versione 2.3. Enum:'obbligatorio, non disponibile, opzionale, parzialmente'.  - `security`: Aspetti di sicurezza forniti da questo sito di parcheggio. Valori consentiti: I seguenti, alcuni dei quali definiti da _ParkingSecurityEnum_ di DATEX II versione 2.3. Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' . o qualsiasi altra applicazione specifica  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `specialLocation`: Se il sito di parcheggio si trova in un luogo speciale (aeroporto, grande magazzino, ecc.) comunica qual è tale luogo speciale.  Valori consentiti: Quelli definiti da _ParkingSpecialLocationEnum_ di [DATEX II versione 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'  - `status`: Stato del sito di parcheggio. Valori consentiti: I seguenti definiti dalle seguenti enumerazioni definite da DATEX II versione 2.3. Enum:'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'. O qualsiasi altra applicazione specifica  - `totalSpotNumber`: Il numero totale di posti offerti da questo sito di parcheggio.  Questo numero può essere difficile da ottenere per quei parcheggi in cui i posti non sono chiaramente contrassegnati da linee. Valori consentiti: Qualsiasi numero intero positivo o 0. Riferimenti normativi: DATEX 2 versione 2.3 attributo _parkingNumberOfSpaces_ della classe _ParkingRecord_.  - `type`: Deve essere OffStreetParking  - `usageScenario`: Scenario(i) d'uso. Dà più dettagli all'attributo `categoria`. Valori consentiti: Quelli definiti dall'enumerazione _ParkingUsageScenarioEnum_ di DATEX II versione 2.3. Enum:'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'. O qualsiasi altro valore utile per l'applicazione e non coperto sopra.  - `vehicleEntranceCount`: Numero aggregato di veicoli che entrano nel sito di parcheggio in un periodo di tempo.  - `vehicleExitCount`: Numero aggregato di veicoli che lasciano il sito di parcheggio in un periodo di tempo.    
Proprietà richieste  
- `id`  - `location`  - `type`    
Un sito, fuori strada, destinato al parcheggio di veicoli, gestito autonomamente e con punti di accesso (entrate e uscite) adeguati e chiaramente segnalati. Se necessario, e per scopi di gestione o per trattare siti di parcheggio multi-locali, può essere diviso in diverse zone modellate dal tipo di entità [ParkingGroup](../ParkingGroup/README.md) . Nella terminologia di DATEX 2 versione 2.3 corrisponde ad un _UrbanParkingSite_ di tipo _offStreetParking_. Un dizionario di dati per i termini DATEX II può essere trovato in [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/acceptedPaymentMethod    
        type: Property    
    accessModified:    
      description: 'Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    aggregateRating:    
      description: 'Aggregated rating for this parking site.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: 'Parking site contact point.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
    extCategory:    
      description: 'External category to complement category.'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: ""    
        type: Property    
    firstAvailableFloor:    
      description: 'Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    highestFloor:    
      description: 'For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    images:    
      description: 'A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/image    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    measuresPeriod:    
      description: 'The measures period related to availableSpotNumber and priceRatePerMinute.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    measuresPeriodUnit:    
      description: 'The measures period unit related to availableSpotNumber and PriceRatePerMinute.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/unitText    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: 'Relative value of occupied spots out of the total spots.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    occupancyModified:    
      description: 'Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    occupiedSpotNumber:    
      description: 'Number of spots occupied. Allowed values: 0 - `totalSpotNumber`'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: 'Opening hours of the parking site.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    priceCurrency:    
      description: 'Price currency of price rate per minute'    
      type: string    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
        type: Property    
    priceRatePerMinute:    
      description: 'Price rate per minute.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    provider:    
      description: 'Parking site service provider'    
      type: object    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
    refParkingAccess:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site''s access point(s).'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refParkingGroup:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Individual parking spots belonging to this offStreet parking site.'    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    totalSpotNumber:    
      description: 'The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    type:    
      description: 'It has to be OffStreetParking'    
      enum:    
        - OffStreetParking    
      type: string    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    vehicleEntranceCount:    
      description: 'Aggregated number of vehicle that enter the parking site in a period of time.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    vehicleExitCount:    
      description: 'Aggregated number of vehicle that leave the parking site in a period of time.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OffStreetParking/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OffStreetParking/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### OffStreetParking NGSI-v2 valori chiave Esempio  
Ecco un esempio di un OffStreetParking in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### OffStreetParking NGSI-v2 normalizzato Esempio  
Ecco un esempio di un OffStreetParking in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### OffStreetParking NGSI-LD valori chiave Esempio  
Ecco un esempio di un OffStreetParking in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### OffStreetParking NGSI-LD normalizzato Esempio  
Ecco un esempio di un OffStreetParking in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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

Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza