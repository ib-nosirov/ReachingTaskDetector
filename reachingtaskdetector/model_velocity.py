"""A velocity-based classifier."""

import model_base

class ModelVelocity(model_base.ModelBase):
  """A model that uses velocity to classify between attempt or no attempt."""

  def __init__(self):
    
    # Call parent constructor
    super(ModelVelocity, self).__init__()
