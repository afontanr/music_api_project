# Django API - Quick Start Guide

This project is a Django-based API that provides endpoints for managing albums and artists. Below are the instructions to set up and run the project using Docker.

## Running the Project with Docker

To quickly get started, follow these steps:

1. **Build and start the containers**  
   ```sh
   docker-compose up --build
   ```
2. **Access the API documentation (Swagger UI)**  
   Once the server is running, you can explore the API using Swagger
   - Open your browser and go to: http://localhost:8000/swagger/
   
3. **Stop the containers**  
   ```sh
   docker-compose down -v
   ```
## Executing test
 Running the command pytest in the root directory will run all the tests:
 ```sh
   pytest
 ```
---
## Examples
### **Get all artists**

#### Request
 ```sh
   curl -X 'GET' \
  'http://127.0.0.1:8000/api/artists/' \
  -H 'accept: application/json'
 ```
### Response when success (200)
```json
{
  "pagination": {
    "total_items": 275,
    "total_pages": 28,
    "current_page": 1,
    "next_page": "http://127.0.0.1:8000/api/artists/?page=2",
    "previous_page": null,
    "page_size": 10
  },
  "results": [
    {
      "id": 43,
      "name": "A Cor Do Som"
    },
    {
      "id": 1,
      "name": "Ac/Dc"
    },
    {
      "id": 230,
      "name": "Aaron Copland & London Symphony Orchestra"
    },
    {
      "id": 202,
      "name": "Aaron Goldberg"
    },
    {
      "id": 214,
      "name": "Academy Of St. Martin In The Fields & Sir Neville Marriner"
    },
    {
      "id": 215,
      "name": "Academy Of St. Martin In The Fields Chamber Ensemble & Sir Neville Marriner"
    },
    {
      "id": 222,
      "name": "Academy Of St. Martin In The Fields, John Birch, Sir Neville Marriner & Sylvia Mcnair"
    },
    {
      "id": 257,
      "name": "Academy Of St. Martin In The Fields, Sir Neville Marriner & Thurston Dart"
    },
    {
      "id": 239,
      "name": "Academy Of St. Martin In The Fields, Sir Neville Marriner & William Bennett"
    },
    {
      "id": 2,
      "name": "Accept"
    }
  ]
}
```
#### Response when page not found (404)
```json
{
  "detail": "Page not found"
}
```

### **Get all albums**

#### Request
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/albums/' \
  -H 'accept: application/json' \
  -H 'X-CSRFTOKEN: xLZICNadvAKrLaPWiKsKoAMjA65dvS3f'
