# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = TorrentResultfromdict(json.loads(json_string))

from enum import Enum
from datetime import datetime
from typing import Optional, List, Any, TypeVar, Callable, Type, cast
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class _Tracker(Enum):
    Demonoid = "Demonoid"
    Isohunt2 = "Isohunt2"
    KickAssTorrent = "KickAssTorrent"
    MagnetDL = "MagnetDL"
    ThePirateBay = "The Pirate Bay"
    Torrentz2 = "Torrentz2"
    EZTV = "EZTV"
    ShowRSS = "ShowRSS"


class _TrackerID(Enum):
    demonoid = "demonoid"
    isohunt2 = "isohunt2"
    kickasstorrent = "kickasstorrent"
    magnetdl = "magnetdl"
    thepiratebay = "thepiratebay"
    torrentz2 = "torrentz2"
    eztv = "eztv"
    showrss = "showrss"

class TorrentResult:
    FirstSeen: datetime
    Tracker: str
    TrackerId: str
    CategoryDesc: str
    Title: str
    Guid: str
    Link: Optional[str]
    PublishDate: datetime
    Category: List[int]
    Size: int
    Grabs: Optional[int]
    RageID: Optional[int]
    TVDBId: Optional[int]
    Imdb: Optional[str]
    TMDb: Optional[int]
    Seeders: int
    Peers: int
    MagnetUri: Optional[str]

    def __init__(self, FirstSeen: datetime, Tracker: str, TrackerId: str, CategoryDesc: str, Title: str, Guid: str, Link: Optional[str], PublishDate: datetime, Category: List[int], Size: int, Grabs: Optional[int], RageID: Optional[int], TVDBId: Optional[int], Imdb: Optional[str], TMDb: Optional[int], Seeders: int, Peers: int, MagnetUri: Optional[str]) -> None:
        self.FirstSeen = FirstSeen
        self.Tracker = Tracker
        self.TrackerId = TrackerId
        self.CategoryDesc = CategoryDesc
        self.Title = Title
        self.Guid = Guid
        self.Link = Link
        self.PublishDate = PublishDate
        self.Category = Category
        self.Size = Size
        self.Grabs = Grabs
        self.RageID = RageID
        self.TVDBId = TVDBId
        self.Imdb = Imdb
        self.TMDb = TMDb
        self.Seeders = Seeders
        self.Peers = Peers
        self.MagnetUri = MagnetUri

    @staticmethod
    def from_dict(obj: Any) -> 'TorrentResult':
        assert isinstance(obj, dict)
        FirstSeen = from_datetime(obj.get("FirstSeen"))
        Tracker = from_str(obj.get("Tracker"))
        TrackerId = from_str(obj.get("TrackerId"))
        CategoryDesc = from_str(obj.get("CategoryDesc"))
        Title = from_str(obj.get("Title"))
        Guid = from_str(obj.get("Guid"))
        Link = from_union([from_none, from_str], obj.get("Link"))
        PublishDate = from_datetime(obj.get("PublishDate"))
        Category = from_list(from_int, obj.get("Category"))
        Size = from_int(obj.get("Size"))
        Grabs = from_union([from_none, from_int], obj.get("Grabs"))
        RageID = from_union([from_none, from_int], obj.get("RageID"))
        TVDBId = from_union([from_none, from_int], obj.get("TVDBId"))
        Imdb = from_union([from_none, from_str], obj.get("Imdb"))
        TMDb = from_union([from_none, from_int], obj.get("TMDb"))
        Seeders = from_int(obj.get("Seeders"))
        Peers = from_int(obj.get("Peers"))
        MagnetUri = from_union([from_none, from_str], obj.get("MagnetUri"))
        return TorrentResult(FirstSeen, Tracker, TrackerId, CategoryDesc, Title, Guid, Link, PublishDate, Category, Size, Grabs, RageID, TVDBId, Imdb, TMDb, Seeders, Peers, MagnetUri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FirstSeen"] = self.FirstSeen.isoformat()
        result["Tracker"] = from_str(self.Tracker)
        result["TrackerId"] = from_str(self.TrackerId)
        result["CategoryDesc"] = from_str(self.CategoryDesc)
        result["Title"] = from_str(self.Title)
        result["Guid"] = from_str(self.Guid)
        result["Link"] = from_union([from_none, from_str], self.Link)
        result["PublishDate"] = self.PublishDate.isoformat()
        result["Category"] = from_list(from_int, self.Category)
        result["Size"] = from_int(self.Size)
        result["Grabs"] = from_union([from_none, from_int], self.Grabs)
        result["RageID"] = from_union([from_none, from_int], self.RageID)
        result["TVDBId"] = from_union([from_none, from_int], self.TVDBId)
        result["Imdb"] = from_union([from_none, from_str], self.Imdb)
        result["TMDb"] = from_union([from_none, from_int], self.TMDb)
        result["Seeders"] = from_int(self.Seeders)
        result["Peers"] = from_int(self.Peers)
        result["MagnetUri"] = from_union([from_none, from_str], self.MagnetUri)
        return result


def TorrentResults(s: Any) -> List[TorrentResult]:
    return from_list(TorrentResult.from_dict, s)


def TorrentResulttodict(x: List[TorrentResult]) -> Any:
    return from_list(lambda x: to_class(TorrentResult, x), x)
