# AWS Glue tute

Using Docker Container Image published at https://gallery.ecr.aws/glue/

- https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html#develop-local-docker-image
- https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/

## Quickstart ETL

```
docker compose up -d
docker compose ps
docker compose logs -f
(ctrl+c)
```

### Console

- Login to glue container terminal 
```
docker compose exec -it glue bash
```

- Navigate to workspace folder and run Spark job script
```
cd jupyter_workspace/quickstart_etl
spark-submit quickstart.py
```

### Notebook

At JupyterLab UI (http://localhost:8888/lab)

- Menu: `File > Open from Path...` and, enter `quickstart.ipynb` when prompt.
- Menu: `Kernel > Change Kernel...` and, select `PySpark` kernel from dropdown list.

## Sample ETL

This `sample_etl` folder contains Glue job script and, run it as headless scenario. 

```
cd jupyter_workspace/sample_etl
spark-submit sample.py
pytest
```

## Other Notes

### AWS

- While at JupyterLab Terminal, try as follows to test AWS account setup works.

```
aws sts get-caller-identity
aws s3 ls s3://awsglue-datasets/examples/us-legislators/all/persons.json
```

- If you get any error from above AWS commands, probably revisit Docker [compose.yml](compose.yml) to check that you do have `AWS_PROFILE` called `dev` and, set the right `AWS_REGION` to your case.

- You can use [compose override](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) `compose.override.yml` file that suit to your case.

### PySpark

- Go to JupyterLab UI (http://localhost:8888/lab)
- `File > New > Terminal`

```
jupyter kernelspec list
```

```
pyspark
>>> exit()
```

### PyCharm

_Developing scripts using development endpoints_

- https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint.html
- https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-pycharm.html
- https://www.jetbrains.com/help/pycharm/big-data-tools-aws-glue.html