```

#### Response when success (200)
```json
{
  "pagination": {
    "total_items": 347,
    "total_pages": 35,
    "current_page": 1,
    "next_page": "http://127.0.0.1:8000/api/albums/?page=2",
    "previous_page": null,
    "page_size": 10
  },
  "results": [
    {
      "id": 156,
      "title": "...And Justice For All",
      "artist": 50,
      "tracks": [
        {
          "id": 1893,
          "name": "Blackened",
          "composer": "James Hetfield, Lars Ulrich & Jason Newsted",
          "milliseconds": 403382,
          "bytes": 13254874,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1894,
          "name": "...And Justice For All",
          "composer": "James Hetfield, Lars Ulrich & Kirk Hammett",
          "milliseconds": 585769,
          "bytes": 19262088,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1895,
          "name": "Eye Of The Beholder",
          "composer": "James Hetfield, Lars Ulrich & Kirk Hammett",
          "milliseconds": 385828,
          "bytes": 12747894,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1896,
          "name": "One",
          "composer": "James Hetfield & Lars Ulrich",
          "milliseconds": 446484,
          "bytes": 14695721,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1897,
          "name": "The Shortest Straw",
          "composer": "James Hetfield and Lars Ulrich",
          "milliseconds": 395389,
          "bytes": 13013990,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1898,
          "name": "Harvester Of Sorrow",
          "composer": "James Hetfield and Lars Ulrich",
          "milliseconds": 345547,
          "bytes": 11377339,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1899,
          "name": "The Frayed Ends Of Sanity",
          "composer": "James Hetfield, Lars Ulrich and Kirk Hammett",
          "milliseconds": 464039,
          "bytes": 15198986,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1900,
          "name": "To Live Is To Die",
          "composer": "James Hetfield, Lars Ulrich and Cliff Burton",
          "milliseconds": 588564,
          "bytes": 19243795,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1901,
          "name": "Dyers Eve",
          "composer": "James Hetfield, Lars Ulrich and Kirk Hammett",
          "milliseconds": 313991,
          "bytes": 10302828,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        }
      ]
    },
    {
      "id": 257,
      "title": "20th Century Masters - The Millennium Collection: The Best of Scorpions",
      "artist": 179,
      "tracks": [
        {
          "id": 3288,
          "name": "Rock You Like a Hurricane",
          "composer": null,
          "milliseconds": 255766,
          "bytes": 4300973,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3289,
          "name": "No One Like You",
          "composer": null,
          "milliseconds": 240325,
          "bytes": 4050259,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3290,
          "name": "The Zoo",
          "composer": null,
          "milliseconds": 332740,
          "bytes": 5550779,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3291,
          "name": "Loving You Sunday Morning",
          "composer": null,
          "milliseconds": 339125,
          "bytes": 5654493,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3292,
          "name": "Still Loving You",
          "composer": null,
          "milliseconds": 390674,
          "bytes": 6491444,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3293,
          "name": "Big City Nights",
          "composer": null,
          "milliseconds": 251865,
          "bytes": 4237651,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3294,
          "name": "Believe in Love",
          "composer": null,
          "milliseconds": 325774,
          "bytes": 5437651,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3295,
          "name": "Rhythm of Love",
          "composer": null,
          "milliseconds": 231246,
          "bytes": 3902834,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3296,
          "name": "I Can't Explain",
          "composer": null,
          "milliseconds": 205332,
          "bytes": 3482099,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3297,
          "name": "Tease Me Please Me",
          "composer": null,
          "milliseconds": 287229,
          "bytes": 4811894,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3298,
          "name": "Wind of Change",
          "composer": null,
          "milliseconds": 315325,
          "bytes": 5268002,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 3299,
          "name": "Send Me an Angel",
          "composer": null,
          "milliseconds": 273041,
          "bytes": 4581492,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        }
      ]
    },
    {
      "id": 296,
      "title": "A Copland Celebration, Vol. I",
      "artist": 230,
      "tracks": [
        {
          "id": 3427,
          "name": "Fanfare for the Common Man",
          "composer": "Aaron Copland",
          "milliseconds": 198064,
          "bytes": 3211245,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Classical"
        }
      ]
    },
    {
      "id": 94,
      "title": "A Matter of Life and Death",
      "artist": 90,
      "tracks": [
        {
          "id": 1201,
          "name": "Different World",
          "composer": null,
          "milliseconds": 258692,
          "bytes": 4383764,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1202,
          "name": "These Colours Don't Run",
          "composer": null,
          "milliseconds": 412152,
          "bytes": 6883500,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1203,
          "name": "Brighter Than a Thousand Suns",
          "composer": null,
          "milliseconds": 526255,
          "bytes": 8721490,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1204,
          "name": "The Pilgrim",
          "composer": null,
          "milliseconds": 307593,
          "bytes": 5172144,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1205,
          "name": "The Longest Day",
          "composer": null,
          "milliseconds": 467810,
          "bytes": 7785748,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1206,
          "name": "Out of the Shadows",
          "composer": null,
          "milliseconds": 336896,
          "bytes": 5647303,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1207,
          "name": "The Reincarnation of Benjamin Breeg",
          "composer": null,
          "milliseconds": 442106,
          "bytes": 7367736,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1208,
          "name": "For the Greater Good of God",
          "composer": null,
          "milliseconds": 564893,
          "bytes": 9367328,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1209,
          "name": "Lord of Light",
          "composer": null,
          "milliseconds": 444614,
          "bytes": 7393698,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1210,
          "name": "The Legacy",
          "composer": null,
          "milliseconds": 562966,
          "bytes": 9314287,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        },
        {
          "id": 1211,
          "name": "Hallowed Be Thy Name (Live) [Non Album Bonus Track]",
          "composer": null,
          "milliseconds": 431262,
          "bytes": 7205816,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Rock"
        }
      ]
    },
    {
      "id": 95,
      "title": "A Real Dead One",
      "artist": 90,
      "tracks": [
        {
          "id": 1212,
          "name": "The Number Of The Beast",
          "composer": "Steve Harris",
          "milliseconds": 294635,
          "bytes": 4718897,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1213,
          "name": "The Trooper",
          "composer": "Steve Harris",
          "milliseconds": 235311,
          "bytes": 3766272,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1214,
          "name": "Prowler",
          "composer": "Steve Harris",
          "milliseconds": 255634,
          "bytes": 4091904,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1215,
          "name": "Transylvania",
          "composer": "Steve Harris",
          "milliseconds": 265874,
          "bytes": 4255744,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1216,
          "name": "Remember Tomorrow",
          "composer": "Paul Di'Anno/Steve Harris",
          "milliseconds": 352731,
          "bytes": 5648438,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1217,
          "name": "Where Eagles Dare",
          "composer": "Steve Harris",
          "milliseconds": 289358,
          "bytes": 4630528,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1218,
          "name": "Sanctuary",
          "composer": "David Murray/Paul Di'Anno/Steve Harris",
          "milliseconds": 293250,
          "bytes": 4694016,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1219,
          "name": "Running Free",
          "composer": "Paul Di'Anno/Steve Harris",
          "milliseconds": 228937,
          "bytes": 3663872,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1220,
          "name": "Run To The Hilss",
          "composer": "Steve Harris",
          "milliseconds": 237557,
          "bytes": 3803136,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1221,
          "name": "2 Minutes To Midnight",
          "composer": "Adrian Smith/Bruce Dickinson",
          "milliseconds": 337423,
          "bytes": 5400576,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1222,
          "name": "Iron Maiden",
          "composer": "Steve Harris",
          "milliseconds": 324623,
          "bytes": 5195776,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1223,
          "name": "Hallowed Be Thy Name",
          "composer": "Steve Harris",
          "milliseconds": 471849,
          "bytes": 7550976,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        }
      ]
    },
    {
      "id": 96,
      "title": "A Real Live One",
      "artist": 90,
      "tracks": [
        {
          "id": 1224,
          "name": "Be Quick Or Be Dead",
          "composer": "Bruce Dickinson/Janick Gers",
          "milliseconds": 196911,
          "bytes": 3151872,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1225,
          "name": "From Here To Eternity",
          "composer": "Steve Harris",
          "milliseconds": 259866,
          "bytes": 4159488,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1226,
          "name": "Can I Play With Madness",
          "composer": "Adrian Smith/Bruce Dickinson/Steve Harris",
          "milliseconds": 282488,
          "bytes": 4521984,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1227,
          "name": "Wasting Love",
          "composer": "Bruce Dickinson/Janick Gers",
          "milliseconds": 347846,
          "bytes": 5566464,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1228,
          "name": "Tailgunner",
          "composer": "Bruce Dickinson/Steve Harris",
          "milliseconds": 249469,
          "bytes": 3993600,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1229,
          "name": "The Evil That Men Do",
          "composer": "Adrian Smith/Bruce Dickinson/Steve Harris",
          "milliseconds": 325929,
          "bytes": 5216256,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1230,
          "name": "Afraid To Shoot Strangers",
          "composer": "Steve Harris",
          "milliseconds": 407980,
          "bytes": 6529024,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1231,
          "name": "Bring Your Daughter... To The Slaughter",
          "composer": "Bruce Dickinson",
          "milliseconds": 317727,
          "bytes": 5085184,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1232,
          "name": "Heaven Can Wait",
          "composer": "Steve Harris",
          "milliseconds": 448574,
          "bytes": 7178240,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1233,
          "name": "The Clairvoyant",
          "composer": "Steve Harris",
          "milliseconds": 269871,
          "bytes": 4319232,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1234,
          "name": "Fear Of The Dark",
          "composer": "Steve Harris",
          "milliseconds": 431333,
          "bytes": 6906078,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        }
      ]
    },
    {
      "id": 285,
      "title": "A Soprano Inspired",
      "artist": 219,
      "tracks": [
        {
          "id": 3416,
          "name": "Ave Maria",
          "composer": "Franz Schubert",
          "milliseconds": 338243,
          "bytes": 5605648,
          "unit_price": 0.99,
          "media_type": "Protected AAC audio file",
          "genre": "Classical"
        }
      ]
    },
    {
      "id": 139,
      "title": "A TempestadeTempestade Ou O Livro Dos Dias",
      "artist": 99,
      "tracks": [
        {
          "id": 1671,
          "name": "Natália",
          "composer": "Renato Russo",
          "milliseconds": 235728,
          "bytes": 7640230,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1672,
          "name": "L'Avventura",
          "composer": "Renato Russo",
          "milliseconds": 278256,
          "bytes": 9165769,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1673,
          "name": "Música De Trabalho",
          "composer": "Renato Russo",
          "milliseconds": 260231,
          "bytes": 8590671,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1674,
          "name": "Longe Do Meu Lado",
          "composer": "Renato Russo - Marcelo Bonfá",
          "milliseconds": 266161,
          "bytes": 8655249,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1675,
          "name": "A Via Láctea",
          "composer": "Renato Russo",
          "milliseconds": 280084,
          "bytes": 9234879,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1676,
          "name": "Música Ambiente",
          "composer": "Renato Russo",
          "milliseconds": 247614,
          "bytes": 8234388,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1677,
          "name": "Aloha",
          "composer": "Renato Russo",
          "milliseconds": 325955,
          "bytes": 10793301,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1678,
          "name": "Soul Parsifal",
          "composer": "Renato Russo - Marisa Monte",
          "milliseconds": 295053,
          "bytes": 9853589,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1679,
          "name": "Dezesseis",
          "composer": "Renato Russo",
          "milliseconds": 323918,
          "bytes": 10573515,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1680,
          "name": "Mil Pedaços",
          "composer": "Renato Russo",
          "milliseconds": 203337,
          "bytes": 6643291,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1681,
          "name": "Leila",
          "composer": "Renato Russo",
          "milliseconds": 323056,
          "bytes": 10608239,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1682,
          "name": "1º De Julho",
          "composer": "Renato Russo",
          "milliseconds": 290298,
          "bytes": 9619257,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1683,
          "name": "Esperando Por Mim",
          "composer": "Renato Russo",
          "milliseconds": 261668,
          "bytes": 8844133,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1684,
          "name": "Quando Você Voltar",
          "composer": "Renato Russo",
          "milliseconds": 173897,
          "bytes": 5781046,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        },
        {
          "id": 1685,
          "name": "O Livro Dos Dias",
          "composer": "Renato Russo",
          "milliseconds": 257253,
          "bytes": 8570929,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Latin"
        }
      ]
    },
    {
      "id": 203,
      "title": "A-Sides",
      "artist": 132,
      "tracks": [
        {
          "id": 2506,
          "name": "Nothing To Say",
          "composer": "Chris Cornell/Kim Thayil",
          "milliseconds": 238027,
          "bytes": 7744833,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2507,
          "name": "Flower",
          "composer": "Chris Cornell/Kim Thayil",
          "milliseconds": 208822,
          "bytes": 6830732,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2508,
          "name": "Loud Love",
          "composer": "Chris Cornell",
          "milliseconds": 297456,
          "bytes": 9660953,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2509,
          "name": "Hands All Over",
          "composer": "Chris Cornell/Kim Thayil",
          "milliseconds": 362475,
          "bytes": 11893108,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2510,
          "name": "Get On The Snake",
          "composer": "Chris Cornell/Kim Thayil",
          "milliseconds": 225123,
          "bytes": 7313744,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2511,
          "name": "Jesus Christ Pose",
          "composer": "Ben Shepherd/Chris Cornell/Kim Thayil/Matt Cameron",
          "milliseconds": 352966,
          "bytes": 11739886,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2512,
          "name": "Outshined",
          "composer": "Chris Cornell",
          "milliseconds": 312476,
          "bytes": 10274629,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2513,
          "name": "Rusty Cage",
          "composer": "Chris Cornell",
          "milliseconds": 267728,
          "bytes": 8779485,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2514,
          "name": "Spoonman",
          "composer": "Chris Cornell",
          "milliseconds": 248476,
          "bytes": 8289906,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2515,
          "name": "The Day I Tried To Live",
          "composer": "Chris Cornell",
          "milliseconds": 321175,
          "bytes": 10507137,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2516,
          "name": "Black Hole Sun",
          "composer": "Soundgarden",
          "milliseconds": 320365,
          "bytes": 10425229,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2517,
          "name": "Fell On Black Days",
          "composer": "Chris Cornell",
          "milliseconds": 282331,
          "bytes": 9256082,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2518,
          "name": "Pretty Noose",
          "composer": "Chris Cornell",
          "milliseconds": 253570,
          "bytes": 8317931,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2519,
          "name": "Burden In My Hand",
          "composer": "Chris Cornell",
          "milliseconds": 292153,
          "bytes": 9659911,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2520,
          "name": "Blow Up The Outside World",
          "composer": "Chris Cornell",
          "milliseconds": 347898,
          "bytes": 11379527,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2521,
          "name": "Ty Cobb",
          "composer": "Ben Shepherd/Chris Cornell",
          "milliseconds": 188786,
          "bytes": 6233136,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 2522,
          "name": "Bleed Together",
          "composer": "Chris Cornell",
          "milliseconds": 232202,
          "bytes": 7597074,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        }
      ]
    },
    {
      "id": 160,
      "title": "Ace Of Spades",
      "artist": 106,
      "tracks": [
        {
          "id": 1942,
          "name": "Ace Of Spades",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 169926,
          "bytes": 5523552,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1943,
          "name": "Love Me Like A Reptile",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 203546,
          "bytes": 6616389,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1944,
          "name": "Shoot You In The Back",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 160026,
          "bytes": 5175327,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1945,
          "name": "Live To Win",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 217626,
          "bytes": 7102182,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1946,
          "name": "Fast And Loose",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 203337,
          "bytes": 6643350,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1947,
          "name": "(We Are) The Road Crew",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 192600,
          "bytes": 6283035,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1948,
          "name": "Fire Fire",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 164675,
          "bytes": 5416114,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1949,
          "name": "Jailbait",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 213916,
          "bytes": 6983609,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1950,
          "name": "Dance",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 158432,
          "bytes": 5155099,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1951,
          "name": "Bite The Bullet",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 98115,
          "bytes": 3195536,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1952,
          "name": "The Chase Is Better Than The Catch",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 258403,
          "bytes": 8393310,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1953,
          "name": "The Hammer",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 168071,
          "bytes": 5543267,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1954,
          "name": "Dirty Love",
          "composer": "Clarke/Kilmister/Taylor",
          "milliseconds": 176457,
          "bytes": 5805241,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1955,
          "name": "Please Don't Touch",
          "composer": "Heath/Robinson",
          "milliseconds": 169926,
          "bytes": 5557002,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        },
        {
          "id": 1956,
          "name": "Emergency",
          "composer": "Dufort/Johnson/McAuliffe/Williams",
          "milliseconds": 180427,
          "bytes": 5828728,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Metal"
        }
      ]
    }
  ]
}
```

#### Response when page not found (404)
```json
{
  "detail": "Page not found"
}
```

### Get all albums of an artist

#### Request
```sh
  curl -X 'GET' \
  'http://127.0.0.1:8000/api/artists/1/albums/' \
  -H 'accept: application/json'
