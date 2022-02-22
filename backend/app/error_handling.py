def return_error(msg: str = None):
  """
  Return an error to the user

  Defaults to: "An unknown error happened, please refresh the page and try again. Contact support if the issue persists."
  """
  if not msg:
    return 'An unknown error happened, please refresh the page and try again. Contact support if the issue persists.'
  else:
    return f'{msg}'