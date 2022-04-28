from api import Api
from documentation import Doc

import justpy as jp
jp.Route("/api", Api.serve)
jp.Route("/", Doc.serve)
jp.justpy()