```
#### Response when success
```json
{
  "pagination": {
    "total_items": 2,
    "total_pages": 1,
    "current_page": 1,
    "next_page": null,
    "previous_page": null,
    "page_size": 10
  },
  "results": [
    {
      "id": 1,
      "title": "For Those About To Rock We Salute You",
      "artist": 1,
      "tracks": [
        {
          "id": 1,
          "name": "For Those About To Rock (We Salute You)",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 343719,
          "bytes": 11170334,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 6,
          "name": "Put The Finger On You",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 205662,
          "bytes": 6713451,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 7,
          "name": "Let's Get It Up",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 233926,
          "bytes": 7636561,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 8,
          "name": "Inject The Venom",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 210834,
          "bytes": 6852860,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 9,
          "name": "Snowballed",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 203102,
          "bytes": 6599424,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 10,
          "name": "Evil Walks",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 263497,
          "bytes": 8611245,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 11,
          "name": "C.O.D.",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 199836,
          "bytes": 6566314,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 12,
          "name": "Breaking The Rules",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 263288,
          "bytes": 8596840,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 13,
          "name": "Night Of The Long Knives",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 205688,
          "bytes": 6706347,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 14,
          "name": "Spellbound",
          "composer": "Angus Young, Malcolm Young, Brian Johnson",
          "milliseconds": 270863,
          "bytes": 8817038,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        }
      ]
    },
    {
      "id": 4,
      "title": "Let There Be Rock",
      "artist": 1,
      "tracks": [
        {
          "id": 15,
          "name": "Go Down",
          "composer": "AC/DC",
          "milliseconds": 331180,
          "bytes": 10847611,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 16,
          "name": "Dog Eat Dog",
          "composer": "AC/DC",
          "milliseconds": 215196,
          "bytes": 7032162,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 17,
          "name": "Let There Be Rock",
          "composer": "AC/DC",
          "milliseconds": 366654,
          "bytes": 12021261,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 18,
          "name": "Bad Boy Boogie",
          "composer": "AC/DC",
          "milliseconds": 267728,
          "bytes": 8776140,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 19,
          "name": "Problem Child",
          "composer": "AC/DC",
          "milliseconds": 325041,
          "bytes": 10617116,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 20,
          "name": "Overdose",
          "composer": "AC/DC",
          "milliseconds": 369319,
          "bytes": 12066294,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 21,
          "name": "Hell Ain't A Bad Place To Be",
          "composer": "AC/DC",
          "milliseconds": 254380,
          "bytes": 8331286,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        },
        {
          "id": 22,
          "name": "Whole Lotta Rosie",
          "composer": "AC/DC",
          "milliseconds": 323761,
          "bytes": 10547154,
          "unit_price": 0.99,
          "media_type": "MPEG audio file",
          "genre": "Rock"
        }
      ]
    }
  ]
}
```

#### Response when artist doesn't exist (404)
```json
{
  "detail": "Artist not found"
}
```
#### Response when artist_id is invalid (400)
```json
[
  "Id must be a positive integer"
]
```
### Get all tracks of an album

#### Request
```sh
  curl -X 'GET' \
  'http://127.0.0.1:8000/api/albums/1/tracks/' \
  -H 'accept: application/json'
