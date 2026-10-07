"""Gestion centralisée des erreurs HTTP de l'API."""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def enregistrer_gestionnaires(app: FastAPI) -> None:
    """Enregistre les réponses d'erreur communes (les erreurs d'entrée valent 400)."""

    @app.exception_handler(RequestValidationError)
    async def erreur_entree(_request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(status_code=400, content={"detail": exc.errors()})

    @app.exception_handler(ValueError)
    async def erreur_valeur(_request: Request, exc: ValueError) -> JSONResponse:
        return JSONResponse(status_code=400, content={"detail": str(exc)})
