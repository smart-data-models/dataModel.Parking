エンティティパーキンググループ  
===============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**パーキンググループ **  

## プロパティのリスト  

- `allowedVehicleType`: 許可される車両タイプ（駐車グループは1つの車両タイプしか許可しません）。Enum:'bike, bus, car, caravan, motorcycle, motorscooter, truck'.  - `alternateName`: このアイテムの別称  - `areBordersMarked`: 駐車場が（空欄などで）区切られているかどうかを示す。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります。  - `availableSpotNumber`: このグループで利用可能なスポットの数です。これは `totalSpotNumber` 以下の値でなければなりません。  - `averageSpotLength`: パーキングスポットの平均的な長さ。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD）。  - `averageSpotWidth`: パーキングスポットの平均的な幅。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります。  - `category`: 駐車場グループのカテゴリー。Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'.  - `chargeType`: 駐車場で行われる料金の種類。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'.  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `id`: エンティティのユニークな識別子  - `maximumAllowedHeight`: 車両の最大許容高さ。  アプリケーションは、このプロパティが定義されていない場合、親のレベルでこのプロパティの値を検査しなければならない（SHOULD）。  - `maximumAllowedWidth`: 車両の最大許容幅。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD）。  - `maximumParkingDuration`: 最大許容滞在時間は、ISO8601の期間としてエンコードされます。存在しない場合や空の文字列に等しい場合は、無期限を意味する。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査しなければならない（SHOULD）。  - `name`: このアイテムの名前です。  - `occupancyDetectionType`: 許可された値。DATEX II バージョン2.3 _OccupancyDetectionTypeEnum_からの以下のもの。Enum:'balancing, manual, modelBased, none, singleSpaceDetection'.またはその他のアプリケーション固有の  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `parkingMode`: 駐車場モードです。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査しなければならない（SHOULD）。許される値DATEX IIバージョン2.3の_ParkingModeEnum_列挙で定義されたもの。Enum:'echelonParking, parallelParking, perpendicularParking' (エシュロンパーキング、パラレルパーキング、パーペンディキュラーパーキング)  - `permitActiveHours`: この属性により、許可証が特定の時間帯や曜日にのみ必要とされる状況を把握することができます。これは構造化された値で、必要とされる各許可証ごとに、その許可証がいつ有効かを示すサブプロパティを含まなければなりません。パーミットに何も指定されていない場合は、常にパーミットが必要であることを意味します。空のオブジェクトは、常にアクティブであることを意味します。構文は、schema.org [opening hours specification](https://schema.org/openingHours)に準拠していなければならない。例えば、デイウィークにのみ有効なブルーゾーンは、'blueZonePermit': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'とエンコードされます。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査する必要があります（SHOULD）。  - `refParkingSite`: このゾーンが所属するパーキングサイトです。グループは孤児になることはできません。グループはサブグループを持つことはできない。OffStreetParkingまたはOnStreetParkingへの参照  - `refParkingSpot`: この駐車場グループに属する個々の駐車場。  - `requiredPermit`: この属性は、このサイトに駐車するためにどのような許可証が必要であるかを示す。意味としては、これらの許可証のうち少なくとも_1つが駐車に必要であるということです。許可証が複数の項目（and）で構成されている場合、それらは「,」で結合することができます。例えば、'residentPermit,disabledPermit'は、居住者と障害者の両方の許可証が同時に駐車に必要であることを示します。リストが空の場合、許可証は必要ありません。  - `reservationType`: 予約の条件。このプロパティが定義されていない場合、アプリケーションは親のレベルでこのプロパティの値を検査しなければならない（SHOULD）。Enum:'mandatory, notAvailable, optional, partly'.  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalSpotNumber`: このグループに関連するスポットの合計数。許容される値任意の正の整数値または0。DATEX 2 version 2.3 _ParkingRecord_クラスの_parkingNumberOfSpaces_属性。  - `type`: NGSI エンティティタイプ。ParkingGroupでなければなりません。    
必須項目  
- `id`  - `refParkingSite`  - `type`    
駐車場のグループです。粒度のレベルは様々です。駐車場の階数であったり、大きな駐車場に属する特定のゾーンであったり、特定の車種を駐車するためのスポットのグループであったり、特定の制限（障害者、居住者、...）の対象となるスポットであったり。簡略化のため、1つの駐車場グループにつき1種類の車両のみが許可されます。同様に、必要な許可証も1つのグループタイプにつき1つしか認められません。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingGroup:    
  description: 'Parking Group '    
  properties:    
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
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available in this group. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
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
    id:    
      anyOf: &parkinggroup_-_properties_-_owner_-_items_-_anyof    
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
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
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
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkinggroup_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking'    
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
      description: 'Individual parking spots belonging to this parking group.'    
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
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ParkingGroup'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingGroup/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/ParkingGroup/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### ParkingGroup NGSI-v2 key-values の例。  
ここでは、ParkingGroupをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": ["onStreet", "adjacentSpaces", "onlyDisabled"],  
  "allowedVehicleType": "car",  
  "chargeType": ["free"],  
  "refParkingSite": "daoiz-velarde-1-5",  
  "description": "Two parking spots reserved for disabled people",  
  "totalSpotNumber": 2,  
  "availableSpotNumber": 1,  
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
  "requiredPermit": ["disabledPermit"],  
  "permitActiveHours": {"Monday":"null"}  
}  
```  
#### パーキンググループ NGSI-v2 正規化された例  
ここでは、正規化されたJSON-LD形式のParkingGroupの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": "null"  
  },  
  "requiredPermit": {  
    "value": "disabledPermit"  
  },  
  "allowedVehicleType": {  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "value": 1,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-12T12:00:00"  
      }  
    }  
  },  
  "totalSpotNumber": {  
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
    "value": ["free"]  
  },  
  "description": {  
    "value": "Two parking spots reserved for disabled people"  
  }  
}  
```  
#### ParkingGroup NGSI-LDのキーバリューの例。  
ここでは、ParkingGroupをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": {  
    "type": "Property",  
    "value": [  
      "onstreet",  
      "adjacentSpaces",  
      "onlyDisabled"  
    ]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5"  
  },  
  "permitActiveHours": {  
    "type": "Property",  
    "value": "null"  
  },  
  "requiredPermit": {  
    "type": "Property",  
    "value": "disabledPermit"  
  },  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 1,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "totalSpotNumber": {  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### パーキンググループ NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のParkingGroupの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
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
  "type": "ParkingGroup"  
}  
```  
