# from fastapi import FastAPI, Depends
# from strawberry.fastapi import GraphQLRouter
# from app.database import get_db
# from app.graphql.schema import schema

# app = FastAPI()

# graphql_app = GraphQLRouter(schema, context_getter=get_db)
# app.include_router(graphql_app, prefix="/graphql")

# @app.get("/")
# async def root():
#     return {"message": "IMDb GraphQL API is running! Visit /graphql"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from app.database import get_db
from app.graphql.schema import schema

app = FastAPI()

# ✅ Enable CORS for frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Attach GraphQL Router with context
graphql_app = GraphQLRouter(schema, context_getter=get_db)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "IMDb GraphQL API is running! Visit /graphql"}
