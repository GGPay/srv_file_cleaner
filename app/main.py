# isort:skip_file

import sys
import uvicorn
from app.application import app
from app.routes.processing import router as processing_router


sys.path.extend(["./"])


ROUTERS = [processing_router]

for r in ROUTERS:
    app.include_router(r)


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
