エンティティパーキングスポット  
===============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingSpot/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**駐車場とは、1台の車を駐車することができる区画のことである。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `annotations`: アイテムに関するアノテーション  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `category`: パーキングスポットのカテゴリーonStreet` : その駐車場はonStreet駐車場に属しています。offStreet` : 駐車場はoffStreetパーキングサイトに属します。  - `color`: 商品の色について  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `id`: エンティティのユニークな識別子  - `image`: アイテムのイメージ  - `length`: 駐車場の長さ  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `refDevice`: この駐車場を監視するための物理的なセンサーを表すデバイスです。  - `refParkingGroup`: パーキングスポットが所属するグループ。モデルの簡略化のために、1つの駐車場につき1つのグループしか認められていません。  - `refParkingSite`: その駐車場が属する駐車場サイト。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `status`: 駐車場の占有状態を表す。Enum:'closed, free, occupied, unknown'.  - `timeInstant`: ペイロードのタイムスタンプ。本番環境では、属性タイプが `ISO8601` の文字列と同じである場合があります。その場合は、`DateTime` の同義語として考えなければなりません。この属性は、古いFIWAREリファレンスの実装との下位互換性のために残されています。  - `type`: NGSI エンティティタイプ。ParkingSpotである必要があります。  - `width`: 駐車場の幅    
必須項目  
- `category`  - `id`  - `location`  - `refParkingSite`  - `status`  - `type`    
このエンティティタイプの目的は、パーキングスポットの状態を個別に監視することです。したがって、ParkingSpotタイプのエンティティは、(OnStreetParking, OffStreetParking)タイプのエンティティを含むことなく存在することはできません。パーキングスポットは、1つのグループに属するかもしれません。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingSpot:    
  description: 'A parking spot is an area well delimited where one vehicle can be parked.'    
  properties:    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Category(ies) of the parking spot. `onStreet` : The parking spot belongs to an onStreet parking site. `offStreet` : The parking spot belongs to an offStreet parking site.'    
      items:    
        enum:    
          - onStreet    
          - offStreet    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
      anyOf: &parkingspot_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    length:    
      description: 'Length of the parking spot.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkingspot_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      description: 'The device representing the physical sensor used to monitor this parking spot.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Relationship    
    refParkingGroup:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Group to which the parking spot belongs to. For model simplification purposes only one group is allowed per parking spot.'    
      x-ngsi:    
        type: Relationship    
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
      description: 'Parking site to which the parking spot belongs to.'    
      x-ngsi:    
        type: Relationship    
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
    status:    
      description: 'Status of the parking spot from the point of view of occupancy. Enum:''closed, free, occupied, unknown'''    
      enum:    
        - closed    
        - free    
        - occupied    
        - unknown    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ParkingSpot'    
      enum:    
        - ParkingSpot    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Width of the parking spot.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
  required:    
    - id    
    - location    
    - type    
    - status    
    - category    
    - refParkingSite    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingSpot/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/ParkingSpot/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## ペイロードの例  
#### ParkingSpot NGSI-v2 key-valuesの例。  
ここでは、ParkingSpotをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "name": "A-13",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.80356167695194, 43.46296641666926]  
  },  
  "status": "free",  
  "category": ["onStreet"],  
  "refParkingSite": "santander:daoiz_velarde_1_5"  
}  
```  
#### ParkingSpot NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のParkingSpotの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "status": {  
    "value": "free",  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-21T12:00:00"  
      },  
      "parkingPermit": {  
        "type": "Property",  
        "value": "yes"  
      }  
    }  
  },  
  "category": {  
    "value": ["onStreet"]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "santander:daoiz_velarde_1_5"  
  },  
  "name": {  
    "value": "A-13"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.80356167695194, 43.46296641666926]  
    }  
  }  
}  
```  
#### ParkingSpot NGSI-LDのキーバリューの例。  
ここでは、ParkingSpotをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:ParkingSpot:santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "status": {  
    "type": "Property",  
    "value": "free",  
    "observedAt": "2018-09-21T12:00:00Z",  
    "parkingPermit": {  
      "type": "Property",  
      "value": "yes"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "onStreet"  
    ]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ParkingSite:santander:daoiz_velarde_1_5"  
  },  
  "name": {  
    "type": "Property",  
    "value": "A-13"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.80356167695194,  
        43.46296641666926  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### ParkingSpot NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のParkingSpotの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "category": [  
    "onStreet"  
  ],  
  "id": "urn:ngsi-ld:ParkingSpot:santander:daoiz_velarde_1_5:3",  
  "location": {  
    "coordinates": [  
      -3.80356167695194,  
      43.46296641666926  
    ],  
    "type": "Point"  
  },  
  "name": "A-13",  
  "refParkingSite": "urn:ngsi-ld:ParkingSite:santander:daoiz_velarde_1_5",  
  "status": "free",  
  "type": "ParkingSpot"  
}  
```  
