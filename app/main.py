from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import uvicorn
from mangum import Mangum

from app.model.items import Items
from app.extract.index import lambda_handler

items = Items

app = FastAPI()

origins = []

###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################

handler = Mangum(app)

app.add_middleware(
	 CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/data/facturedo")
async def main(item: Items):
	try:
		if item.id == 12345678 and item.name == "RolFacturedo":
				create_file = lambda_handler()
				return create_file
		else: 
				return "Parameter error"
	except OSError as err:
			return {"messages": "Datos enviados en el body fallaron" }
 
 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

  
