from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AllowedVehicleType(Enum):
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    motorcycle = 'motorcycle'
    motorscooter = 'motorscooter'
    truck = 'truck'


class CategoryEnum(Enum):
    adjacentSpaces = 'adjacentSpaces'
    blueZone = 'blueZone'
    completeFloor = 'completeFloor'
    free = 'free'
    feeCharged = 'feeCharged'
    greenZone = 'greenZone'
    loadUnloadZone = 'loadUnloadZone'
    nonAdjacentSpaces = 'nonAdjacentSpaces'
    offStreet = 'offStreet'
    onlyDisabled = 'onlyDisabled'
    onlyElectricalCharging = 'onlyElectricalCharging'
    onlyResidents = 'onlyResidents'
    onlyWithPermit = 'onlyWithPermit'
    onStreet = 'onStreet'
    particularConditionsSpaces = 'particularConditionsSpaces'
    shortTermMediumTermLongTerm = 'shortTermMediumTermLongTerm'
    statisticsOnly = 'statisticsOnly'
    vehicleTypeSpaces = 'vehicleTypeSpaces'


class ChargeTypeEnum(Enum):
    additionalIntervalPrice = 'additionalIntervalPrice'
    annualPayment = 'annualPayment'
    firstIntervalPrice = 'firstIntervalPrice'
    flat = 'flat'
    free = 'free'
    minimum = 'minimum'
    maximum = 'maximum'
    monthlyPayment = 'monthlyPayment'
    seasonTicket = 'seasonTicket'
    temporaryFee = 'temporaryFee'
    temporaryPrice = 'temporaryPrice'
    unknown = 'unknown'
    other = 'other'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OccupancyDetectionTypeEnum(Enum):
    balancing = 'balancing'
    manual = 'manual'
    modelBased = 'modelBased'
    none = 'none'
    singleSpaceDetection = 'singleSpaceDetection'


class ParkingModeEnum(Enum):
    echelonParking = 'echelonParking'
    parallelParking = 'parallelParking'
    perpendicularParking = 'perpendicularParking'


class RequiredPermitEnum(Enum):
    employeePermit = 'employeePermit'
    studentPermit = 'studentPermit'
    fairPermit = 'fairPermit'
    governmentPermit = 'governmentPermit'
    residentPermit = 'residentPermit'
    specificIdentifiedVehiclePermit = 'specificIdentifiedVehiclePermit'
    disabledPermit = 'disabledPermit'
    visitorPermit = 'visitorPermit'
    blueZonePermit = 'blueZonePermit'
    careTakingPermit = 'careTakingPermit'
    carpoolingPermit = 'carpoolingPermit'
    carSharingPermit = 'carSharingPermit'
    emergencyVehiclePermit = 'emergencyVehiclePermit'
    maintenanceVehiclePermit = 'maintenanceVehiclePermit'
    roadWorksPermit = 'roadWorksPermit'
    taxiPermit = 'taxiPermit'
    transportationPermit = 'transportationPermit'
    noPermitNeeded = 'noPermitNeeded'


class ReservationType(Enum):
    mandatory = 'mandatory'
    notAvailable = 'notAvailable'
    optional = 'optional'
    partly = 'partly'


class Type6(Enum):
    ParkingGroup = 'ParkingGroup'


class ParkingGroup(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    allowedVehicleType: Optional[AllowedVehicleType] = Field(
        None,
        description="Vehicle type allowed (a parking group only allows one vehicle type). Enum:'bicycle, bus, car, caravan, motorcycle, motorscooter, truck' ",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areBordersMarked: Optional[bool] = Field(
        None,
        description="Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availableSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of spots available in this group. It must lower or equal than `totalSpotNumber`',
    )
    averageSpotLength: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description="The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    averageSpotWidth: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description="The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Parking Group's category. Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'",
    )
    chargeType: Optional[List[ChargeTypeEnum]] = Field(
        None,
        description="Type of charge(s) performed by the parking site. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maximumAllowedHeight: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description="Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    maximumAllowedWidth: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description="Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    maximumParkingDuration: Optional[AwareDatetime] = Field(
        None,
        description="Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    occupancyDetectionType: Optional[List[OccupancyDetectionTypeEnum]] = Field(
        None,
        description="Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Or any other application-specific",
        min_length=1,
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    parkingMode: Optional[List[ParkingModeEnum]] = Field(
        None,
        description="Parking mode(s). Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined. Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:'echelonParking, parallelParking, perpendicularParking'",
        min_length=1,
    )
    permitActiveHours: Optional[Dict[str, Any]] = Field(
        None,
        description="This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. Empty object means always active. The syntax must be conformant with schema.org [opening hours specification](https://schema.org/openingHours). For instance, a blue zone which is only active on dayweeks will be encoded as 'blueZonePermit': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined",
    )
    refParkingSite: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking',
    )
    refParkingSpot: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='Individual parking spots belonging to this parking group'
    )
    requiredPermit: Optional[List[RequiredPermitEnum]] = Field(
        None,
        description="This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ','. For instance 'residentPermit,disabledPermit' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed",
    )
    reservationType: Optional[ReservationType] = Field(
        None,
        description="Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined. Enum:'mandatory, notAvailable, optional, partly'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    totalSpotNumber: Optional[confloat(ge=1.0)] = Field(
        None,
        description='The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be ParkingGroup'
    )
