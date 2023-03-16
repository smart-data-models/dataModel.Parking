<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティパーキンググループ  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな内容です。**駐車場グループ  
バージョン：0.1.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `allowedVehicleType[string]`: 許可される車種（駐車場グループは1つの車種しか許可しない）。Enum:'自転車、バス、車、キャラバン、バイク、モータースクーター、トラック'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: このアイテムの別称  - `areBordersMarked[boolean]`: 駐車場が区切られているかどうか（空白線などで区切られているかどうか）を示す。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_INSPECT）。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: このグループで利用可能なスポットの数。totalSpotNumber`より小さいか等しくなければならない。  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 駐車場の平均的な長さです。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: 駐車場の平均的な幅を示す。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: 駐車場グループのカテゴリーです。Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  . Model: [http://schema.org/Text](http://schema.org/Text)- `chargeType[array]`: 駐車場が実施する料金の種類（複数可）。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'.  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかとする。  - `maximumAllowedHeight[number]`: 車両の最大許容高さ。  このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: 車両の最大許容幅。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[string]`: ISO8601 の期間としてエンコードされた最大許容滞在時間。存在しない場合、または空文字列に等しい場合は、無期限を意味します。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  - `name[string]`: この項目の名称です。  - `occupancyDetectionType[array]`: 許容される値。DATEX II version 2.3 _OccupancyDetectionTypeEnum_ より以下の通り。Enum:'balancing, manual, modelBased, none, singleSpaceDetection'.または、その他のアプリケーション固有の  . Model: [http://schema.org/Text](http://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `parkingMode[array]`: 駐車モード（複数可）。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_INSPECT）。許容される値。DATEX II version 2.3 _ParkingModeEnum_ enumerationで定義されたもの。列挙：'echelonParking, parallelParking, perpendicularParking' です。  . Model: [http://schema.org/Text](http://schema.org/Text)- `permitActiveHours[object]`: この属性により、特定の時間帯や曜日のみ許可が必要な状況を把握することができます。この属性は構造化された値で、必要な許可ごとに、その許可がいつ有効かを示すサブプロパティが含まれていなければなりません。許可証に何も指定しない場合は、常に許可証が必要であることを意味します。空のオブジェクトは、常にアクティブであることを意味する。構文は、schema.org [営業時間指定](https://schema.org/openingHours)に準拠する必要があります。例えば、平日のみ活動するブルーゾーンは、「blueZonePermit」：「Mo,Tu,We,Th,Fr,Sa 09:00-20:00 」としてエンコードされます。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD_）。  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `refParkingSite[*]`: このゾーンが属する駐車場サイト。グループには孤児を設定できません。グループは、サブグループを持つことはできない。OffStreetParkingまたはOnStreetParkingへの参照。  - `refParkingSpot[*]`: この駐車場グループに属する個々の駐車場。  - `requiredPermit[array]`: この属性は、このサイトで駐車するために必要かもしれない許可証をキャプチャします。意味としては、これらの許可証のうち少なくとも1つが駐車に必要であるということである。許可証が複数の項目で構成されている場合（および）、それらは「,」で結合することができます。例えば、「residentPermit,disabledPermit」は、駐車するために居住者と障害者の両方の許可証が同時に必要であることを示します。リストが空の場合、許可証は必要ありません  . Model: [http://schema.org/Text](http://schema.org/Text)- `reservationType[string]`: 予約の条件このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する _SHOULD_ べきである。Enum:'mandatory, notAvailable, optional, partly'.  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalSpotNumber[number]`: このグループに関連するスポットの総数。許容される値。任意の正の整数値または0。DATEX 2 version 2.3 _ParkingRecord_クラスの_parkingNumberOfSpaces_属性。  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI Entityタイプ。ParkingGroupである必要があります。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `refParkingSite`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
駐車場のグループです。粒度は様々です。駐車場の1階部分、大きな駐車場の特定のゾーン、あるいは特定の車種を駐車するためのスポットのグループ、または特定の制限（障害者、住民、...）がある場合もあります。簡略化のため、1つの駐車場グループにつき1つの車種のみが許可されています。同様に、必要な許可証も1つのグループタイプにつき、1つだけ許可されます。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      description: The number of spots available in this group. It must lower or equal than `totalSpotNumber`.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined.    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined.    
      exclusiveMinimum: true    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      anyOf: &parkinggroup_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    maximumAllowedHeight:    
      description: Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined.    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined.    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
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
        anyOf: *parkinggroup_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
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
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
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
      description: Individual parking spots belonging to this parking group.    
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
      description: 'Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Enum:''mandatory, notAvailable, optional, partly''.'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalSpotNumber:    
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
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
## ペイロードの例  
#### ParkingGroup NGSI-v2 キーバリュー例  
ParkingGroupをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ParkingGroup NGSI-v2 正規化例  
正規化されたJSON-LD形式のParkingGroupの例を示します。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": {  
    "value": ["onstreet", "adjacentSpaces", "onlyDisabled"]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "value": "daoiz-velarde-1-5"  
  },  
  "permitActiveHours": {  
    "type": "Text",  
    "value": "null"  
  },  
  "requiredPermit": {  
    "type": "Text",  
    "value": "disabledPermit"  
  },  
  "allowedVehicleType": {  
    "type": "Text",  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "type": "Number",  
    "value": 1,  
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
          [-3.80356167695194, 43.46296641666926],  
          [-3.803161973253841, 43.46301091092682],  
          [-3.803147082548618, 43.462879859445884],  
          [-3.803536474744068, 43.462838666196674],  
          [-3.80356167695194, 43.46296641666926]  
        ]  
      ]  
    }  
  },  
  "chargeType": {  
    "type": "array",  
    "value": ["free"]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Two parking spots reserved for disabled people"  
  }  
}  
```  
</details>  
#### ParkingGroup NGSI-LD キーバリュー例  
ここでは、ParkingGroupをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 駐車場グループ NGSI-LD 正規化例  
ParkingGroupをJSON-LD形式で正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)をご参照ください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
