#!/usr/bin/env python3

"""Hitos de un curso servidos para usted usando Hug"""

import os
import logging

import hug
from hug.middleware import LogMiddleware

from pythonjsonlogger import jsonlogger

from datetime import datetime

from Hitos.Hitos import Hitos

""" Define logger en JSON """
@hug.middleware_class()
class CustomLogger(LogMiddleware):
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        super().__init__(logger=logger)

    def _generate_combined_log(self, request, response):
        """Genera un log similar a nginx."""
        current_time = datetime.utcnow()
        return {'remote_addr':request.remote_addr,
                'time': current_time,
                'method': request.method,
                'uri': request.relative_uri,
                'status': response.status,
                'user-agent': request.user_agent }
    

""" Declara clase """ 
estos_hitos = Hitos()

""" Define API REST """ 
@hug.get('/')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/status')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/all')
def all():
    """Devuelve todos los hitos"""
    return { "hitos": estos_hitos.todos_hitos() }

@hug.get('/one/{id}')
def one( id: int ):
    """Devuelve un hito"""
    return { "hito": estos_hitos.uno( id ) }

""" Usa puerto del entorno si existe """ 
if 'PORT' in os.environ :
    port = int(os.environ['PORT'])
else:
    port = 8000

if __name__ == '__main__':
    hug.API(__name__).http.serve(port )
