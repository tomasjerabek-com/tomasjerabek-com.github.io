#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by: tomas@tomasjerabek.com
# Created on: 28/03/2021

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, HTMLResponse
import datetime


# app initialization
app = FastAPI(title='tomasjerabek.com API',
              description='Repo: <a href=https://github.com/tomasjerabek-com/tomasjerabek.com">'
                          'https://github.com/tomasjerabek-com/tomasjerabek.com</a><br>')
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")


# gzip compression
app.add_middleware(GZipMiddleware, minimum_size=0)


# endpoints section
@app.get("/", tags=["home"], response_class=HTMLResponse)
def home(request: Request):
    """API homepage.<br>
    Return the request response.

    :param request: object<br>
    :returns html
    """
    year = datetime.datetime.today().year
    return templates.TemplateResponse("index.html", {"request": request, "year": year})
