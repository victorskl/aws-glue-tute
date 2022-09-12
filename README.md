# AWS Glue tute

```
docker compose up -d
docker compose ps
docker compose logs -f
(ctrl+c)
```
- Go to http://localhost:8888

### Makefile

Alternatively, use `make` based dev workflow

```
make up
make ps
make logs
make start
make enter
make down
...
```
- Look [Makefile](Makefile) targets for more dev routines

## Quickstart

```
make enter
cd jupyter_workspace
spark-submit quickstart.py
```

## JupyterLab

- Go to [JupyterLab UI](http://localhost:8888/lab), `File > New > Terminal`

```
jupyter kernelspec list
```

```
pyspark
>>> exit()
```

### Sample ETL

```
cd jupyter_workspace/sample_etl
spark-submit sample.py
pytest
```

### AWS

- While at JupyterLab Terminal, try as follows to test AWS account setup works.

```
aws sts get-caller-identity
aws s3 ls s3://awsglue-datasets/examples/us-legislators/all/persons.json
```

- If you get any error from above AWS commands, probably revisit [docker-compose.yml](docker-compose.yml) to check that you do have `AWS_PROFILE` called `dev` and, set the right `AWS_REGION` to your case.

- You can use [docker-compose.override.arm64.yml](docker-compose.override.arm64.yml) to override settings specific to your case.


### Quickstart Notebook

At [JupyterLab UI](http://localhost:8888/lab)

- Menu: `File > Open from Path...` and, enter `quickstart.ipynb` when prompt.
- Menu: `Kernel > Change Kernel...` and, select `PySpark` kernel from dropdown list.
