from alipay import AliPay

alipay_public_key_string='''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwcwFN4yAlGqZzJOF8aFqLt4c6Fcy5EmLtr7oI5NSQG1BPaqUsHgDElref4dE2t15W0LCU7ZKYPuS9JXXlDlVUkJ0zVkIw3j/mpkB5+7bG6gbcZAMhzeXCgOgwBZzIg8licQpKjamVWOmGBxhMggEJLBM4k3v1zXPdai26a3DPvtSy/dJ7iTVFVxoSVQqJoIKo07eXZ28aTSC5dgbHPa+2OUqsJvT4Zbwt8flBYSTCHWGqVBU1WwBQtmIwRdfJjM9U7Jn5BUdaegPHfCMCE5KxwGd87RiZrTw19dKYDf7ObXq8x8SP43fhnoVrOUH7cWqNlJZktPPyVB37ubNar6bmQIDAQAB
-----END PUBLIC KEY-----'''

alipay_private_key_string='''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwcwFN4yAlGqZzJOF8aFqLt4c6Fcy5EmLtr7oI5NSQG1BPaqUsHgDElref4dE2t15W0LCU7ZKYPuS9JXXlDlVUkJ0zVkIw3j/mpkB5+7bG6gbcZAMhzeXCgOgwBZzIg8licQpKjamVWOmGBxhMggEJLBM4k3v1zXPdai26a3DPvtSy/dJ7iTVFVxoSVQqJoIKo07eXZ28aTSC5dgbHPa+2OUqsJvT4Zbwt8flBYSTCHWGqVBU1WwBQtmIwRdfJjM9U7Jn5BUdaegPHfCMCE5KxwGd87RiZrTw19dKYDf7ObXq8x8SP43fhnoVrOUH7cWqNlJZktPPyVB37ubNar6bmQIDAQABAoIBAQCws8IeADJNIVXSvsBmrXMQAN4Cy19P3+9QVYl8xps8u2G9RIgGz6adWdV+Gmyh00cP+zMM+S2geEJqWSYTtKMjOg0eH4xqDy2gXNrsC1IlSYacaWfC8uD49I3iF5Yq+/ySPRX7s5C+UvnjCh1lbQG6IjY4Mi/53sqm0YrWTuWzygJ469HlkHHVrpfixu8r2ONzsAXdSVRFMoXf22JUZwV4jm7AfX0DnD0wWyuteeNmInGzvb4giDkLeyTX4yzgFovaUehEGEpZaOATMz1MWfYSFIzBJLTxhq5Yui3qtVBMSdWCQv1hPa0A8n2s0hZY8jSg/YKZMTm3e/EPEdgDiSXxAoGBAP/8WYz4HOsrEhkJJUZz7ltdLTKn2sLGuyUn74X0d8XLCcs6MfgiIy+1SgcaER9YuCA2Q6RNigo1xvC3UsfV9IM1D52TWvR9JW2BSacjwJlooQWipLW7DOwrRzY3n0ROGDYeUbQx4tjRvrsjmrkBN1L7yMDGPbB0KOigJS/x1DgnAoGBAMHOyKcSbtZWHEHpqrD2SEmnJIafDzVGhoxKhijBKHGB4zlsqXHotg0TUWo/HwAM3jeOE3NPW16OUHAHZy1yvjRiQ/sccRjcXTZE/DskTcxS76d+AO2kW5uYsxO1kEDg2GQEC4XB4MX4gh/HV47qU2+z7BkwtwMA0cXbXWN1uSY/AoGBAOtxuRP1qPOL++tXBBfWzWbvPoEW7hi0HLFCGAZHIlqkMu/fKNKm42IgBmSdzx3bxg6qmnBmeQ6HA+GnW9Y9rdV4WlJ+k+vHp0Me5RV7xsvS9jdurrwPvQUDkU4GvtBeW9p67H8mWxU9ZYZOayK6QZ5rwuu76kV/sZi0oz+D18OFAoGAJCYtxvvpMJFfM+whqmBFm3dRmMqSS52b+w7rdy6QHJvdhhh+goCldErmJKshXSEJUdNuTVO/9yMUXdEDrbZ5Q8wQYgYsEjcIK9cyNNXQrQvLJ7KY+bpuW9dfj42OGovV0NHwVEKValev7b2A12ddqLgmkYxElorQldcU1DhhEIECgYBxlMklF3Ij0nTyIRswmGwxP6B7zH+wKnCmWzzNSJugKu0P5MqP45WxfIJnmPNPlF19VD0MKa4P+/Ukp1Q5QviKS+ma38dtsFKNuEZqvZnV2vUAlPjXevn9Lxkqu5TIL9pA/lgtzkv0FnGmvfknD7nWZliLCgA0tPiityzE+E7xRA==
-----END RSA PRIVATE KEY-----'''

#实例化支付
alipay=AliPay(
    appid='2016101200667746',
    app_notify_url=None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type='RSA2'
)
#实例化订单

order_string=alipay.api_alipay_trade_page_pay(
    out_trade_no='201909111525',#订单号，唯一
    total_amount=str(1888),#支付金额
    subject='快活林',#支付主题
    return_url=None,
    notify_url=None,
)

#拼接收款地址
result="https://openapi.alipaydev.com/gateway.do?"+order_string

print(result)