from mopidy.models import fields, Album, Artist, Track
#class BeetsTrack(Track):

class BeetsAlbum(Album):
  added = fields.Date()
  albumartist_credit = fields.String()
  albumartist_sort  = fields.String()
  albumtype   = fields.String()
  catalognum  = fields.String()
  mb_albumartistid   = fields.String()
  mb_albumid         = fields.String()
  mb_releasegroupid  = fields.String()
  rg_album_gain      = fields.Float()
  rg_album_peak      = fields.Float()
