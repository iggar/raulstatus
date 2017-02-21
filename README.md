# Simple Python Flask API for the Raul Hackerspace presence control #


### Running locally

To run locally you will need `python` and the Flask module (`pip install flask`)
Once you install the requirements, simply run `python app.py`

### Running on Docker

After installing [Docker](https://www.docker.com/products/overview), first build the image using the following command:

```bash
docker build -t raul-status:latest .
```

Then run the Docker container:

```bash
docker run -p 5000:5000 raul-status
```

To run in daemon mode instead, add `-d`:

```bash
docker run -d -p 5000:5000 raul-status
```

### Accessing the API

#### Current status

The current status will be accessible in JSON format at endpoint `/status` with information of date-time of the last event, open status (true|false) and the user:

http://localhost:5000/status


Alternatively, using curl:

```bash
curl -L -XGET 'http://localhost:5000/status'
```


#### Check-in

The `/checkin` endpoint will change the current status to open and update the date-time stamp. Optionally a user can be provided. If not provided, "Raul Seixas" will be assumed instead. It will return HTTP status 200 and the updated space status.

```bash
$ curl -H "Content-Type: application/json" -XPOST 'http://localhost:5000/status/checkin' -d '{"user": "Igor Garcia"}'
{
  "date-time": "2017-02-21T23:25:09.590457", 
  "open": true, 
  "user": "Igor Garcia"
}
```


#### Check-out

The `/checkout` endpoint will change the current status to closed and update the date-time stamp. Optionally a user can be provided. If not provided, "Raul Seixas" will be assumed instead. It will return HTTP status 200 and the updated space status.

```bash
$ curl -H "Content-Type: application/json" -XPOST 'http://localhost:5000/status/checkout' -d '{"user": "Rafael Gomex"}'
{
  "date-time": "2017-02-21T23:25:36.583668", 
  "open": false, 
  "user": "Rafael Gomex"
}
```

### Testing with a HTML widget

There's a sample html file `widget.htm` that will try and load the correct image depending on the current status. You must adjust the value on the source code to match your server and port parameters.

With the server running, simply open the html file in any browser. You can then post to `/checkin` and `/checkout` and refresh the page to observe the image changing.


