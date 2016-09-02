from mopidy.models import Album, Artist, Track
#class BeetsTrack(Track):

class BeetsAlbum(Album):
  added = None
  albumartist_credit = None
  albumartist_sort  = None
  albumdisambig = None
  albumstatus = None
  albumtotal  = None
  albumtype   = None
  artpath     = None
  asin        = None
  catalognum  = fields.String()
  comp        = None
  country     = None
  disctotal   = None
  language    = None
  mb_albumartistid   = None
  mb_albumid         = None
  mb_releasegroupid  = None
  month              = None
  rg_album_gain      = None
  rg_album_peak      = None
  script             = None
