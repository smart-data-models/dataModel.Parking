<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: ParcheggioGruppo    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Gruppo parcheggio **    
versione: 0.1.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `allowedVehicleType[string]`: Tipo di veicolo consentito (un gruppo di parcheggio consente un solo tipo di veicolo). Enum:'bicicletta, autobus, auto, caravan, moto, motoscooter, camion'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: Un nome alternativo per questa voce  - `areBordersMarked[boolean]`: Indica se i posti auto sono delimitati (con linee vuote o simili) o meno. Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: Il numero di posti disponibili in questo gruppo. Deve essere inferiore o uguale a `totalSpotNumber`.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: La lunghezza media dei posti auto. Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: Larghezza media dei posti auto. Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: Categoria del gruppo di parcheggio. Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `chargeType[array]`: Tipo di tariffe applicate dal parcheggio. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maximumAllowedHeight[number]`: Altezza massima consentita per i veicoli.  Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: Larghezza massima consentita per i veicoli. Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[date-time]`: Soggiorno massimo consentito, codificato come durata ISO8601. Quando non è presente o è uguale alla stringa vuota, significa indefinito. Le applicazioni _DOVREBBERO_ ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  - `name[string]`: Il nome di questo elemento  - `occupancyDetectionType[array]`: Valori ammessi: I seguenti da DATEX II versione 2.3 _OccupancyDetectionTypeEnum_. Enum:'bilanciamento, manuale, modelBased, nessuno, singleSpaceDetection'. O qualsiasi altro valore specifico dell'applicazione  . Model: [http://schema.org/Text](http://schema.org/Text)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `parkingMode[array]`: Modalità di parcheggio. Le applicazioni DEVONO ispezionare il valore di questa proprietà a livello di genitore, se non è definita. Valori ammessi: Quelli definiti dall'enumerazione DATEX II versione 2.3 _ParkingModeEnum_. Enum:'echelonParking, parallelParking, perpendicularParking'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `permitActiveHours[object]`: Questo attributo consente di cogliere situazioni in cui un permesso è necessario solo in determinati orari o giorni della settimana. È un valore strutturato che deve contenere una sottoproprietà per ogni permesso richiesto, che indica quando il permesso è attivo. Se non viene specificato nulla per un permesso, significa che il permesso è sempre richiesto. Un oggetto vuoto significa sempre attivo. La sintassi deve essere conforme a schema.org [specifica degli orari di apertura] (https://schema.org/openingHours). Ad esempio, una zona blu attiva solo nei giorni feriali sarà codificata come "blueZonePermit": "Mo,Tu,We,Th,Fr,Sa 09:00-20:00". Le applicazioni DEVONO ispezionare il valore di questa proprietà a livello di genitore, se non è definita.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `refParkingSite[*]`: Sito di parcheggio a cui appartiene questa zona. Un gruppo non può essere orfano. Un gruppo non può avere sottogruppi. Riferimento a un Parcheggio fuori strada o a un Parcheggio su strada  - `refParkingSpot[*]`: I singoli posti auto appartenenti a questo gruppo di parcheggi  - `requiredPermit[array]`: Questo attributo indica quali permessi potrebbero essere necessari per parcheggiare in questo sito. La semantica è che almeno _uno_ di questi permessi è necessario per parcheggiare. Quando un permesso è composto da più elementi (e), questi possono essere combinati con un ','. Ad esempio, 'residentPermit,disabledPermit' indica che per parcheggiare sono necessari contemporaneamente un permesso per residenti e uno per disabili. Se l'elenco è vuoto, non è necessario alcun permesso  . Model: [http://schema.org/Text](http://schema.org/Text)- `reservationType[string]`: Condizioni per la prenotazione. Le applicazioni DEVONO ispezionare il valore di questa proprietà a livello di genitore, se non è definita. Enum:'obbligatorio, non disponibile, facoltativo, parzialmente'.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `totalSpotNumber[number]`: Il numero totale di spot appartenenti a questo gruppo. Valori ammessi: Qualsiasi numero intero positivo o 0. Riferimenti normativi: Attributo _parkingNumberOfSpaces_ della classe _ParkingRecord_ di DATEX 2 versione 2.3.  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere ParkingGroup  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `refParkingSite`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Un gruppo di posti auto. Il livello di granularità può variare. Può trattarsi di un piano di un garage, di una zona specifica di un grande parcheggio o semplicemente di un gruppo di posti destinati al parcheggio di un certo tipo di veicolo o soggetti a determinate restrizioni (disabili, residenti, ...). Per semplicità, è consentito un solo tipo di veicolo per gruppo di parcheggio. Allo stesso modo, è consentito un solo permesso per ogni tipo di gruppo.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### Gruppo di parcheggio NGSI-v2 valori chiave Esempio    
Ecco un esempio di ParkingGroup in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### ParkingGroup NGSI-v2 normalizzato Esempio    
Ecco un esempio di ParkingGroup in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### Gruppo di parcheggio Valori chiave NGSI-LD Esempio    
Ecco un esempio di ParkingGroup in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### ParkingGroup NGSI-LD normalizzato Esempio    
Ecco un esempio di ParkingGroup in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
