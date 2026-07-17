from fastapi import APIRouter

propertyRouter=APIRouter()

@propertyRouter.get("/")
def greet():
    return "Hello Everyone"

