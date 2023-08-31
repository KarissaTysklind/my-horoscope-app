resource "aws_s3_bucket" "horoscope_lambda_function" {
  bucket = var.lambda_bucket_name
}

data "archive_file" "horoscope_function" {
  type        = "zip"
  source_file = "${path.module}/lambda/python/horoscope.py"
  output_path = "${path.module}/lambda/zip/horoscope.zip"
}

resource "aws_s3_object" "horoscope_function" {
  depends_on = [data.archive_file.horoscope_function]
  bucket     = aws_s3_bucket.horoscope_lambda_function.id
  key        = "horoscope.zip"
  source     = data.archive_file.horoscope_function.output_path
  etag       = filemd5(data.archive_file.horoscope_function.output_path)
}

resource "aws_lambda_function" "horoscope" {
  function_name = "Horoscope"
  s3_bucket     = aws_s3_bucket.horoscope_lambda_function.id
  s3_key        = aws_s3_object.horoscope_function.key
  runtime       = "python3.11"
  handler       = "horoscope.lambda_handler"

  source_code_hash = data.archive_file.horoscope_function.output_base64sha256

  role = aws_iam_role.horoscope_lambda.arn
}