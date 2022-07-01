| POST         |           |     |   |   |
|--------------|-----------|-----|---|---|
| author       | User      | FK  |   |   |
| title        | CharField |     |   |   |
| content      | TextField |     |   |   |
| created_date | DateTime  |     |   |   |
| updated_date | DateTime  |     |   |   |
| likes        | User      | M2M |   |   |


| COMMENT      |      |     |   |   |
|--------------|------|-----|---|---|
| post         | Post | FK  |   |   |
| author       | User | FK  |   |   |
| content      |      |     |   |   |
| created_date |      |     |   |   |
| updated_date |      |     |   |   |
| likes        | User | M2M |   |   |