```

#### Response when success (200)
```json
{
  "id": 1,
  "title": "For Those About To Rock We Salute You",
  "artist": 1,
  "tracks": [
    {
      "id": 1,
      "name": "For Those About To Rock (We Salute You)",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 343719,
      "bytes": 11170334,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 6,
      "name": "Put The Finger On You",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 205662,
      "bytes": 6713451,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 7,
      "name": "Let's Get It Up",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 233926,
      "bytes": 7636561,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 8,
      "name": "Inject The Venom",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 210834,
      "bytes": 6852860,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 9,
      "name": "Snowballed",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 203102,
      "bytes": 6599424,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 10,
      "name": "Evil Walks",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 263497,
      "bytes": 8611245,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 11,
      "name": "C.O.D.",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 199836,
      "bytes": 6566314,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 12,
      "name": "Breaking The Rules",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 263288,
      "bytes": 8596840,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 13,
      "name": "Night Of The Long Knives",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 205688,
      "bytes": 6706347,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    },
    {
      "id": 14,
      "name": "Spellbound",
      "composer": "Angus Young, Malcolm Young, Brian Johnson",
      "milliseconds": 270863,
      "bytes": 8817038,
      "unit_price": 0.99,
      "media_type": "MPEG audio file",
      "genre": "Rock"
    }
  ]
}
```

#### Response when album doesn't exist (404)
```json
{
  "detail": "Album not found"
}
```
#### Response when album_id is an invalid number (400)
```json
[
  "Id must be a positive integer"
]
```
### Get all albums summarize
#### Request
```sh
  curl -X 'GET' \
  'http://127.0.0.1:8000/api/albums/summary/' \
  -H 'accept: application/json'
