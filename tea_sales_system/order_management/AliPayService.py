import json

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest


class AlipayService:
    def __init__(self):
        self.client_config = AlipayClientConfig()
        self.client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
        self.client_config.app_id = '2021004199682528'
        self.client_config.app_private_key = 'MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCP1ud4dv9WWa6R7sbgMX1ZxRL0AgOwihTcKmrczcyLWRY5j/sJYi+jhnuSX1T4dCQs77yC3yiBwpFoHVnuy/hcRNipp4H+wScT0zKIosP0qRkYODspQTsli2CsarJ3G4ClC06BtLk4foWSHKmLFqOUOkV48w5RU8lXEMSSIMe1r3Fn4GpsirKqJNTbQWn5fKhJj67e8iEd8R63wMgt9hUJNd/eoyQ8OmsKCS4JW1VkxCYS1U17kkOUzDDfPOfl7ollqqrrqMYPLOOfEPkm6KPHDe4r4kmEQeVEqAyW4crbAsSLVU92ySvlGnAp/1UiPnQWt4vW2QPiS15vMYJP9YqbAgMBAAECggEAT4jXKOczvP2N56eOVD1JQLAWENJkU+OmMS9LM5igN5UlEuMoPkIKcXNVNNR92Xvu3OIa7IqUjVuWp2lDZyVlyS9QVk8HNGR9RRsM4DyP+eLeu2OsYt1s5Q+yfuPolq+gbKJZ4KKboD9lgCtVHFGCVd36uCw9iH653+inqN1zUGRA7dgZ7+yZt7YJxLqRY3i52BrGg/T19X+Kj89fbDX5NwFw9TVx4oaU4jlSA3CdVPtTUobPhwSAJKf8OvA0BpZszIQm3JAUKtU/eMOQi0/FfbIFKi7eek2kB6GUo0qf75sJ3otYE0SNYEbM5whspTIa/MePdbDoaRfLnlCr5KeHgQKBgQDkgPV0a4yGpl5QeLuSaghgOeRIQlISBeRiwBCaFOyLKPilJtCPwHnuCH4Zae426z6TPbINdg1jaEhcaaNiNjvXbbEYHs4PtBjBvpIFMeJMnDI2xpun0DUSx45GFsBQwkD9dk8eLBQWcoykXYYvYqN5xn59P8N9D/JNrGdgRo2ZoQKBgQChJd5YcGxLYOZzsXyEJMCqrKof9mrkkB60p0R3p8VUJrkjq1utpaP7A+a/I1exvf/e1R9kfT8V07NIR+dvkbMJ4rfr1b+0/jMvcMWk8U6BO4/d6MljoI0uHoLSPELayu21Nk2YXxADJRH6GZtwu5ZmFOudgigelEruf2vdMRkSuwKBgGfMFLOfryPzKuCPF1V5CPj9Ey+nwLQjLQ2WhXQYkSLdp6UNrqu+GSUBgpZ0whr8XV5xJhJrT8WaN1STP/56+E/xqgJ069HCU4Se1qG5eTynrz+mlEp0j8dKEtzPtOh6dR8twN7J0w4nVq/LNAsOWYgVnJu0fU6wEbcq24KmSehBAoGAan6KF8wD5TSeVyqd7P4UzTXaH9FLBs0vXZeEqcaXo2sLwsTFi1YBrir/3KTQmUfExk/1tQUIIbaLrmLGUXbp6MiJXzMcw9GRpfJSyxQlG0ZvZukl3c8GPcowDhuA2vJscOr4EJASFuHypWMy1CdD1yZQJwES3lKFymMutzhxJ20CgYA/ZKggijr9EAfCsVFt1tzjolONimi9hIS5+SEvcfLD6tjfKz+AqKmHOsT4/qmxzaIrT3q7N0wDZ3mfh48c5fw0bx2+iqlGbOb3DtBnqrAIjRi8UZiv1/L6P/LFNaZLOXf0/H5LECgQGhMp0JLb7xzJnmLifhBDFIlYH9Lyv69gcw=='
        self.client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAj9bneHb/Vlmuke7G4DF9WcUS9AIDsIoU3Cpq3M3Mi1kWOY/7CWIvo4Z7kl9U+HQkLO+8gt8ogcKRaB1Z7sv4XETYqaeB/sEnE9MyiKLD9KkZGDg7KUE7JYtgrGqydxuApQtOgbS5OH6FkhypixajlDpFePMOUVPJVxDEkiDHta9xZ+BqbIqyqiTU20Fp+XyoSY+u3vIhHfEet8DILfYVCTXf3qMkPDprCgkuCVtVZMQmEtVNe5JDlMww3zzn5e6JZaqq66jGDyzjnxD5Juijxw3uK+JJhEHlRKgMluHK2wLEi1VPdskr5RpwKf9VIj50FreL1tkD4ktebzGCT/WKmwIDAQAB'
        self.client = DefaultAlipayClient(alipay_client_config=self.client_config)

    def generate_payment_url(self, order_id, amount):

        request = AlipayTradePagePayRequest()
        # 构造字典并转换为 JSON 字符串
        request.biz_content = {
            "out_trade_no": str(order_id),
            "total_amount": f"{float(amount):.2f}",
            "subject": f"Tea Order {order_id}",
            "product_code": "FAST_INSTANT_TRADE_PAY",
        }
        print("Request Biz Content (JSON):", request.biz_content)

        try:
            # 调用支付宝接口生成支付链接
            result = self.client.page_execute(request, http_method="GET")
            print("Generated Payment URL:", result)  # 调试日志
            return result
        except Exception as e:
            print(f"Error generating payment URL with order_id={order_id}, amount={amount}: {e}")
            print("Request Biz Content:", request.biz_content)
            raise
