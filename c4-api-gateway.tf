resource "aws_api_gateway_rest_api" "horoscope" {
  name = var.api_horoscope_name
  endpoint_configuration {
    types = [var.endpoint_configuration]
  }
}

resource "aws_api_gateway_method" "horoscope_POST" {
  rest_api_id = aws_api_gateway_rest_api.horoscope.id
  resource_id = aws_api_gateway_rest_api.horoscope.root_resource_id
  http_method = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "horoscope_POST" {
  rest_api_id = aws_api_gateway_rest_api.horoscope.id
  resource_id = aws_api_gateway_rest_api.horoscope.root_resource_id
  http_method = "POST"
  integration_http_method = "POST"
  type        = "AWS"
  uri         = aws_lambda_function.horoscope.invoke_arn
  content_handling = "CONVERT_TO_TEXT"
}

resource "aws_api_gateway_method_response" "horoscope_POST" {
    rest_api_id = aws_api_gateway_rest_api.horoscope.id
    resource_id = aws_api_gateway_rest_api.horoscope.root_resource_id
    http_method = aws_api_gateway_method.horoscope_POST.http_method
    status_code = "200"
    response_models = {
      "application/json" = "Empty"
    }
}

resource "aws_api_gateway_integration_response" "horoscope_POST" {
    rest_api_id = aws_api_gateway_rest_api.horoscope.id
    resource_id = aws_api_gateway_rest_api.horoscope.root_resource_id
    http_method = aws_api_gateway_method.horoscope_POST.http_method
    status_code = "200"
}

resource "aws_api_gateway_deployment" "horoscope_dev" {
  rest_api_id = aws_api_gateway_rest_api.horoscope.id
  stage_name  = var.stage_name
}