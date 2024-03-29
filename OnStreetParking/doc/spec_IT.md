<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: OnStreetParking    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un sito, zona di spazio aperto, su strada, (con o senza contatore) con accesso diretto da una strada, destinato al parcheggio di veicoli.**    
versione: 0.1.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `acceptedPaymentMethod[string]`: Tipo di addebito effettuato dal sito di parcheggio. Enum:'Tramite bonifico bancario anticipato, Tramite fattura, Contanti, Assegno anticipato, Contrassegno, Addebito diretto, GoogleCheckout, PayPal, PaySwarm'.  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel Paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `allowedVehicleType[array]`: Tipo/i di veicolo/i consentito/i. Il primo elemento di questa matrice _DEVE_ essere il tipo di veicolo principale consentito. I seguenti valori sono definiti da _VehicleTypeEnum_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).. Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, truck, moped, motorcycle, motorcycleWithSideCar, motorscooter, autocisterna, veicolo a tre ruote, rimorchio, tram, veicolo a due ruote, furgone, veicolo con convertitore catalitico, veicolo senza convertitore catalitico, veicolo con roulotte, veicolo con rimorchio, con targa pari, con targa dispari, altro".  - `alternateName[string]`: Un nome alternativo per questa voce  - `areBordersMarked[boolean]`: Indica se i posti auto sono delimitati (con linee vuote o simili) o meno.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: Il numero di posti disponibili a livello globale, compresi gli spazi riservati, come quelli per i disabili, i parcheggiatori di lunga durata e così via. Questo potrebbe essere più difficile da stimare in quei parcheggi in cui i confini dei posti non sono chiaramente segnati da linee.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: La lunghezza media dei posti auto  . Model: [https://schema.org/length](https://schema.org/length)- `averageSpotWidth[number]`: La larghezza media dei posti auto  . Model: [https://schema.org/width](https://schema.org/width)- `category[array]`: Categoria di parcheggio stradale. Enum:'blueZone, a pagamento, perDisabili, perCarica Elettrica, perScarico, perResidenti, gratuito, greenZone, a media durata, solo con permesso, a breve durata, taxiStop'.  - `chargeType[array]`: Tipo di tariffe applicate dal parcheggio. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `extraSpotNumber[number]`: Il numero di posti extra disponibili, cioè liberi. I posti extra sono quelli riservati a scopi speciali e di solito richiedono un permesso. I dettagli del permesso si trovano a livello di gruppo di parcheggio (entità di tipo `ParkingGroup`). Questo valore deve aggregare i posti liberi di tutti i gruppi dedicati a condizioni di parcheggio speciali. Valori ammessi: Un numero intero positivo, incluso 0. `extraSpotNumber` più `availableSpotNumber` deve essere inferiore o uguale a `totalSpotNumber  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: Stato della disponibilità di posti auto per quattro ruote nel sito di parcheggio corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSlotNumber[number]`: Numero di posti auto disponibili per l'uso nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al totalSpotNumber.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSlotNumber[number]`: Numero di posti auto occupati nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al numero totale di posti auto.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `id[*]`: Identificatore univoco dell'entità  - `layout[array]`: Classificazione generica del layout del parcheggio  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maximumParkingDuration[date-time]`: Permanenza massima consentita nel sito, codificata come durata ISO8601. Un valore vuoto indica una durata indefinita  - `municipalityInfo[object]`: Informazioni sul comune corrispondenti a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: ID della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: Nome della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: Nome del distretto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Nome dello stato corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: Nome dell'Ente Locale Urbano corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: ID del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: Nome del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: Numero del reparto corrispondente a questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: ID della zona corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: Il nome di questo elemento  - `observationDateTime[date-time]`: Ultima ora di osservazione segnalata  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyDetectionType[array]`: Metodo di rilevamento dell'occupazione. Enum:'bilanciamento, manuale, basato su modello, nessuno, singleSpaceDetection'. Quanto segue da DATEX II versione 2.3 _OccupancyDetectionTypeEnum_  - `occupancyModified[date-time]`: Data dell'ultima modifica dell'occupazione del parcheggio  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `occupiedSpotNumber[number]`: Numero di posti auto totali occupati nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale a totalSpotNumber.  . Model: [https://schema.org/Number](https://schema.org/Number)- `outOfServiceSlotNumber[number]`: Il numero di rastrelliere/posti bici o di parcheggi che sono fuori servizio e che non possono essere utilizzati per noleggiare o parcheggiare una bicicletta nella stazione di parcheggio o nel sito di parcheggio corrispondente a questa osservazione.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `parkingMode[string]`: Modalità di parcheggio. Enum:'echelonParking, parallelParking, perpendicularParking'.  - `parkingSiteId[string]`: L'ID univoco del sito di parcheggio o del parcheggio corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)- `permitActiveHours[object]`: Questo attributo consente di rilevare situazioni in cui un permesso è necessario solo in determinati orari o giorni della settimana. È un valore strutturato che deve contenere una sottoproprietà per ogni permesso richiesto, che indica quando il permesso è attivo. Se non viene specificato nulla per un permesso, significa che il permesso è sempre richiesto. Un Oggetto JSON vuoto significa sempre attivo. La sintassi deve essere conforme a schema.org  - `refParkingGroup[array]`: Riferimento al/i gruppo/i di parcheggio (se presente/i) appartenente/i a questa zona di parcheggio su strada  - `refParkingSpot[array]`: Posti auto individuali appartenenti a questo parcheggio su strada  - `requiredPermit[array]`: Questo attributo indica quali permessi potrebbero essere necessari per parcheggiare in questo sito. La semantica è che almeno _uno_ di questi permessi è necessario per parcheggiare. Quando un permesso è composto da più elementi (e), questi possono essere combinati con un ','. Ad esempio, 'residentPermit,disabledPermit' indica che per parcheggiare sono necessari contemporaneamente un permesso per residenti e uno per disabili. Se l'elenco è vuoto, non è necessario alcun permesso  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `totalSpotNumber[number]`: Il numero totale di posti offerti da questo parcheggio. Questo numero può essere difficile da ottenere per quei parcheggi in cui i posti non sono chiaramente contrassegnati da linee. Riferimenti normativi: Attributo _parkingNumberOfSpaces_ della classe _ParkingRecord_ di DATEX 2 versione 2.3.  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: Stato della disponibilità di posti auto per due ruote nel sito di parcheggio corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: Numero di posti auto disponibili per l'uso nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al totalSpotNumber.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: Numero di posti auto occupati nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al numero totale di posti auto.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `type[string]`: Tipo di entità. Deve essere uguale a OnStreetParking  - `unclassifiedSlots[object]`: Veicoli non classificati o altri veicoli che parcheggiano nel sito di parcheggio corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: Numero di posti auto disponibili per l'uso nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al totalSpotNumber.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: Numero di posti auto occupati nel parcheggio intelligente corrispondente a questa osservazione. Deve essere un numero positivo inferiore o uguale al numero totale di posti auto.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `usageScenario[string]`: Tipo di tariffa/e effettuata/e dal sito di parcheggio. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Nella terminologia di DATEX 2 versione 2.3 corrisponde a un _UrbanParkingSite_ di tipo _onStreetParking_. Un dizionario di dati per i termini di DATEX II si trova in [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
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
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areBordersMarked:      
      description: Denotes whether parking spots are delimited (with blank lines or similar) or not      
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
      description: 'The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    averageSpotLength:      
      description: The average length of parking spots      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/length      
        type: Property      
    averageSpotWidth:      
      description: The average width of parking spots      
      minimum: 0      
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
    extraSpotNumber:      
      description: 'The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    fourWheelerSlots:      
      description: Four wheeler parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSlotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSlotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSlotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
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
    layout:      
      description: Generic classification of the layout of the parking      
      items:      
        type: string      
      type: array      
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
    maximumParkingDuration:      
      description: Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    municipalityInfo:      
      description: Municipality information corresponding to this observation      
      properties:      
        cityId:      
          description: City ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        cityName:      
          description: City name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        district:      
          description: District name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        stateName:      
          description: Name of the state corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        ulbName:      
          description: Name of the Urban Local Body corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardId:      
          description: Ward ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardName:      
          description: Ward name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardNum:      
          description: Ward number corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        zoneId:      
          description: Zone ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        zoneName:      
          description: Zone name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
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
      description: Date last time the occupancy of the parking has being modified      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    occupiedSpotNumber:      
      description: Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    outOfServiceSlotNumber:      
      description: The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
      description: 'Parking mode(s). Enum:''echelonParking, parallelParking, perpendicularParking'''      
      enum:      
        - echelonParking      
        - parallelParking      
        - perpendicularParking      
      type: string      
      x-ngsi:      
        type: Property      
    parkingSiteId:      
      description: The unique ID of the parking site or parking lot corresponding to this observation      
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
      description: Reference to the parking group(s) (if any) belonging to this onstreet parking zone      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Relationship      
    refParkingSpot:      
      description: Individual parking spots belonging to this on street parking site      
      items:      
        format: uri      
        type: string      
      type: array      
      x-ngsi:      
        type: Relationship      
    requiredPermit:      
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed'      
      items:      
        type: string      
      type: array      
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
      description: 'The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    twoWheelerSlots:      
      description: Two wheeler parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSpotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSpotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSpotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: Entity type. It must be equal to OnStreetParking      
      enum:      
        - OnStreetParking      
      type: string      
      x-ngsi:      
        type: Property      
    unclassifiedSlots:      
      description: Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSpotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSpotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSpotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
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
  x-version: 0.1.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### OnStreetParking NGSI-v2 valori chiave Esempio    
Ecco un esempio di OnStreetParking in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "observationDateTime": "2021-03-11T15:51:02Z",  
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
</details>    
#### OnStreetParking NGSI-v2 normalizzato Esempio    
Ecco un esempio di OnStreetParking in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "permitActiveHours": {  
    "type": "StructuredValue",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "type": "StructuredValue",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "StructuredValue",  
    "value": [  
      "car"  
    ]  
  },  
  "chargeType": {  
    "type": "StructuredValue",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "refParkingGroup": {  
    "type": "StructuredValue",  
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
    "value": "2021-03-11T15:51:02Z"  
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
</details>    
#### OnStreetParking Valori-chiave NGSI-LD Esempio    
Ecco un esempio di OnStreetParking in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "observationDateTime": "2021-03-11T15:51:02Z",  
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
</details>    
#### OnStreetParking NGSI-LD normalizzato Esempio    
Ecco un esempio di OnStreetParking in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
