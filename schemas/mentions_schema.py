from pyspark.sql.types import StructType, StructField, LongType, StringType

# mentions schema
mentions_schema = StructType([
    StructField('_id', StringType()),
    StructField('created_at', StringType()),
    StructField('text', StringType()),
    StructField('id', LongType()),
    StructField('in_reply_to_status_id', StringType()),
    StructField('user_id', LongType()),
    StructField('user_name', StringType()),
    StructField('user_screen_name', StringType()),
    StructField('user_description', StringType()),
    StructField('user_profile_image_url', StringType()),
    StructField('user_profile_image_url_https', StringType()),
    StructField('extended_tweet_full_text', StringType()),
    StructField('classification', StringType()),
])