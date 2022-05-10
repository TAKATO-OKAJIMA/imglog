# IMGLOG

## What is IMGLOG

A logger for images that aims to be used like the standard python module logging

## Installation

``` sh
pip install git+https://github.com/TAKATO-OKAJIMA/imglog.git
```

## Example Code

### bytes

``` python
import logging
from imglog import BytesImageLoggerFactory, HTMLHandler


factory = BytesImageLoggerFactory()
logger = factory.getLogger()

logger.setLevel(logging.INFO)
logger.addHandler(HTMLHandler('./image_log.html'))
logger.info(BYTES_IMAGE)
```

### ndarray

``` python
import logging
from imglog import ArrayImageLoggerFactory, HTMLHandler


factory = ArrayImageLoggerFactory()
logger = factory.getLogger()

logger.setLevel(logging.INFO)
logger.addHandler(HTMLHandler('./image_log.html'))
logger.info(NDARRAY_IMAGE)
```

### Pillow

``` python
import logging
from imglog import PillowImageLoggerFactory, HTMLHandler


factory = PillowImageLoggerFactory()
logger = factory.getLogger()

logger.setLevel(logging.INFO)
logger.addHandler(HTMLHandler('./image_log.html'))
logger.info(PILLOW_IMAGE)
```

## License

[MIT](LICENSE)