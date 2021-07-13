
class ModelBase(object):
  """A base class for all models used in modeling the reaching task."""

  def __init__(self):

  @property
  def timestamps(self):
    return _timestamps

  def convert_to_timestmps(self, time):
    seconds = int(time % 60)
    minutes = int(time / 60)
    _timestamps.append((minutes,seconds))
