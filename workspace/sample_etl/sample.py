import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions


class GluePythonSample:
    def __init__(self):
        params = []
        if '--JOB_NAME' in sys.argv:
            params.append('JOB_NAME')
        args = getResolvedOptions(sys.argv, params)

        self.context = GlueContext(SparkContext.getOrCreate())
        self.job = Job(self.context)

        if 'JOB_NAME' in args:
            job_name = args['JOB_NAME']
        else:
            job_name = "test"
        self.job.init(job_name, args)

    def run(self):
        # dyf = read_json(self.context, "s3://awsglue-datasets/examples/us-legislators/all/persons.json")
        dyf = read_json(self.context, "persons_subset_head_10.ndjson")
        dyf.printSchema()

        self.job.commit()


def read_json(glue_context, path):
    dynamic_frame = glue_context.create_dynamic_frame.from_options(
        connection_type='s3',
        connection_options={
            'paths': [path],
            'recurse': True
        },
        format='json'
    )
    return dynamic_frame


if __name__ == '__main__':
    GluePythonSample().run()