```

#### Response when success (200)
```json
{
  "pagination": {
    "total_items": 347,
    "total_pages": 35,
    "current_page": 1,
    "next_page": "http://127.0.0.1:8000/api/albums/summary/?page=2",
    "previous_page": null,
    "page_size": 10
  },
  "results": [
    {
      "id": 156,
      "title": "...And Justice For All",
      "artist_name": "Metallica",
      "total_tracks": 9
    },
    {
      "id": 257,
      "title": "20th Century Masters - The Millennium Collection: The Best of Scorpions",
      "artist_name": "Scorpions",
      "total_tracks": 12
    },
    {
      "id": 296,
      "title": "A Copland Celebration, Vol. I",
      "artist_name": "Aaron Copland & London Symphony Orchestra",
      "total_tracks": 1
    },
    {
      "id": 94,
      "title": "A Matter of Life and Death",
      "artist_name": "Iron Maiden",
      "total_tracks": 11
    },
    {
      "id": 95,
      "title": "A Real Dead One",
      "artist_name": "Iron Maiden",
      "total_tracks": 12
    },
    {
      "id": 96,
      "title": "A Real Live One",
      "artist_name": "Iron Maiden",
      "total_tracks": 11
    },
    {
      "id": 285,
      "title": "A Soprano Inspired",
      "artist_name": "Britten Sinfonia, Ivor Bolton & Lesley Garrett",
      "total_tracks": 1
    },
    {
      "id": 139,
      "title": "A TempestadeTempestade Ou O Livro Dos Dias",
      "artist_name": "Legião Urbana",
      "total_tracks": 15
    },
    {
      "id": 203,
      "title": "A-Sides",
      "artist_name": "Soundgarden",
      "total_tracks": 17
    },
    {
      "id": 160,
      "title": "Ace Of Spades",
      "artist_name": "Motörhead",
      "total_tracks": 15
    }
  ]
}
```

#### Response when page doesn't exist
```json
{
  "detail": "Page not found"
}
```