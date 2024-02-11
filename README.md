# Deposit Test Task

## Task details 

Create a REST API service for deposit calculation

### Example of request
```json
{
    "date": "31.01.2021",
    "periods": 3,
    "amount": 10000,
    "rate": 6,
}
```

| Name | Type | Validation | Description |
| :------ | :------ | :------ | :------ |
| date | String | Format - dd.mm.YYY | The date of request |
| periods | Integer | from 1 to 60 | Amount of months for deposit |
| amount | Integer | from 10 000 to 3 000 000 | Amount of deposit |
| rate | Float | from 1.00 to 8.00 | interest on deposit |

### Results examples

#### If data validation passed

* valid response with status 200 
    ```json
    {
        "2021-01-31":10050,
        "2021-02-28":10100.25,
        "2021-03-31":10150.75,
    }
    ```
#### If data validation wasn't passed
* valid response with status code 400
    ```json
    {
        "error": "Error descripton"
    }
    ```

### Additional requirements
1. Language - `Python/Go/Rust`
2. Coverage by unit-tests - 80% and higher
3. Create Dockerfile for app building

## Build and run

### Simple service start 
Run start script
You can pass `port` as positional argument to redefine port outside the container  
```bash
./scripts/docker_build_run.sh "port" # port - optional (default: 8000)
``` 

#### Script will:
1. Check if docker running. Stops script if not.
2. Build image with default name `deposit_service:latest`
    * In current realization previously builded images will become dangling
3. Run tests. Stops script if one ore more not passed.
4. Ran container and start app.


