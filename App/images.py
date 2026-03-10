from imagekitio import ImageKit
from dotenv import load_dotenv
import os
load_dotenv()

imagekit = ImageKit (
            private_key=os.getenv("IMAGEKIT-PRIVATE-KEY"),
            public_key=os.getenv("IMAGEKIT-PUBLIC-KEY"),
            url_endpoint=os.getenv("IMAGEKIT-URL")
        )

