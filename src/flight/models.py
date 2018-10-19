from abc import ABCMeta
import uuid
from datetime import datetime

class Model(object):
  """
  Abstract base class for all models -
  all models should extend this class
  """
  __metaclass__ = ABCMeta

  def __init__(self):
    self.id = str(uuid.uuid1())

  def to_dict(self):
    """
    Dictionary representation of this Model
    """
    return vars(self)


