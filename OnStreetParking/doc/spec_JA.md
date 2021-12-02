エンティティOnStreetParking  
=====================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**道路から直接アクセスできる、車を駐車することを目的とした敷地、オープンスペースゾーン、路上（従量制または非従量制） **。  

## プロパティのリスト  

- `acceptedPaymentMethod`: パーキングサイトが行う課金の種類。Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'.  - `address`: 郵送先住所  - `allowedVehicleType`: 許可された車両タイプ（路上駐車1台につき1つのみ）。Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter,タンクローリー、三輪自動車、トレーラー、路面電車、二輪自動車、バン、触媒コンバーター付き車両、触媒コンバーターなし車両、キャラバン付き車両、トレーラー付き車両、偶数番号登録プレート付き、追加番号登録プレート付き、その他'  - `alternateName`: このアイテムの別称  - `areBordersMarked`: 駐車場の区切り（空白の線など）の有無を表す  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `availableSpotNumber`: 障がい者用、長期駐車者用などの予約スペースを含む、世界の駐車場の数。これは、駐車場の境界が線で明確に示されていない場所では、推定が難しいかもしれません。  - `averageSpotLength`: 駐車場の平均長さ  - `averageSpotWidth`: 駐車場の平均的な幅  - `category`: 路上駐車のカテゴリー。Enum:'blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'.  - `chargeType`: 駐車場で行われる料金の種類。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'.  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `extraSpotNumber`: 利用可能なエクストラスポットの数、つまり無料です。追加スポットは特別な目的のために予約されたもので、通常は許可証が必要です。許可証の詳細はパーキンググループレベル（`ParkingGroup`タイプのエンティティ）で確認できます。この値は、特別な駐車条件のためのすべてのグループからの無料スポットを集約しなければならない。許可された値。extraSpotNumber` と `availableSpotNumber` を足した値は `totalSpotNumber` 以下でなければなりません。  - `id`: エンティティのユニークな識別子  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `maximumParkingDuration`: ISO8601の期間としてエンコードされたサイトでの最大許容滞在時間。空の値は無期限であることを示す。  - `name`: このアイテムの名前です。  - `occupancyDetectionType`: オキュパンシー検出方法。Enum:'balancing, manual, modelBased, none, singleSpaceDetection'.以下、DATEX IIバージョン2.3の_OccupancyDetectionTypeEnum_より。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `parkingMode`: パーキングモード（複数可）。Enum:'echelonParking, parallelParking, perpendicularParking' (エシュロンパーキング、パラレルパーキング、パーペンディキュラーパーキング)  - `permitActiveHours`: この属性により、許可証が特定の時間帯や曜日にのみ必要とされる状況を把握することができます。  これは構造化された値で、必要とされる各許可証ごとに、その許可証がいつ有効かを示すサブプロパティを含まなければなりません。パーミットに何も指定されていない場合は、常にパーミットが必要であることを意味します。空のJSONオブジェクトは、常にアクティブであることを意味します。構文は、schema.orgに準拠していなければなりません。  - `refParkingGroup`: この路上駐車ゾーンに属する駐車グループ（複数ある場合）を示す。  - `refParkingSpot`: この路上駐車場には、個々の駐車場が属しています。  - `requiredPermit`: この属性は、このサイトに駐車するためにどのような許可証が必要であるかを示す。意味としては、これらの許可証のうち少なくとも_1つが駐車に必要であるということです。許可証が複数の項目（and）で構成されている場合、それらは「,」で結合することができます。例えば、'residentPermit,disabledPermit'は、居住者と障害者の両方の許可証が同時に駐車に必要であることを示します。リストが空であれば、許可証は必要ありません。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalSpotNumber`: この駐車場で提供されているスポットの総数です。この数は、スポットが線で明確に示されていない駐車場では取得が困難な場合がある。規範となる文献DATEX 2 version 2.3 _ParkingRecord_クラスの属性_parkingNumberOfSpaces_。  - `type`: エンティティタイプ。OnStreetParkingと同じでなければなりません。  - `usageScenario`: 駐車場で行われる料金の種類。Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'.    
必須項目  
- `id`  - `location`  - `type`    
DATEX 2バージョン2.3の用語では、_onStreetParking_型の_UrbanParkingSite_に相当します。DATEX II用語のデータ辞書は[http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)にあります。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
      description: 'Vehicle type allowed (only one per on street parking). Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, van, vehicleWithCatalyticConverter, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'''    
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
          - shortTerm    
          - taxiStop    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
    permitActiveHours:    
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week.  It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. An empty JSON Object means always active. The syntax must be conformant with schema.org'    
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
    type:    
      description: 'Entity type. It must be equal to OnStreetParking'    
      enum:    
        - OnStreetParking    
      type: string    
      x-ngsi:    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OnStreetParking/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OnStreetParking/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### OnStreetParking NGSI-v2 のキーバリューの例。  
