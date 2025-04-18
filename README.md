# NFLRecordsWebScrapper

This script pulls data from USA Today's NFL player arrests database and stores it in a JSON file for analysis.

From there, it filters and analyzes violent charges to provide meaningful insight into arrest trends.

---

## Web Scrapper

This goes to the website:  
🔗 https://databases.usatoday.com/nfl-arrests  
and grabs all of the data from the paginated arrest tables, storing them in an `arrest_records.json` file.

---

## Data Analysis

This runs in **O(n)** time. It categorizes records by violent keywords and outputs the number of matching charges.

---

### Output of the Data Analysis

| Violent Term       | Record Count |
|--------------------|--------------|
| Abuse              | 5            |
| Animal cruelty     | 3            |
| Assault            | 109          |
| Battery            | 35           |
| Bomb threat        | 1            |
| Burglary           | 3            |
| Child abuse        | 3            |
| Dogfighting        | 1            |
| Gun                | 82           |
| Injury             | 1            |
| Menacing           | 2            |
| Murder             | 5            |
| Rape               | 1            |
| Resisting arrest   | 22           |
| Robbery            | 3            |
| Stalking           | 2            |
| Violence           | 142          |
| Weapon             | 3            |

**Total records:** 1,092  
**Total violent records:** 423  
**Percentage violent:** 38.74%
