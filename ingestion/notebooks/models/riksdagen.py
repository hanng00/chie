from typing import List, Optional
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class Utskottsforslag(BaseModel):
    """
    ## Utskottsforslag Model

    Utskottet's proposal for a Betänkande.

    """

    punkt: str
    rubrik: str
    forslag: str
    beslutstyp: str
    motforslag_nummer: str
    motforslag_partier: str
    votering_id: str
    votering_sammanfattning_html: str
    votering_url_xml: str
    rm: str
    bet: str
    vinnare: str
    voteringskrav: str
    beslutsregelkvot: str
    beslutsregelparagraf: str
    punkttyp: str


class Aktivitet(BaseModel):
    """
    ## Aktivitet Model

    Information about the activity of a Betänkande. Serves as an audit log.

    """

    kod: str
    namn: str
    datum: str
    status: str
    ordning: str
    process: str


class Uppgift(BaseModel):
    kod: str
    namn: str
    text: str
    dok_id: str
    systemdatum: str


class Bilaga(BaseModel):
    """
    ## Bilaga Model

    Information about a Bilaga. Includes metadata and links to the original document.

    """

    dok_id: str
    subtitel: str
    filnamn: str
    filstorlek: str
    filtyp: str
    titel: str
    fil_url: str


class Referens(BaseModel):
    """
    ## Referens Model

    Information about a Referens. Includes metadata and links to the original document.

    A Referens appears to be a reference to another document, and includes metadata about that document.
    Examples of Referens include:
      - The original Motion's and Proposition's that led to the Betänkande.
      -

    """

    referenstyp: str
    uppgift: str
    ref_dok_id: str
    ref_dok_typ: str
    ref_dok_rm: str
    ref_dok_bet: str
    ref_dok_titel: str
    ref_dok_subtitel: str
    ref_dok_subtyp: str
    ref_dok_dokumentnamn: str


class Dokument(BaseModel):
    """
    ## Dokument Model
    Information about a Betänkande. Includes metadata and links to the original document.
    """

    hangar_id: str
    dok_id: str
    rm: str
    beteckning: str
    typ: str
    subtyp: str
    doktyp: str
    typrubrik: str
    dokumentnamn: str
    debattnamn: str
    tempbeteckning: str
    organ: str
    mottagare: str
    nummer: str
    slutnummer: str
    datum: datetime
    systemdatum: datetime
    publicerad: datetime
    titel: str
    subtitel: str
    status: str
    htmlformat: str
    relaterat_id: str
    source: str
    sourceid: str
    dokument_url_text: str
    dokument_url_html: str
    dokumentstatus_url_xml: str
    utskottsforslag_url_xml: str


class DokUtskottsforslag(BaseModel):
    """
    ## DokUtskottsforslag Model

    Wraps around the Utskottsforslag model to provide a more structured response.
    """

    utskottsforslag: Optional[Utskottsforslag]


class DokAktivitet(BaseModel):
    aktivitet: Optional[List[Aktivitet]]


class DokUppgift(BaseModel):
    uppgift: Optional[List[Uppgift]]


class DokBilaga(BaseModel):
    """
    ## DokBilaga Model

    Wrapper around the Bilaga model to provide a more structured response.
    """

    bilaga: Optional[List[Bilaga]]


class DokReferens(BaseModel):
    """
    ## DokReferens Model

    Wrapper around the Referens model to provide a more structured response.
    """

    referens: Optional[List[Referens]]


class DokumentStatus(BaseModel):
    """
    ## DokumentStatus Model
    Contains all the information about a betänkande.
    """

    dokument: Optional[Dokument]
    dokutskottsforslag: Optional[DokUtskottsforslag]
    dokaktivitet: Optional[DokAktivitet]
    dokuppgift: Optional[DokUppgift]
    dokbilaga: Optional[DokBilaga]
    dokreferens: Optional[DokReferens]