OnStreetParkingをkey-valuesとしてJSON-LD形式で表現した例を示します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": ["blueZone", "shortTerm", "forDisabled"],  
  "allowedVehicleType": "car",  
  "chargeType": ["temporaryFee"],  
  "requiredPermit": ["blueZonePermit", "disabledPermit"],  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "maximumAllowedStay": "PT2H",  
  "availableSpotNumber": 3,  
  "occupiedSpotNumber": 3,  
  "totalSpotNumber": 6,  
  "extraSpotNumber": 2,  
  "dateModified": "2016-06-02T09:25:55.00Z",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [-3.80356167695194, 43.46296641666926],  
        [-3.803161973253841, 43.46301091092682],  
        [-3.803147082548618, 43.462879859445884],  
        [-3.803536474744068, 43.462838666196674],  
        [-3.80356167695194, 43.46296641666926]  
      ]  
    ]  
  },  
  "areaServed": "Zona Centro",  
  "refParkingGroup": ["daoiz-velarde-1-5-main", "daoiz-velarde-1-5-disabled"]  
}  
```  
#### OnStreetParking NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のOnStreetParkingの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "value": ["blueZone", "shortTerm", "forDisabled"]  
  },  
  "permitActiveHours": {  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "value": ["blueZonePermit", "disabledPermit"]  
  },  
  "allowedVehicleType": {  
    "value": "car"  
  },  
  "chargeType": {  
    "value": ["temporaryFee"]  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
    "value": ["daoiz-velarde-1-5-main", "daoiz-velarde-1-5-disabled"]  
  },  
  "totalSpotNumber": {  
    "value": 6  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [-3.80356167695194, 43.46296641666926],  
          [-3.803161973253841, 43.46301091092682],  
          [-3.803147082548618, 43.462879859445884],  
          [-3.803536474744068, 43.462838666196674],  
          [-3.80356167695194, 43.46296641666926]  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "value": "Zona Centro"  
  },  
  "maximumAllowedStay": {  
    "value": "PT2H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-02T09:25:55.00Z"  
  },  
  "extraSpotNumber": {  
    "value": 2  
  },  
  "availableSpotNumber": {  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  },  
  "occupiedSpotNumber": {  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  }  
}  
```  
#### OnStreetParking NGSI-LDのキー・バリューの例  
OnStreetParkingをkey-valuesとしてJSON-LD形式で表現した例です。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "modifiedAt": "2016-06-02T09:25:55.00Z",  
  "category": {  
    "type": "Property",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "permitActiveHours": {  
    "type": "Property",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "type": "Property",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": "car"  
  },  
  "chargeType": {  
    "type": "Property",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
      "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
    ]  
  },  
  "totalSpotNumber": {  
    "type": "Property",  
    "value": 6  
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
  "areaServed": {  
    "type": "Property",  
    "value": "Zona Centro"  
  },  
  "maximumAllowedStay": {  
    "type": "Property",  
    "value": "PT2H"  
  },  
  "extraSpotNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 3,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "occupiedSpotNumber": {  
    "type": "Property",  
    "value": 3,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### OnStreetParking NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のOnStreetParkingの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "allowedVehicleType": "car",  
  "areaServed": "Zona Centro",  
  "availableSpotNumber": 3,  
  "occupiedSpotNumber": 3,  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "extraSpotNumber": 2,  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
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
  "type": "OnStreetParking"  
}  
```  

マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。