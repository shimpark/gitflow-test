from playwright.sync_api import sync_playwright

def generate_pdf(url, output_path):
    with sync_playwright() as p:
        # Chromium 브라우저를 실행합니다.
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # URL로 이동하여 페이지를 로드합니다.
        page.goto(url, wait_until='networkidle')

        # 추가 대기 시간 (3초) - 페이지가 완전히 로드될 때까지 기다림
        page.wait_for_timeout(1500)  # 1000 밀리초 = 1초


        # 페이지를 PDF로 저장합니다.
        # 페이지를 가로 방향으로 PDF로 저장합니다.
        page.pdf(
            path=output_path, 
            format="A4", 
            landscape=True,  # 가로 방향 설정
            margin={'top': '0.5in', 'bottom': '0.5in', 'left': '0.5in', 'right': '0.5in'}  # 여백 설정
        )

        print(f"PDF 생성 완료: {output_path}")

        # 브라우저를 닫습니다.
        browser.close()

# 사용 예시
url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2'
output_path = '1. EC2.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/20-preq'
output_path = '1-1. EC2_워크샵 시작 전 준비 사항.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/20-preq/100-account'
output_path = '1-1-1. EC2_워크샵 시작_AWS계정으로시작.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/20-preq/300-setting'
output_path = '1-1-2. EC2_워크샵 시작_추가설정하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/30-vpc'
output_path = '1-2. EC2_네트워크 구성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/30-vpc/100-create-vpc'
output_path = '1-2-1. EC2_네트워크 구성하기_VPC 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/30-vpc/200-create-subnet'
output_path = '1-2-2. EC2_네트워크 구성하기_추가 서브넷 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/30-vpc/300-set-route-table'
output_path = '1-2-3. EC2_네트워크 구성하기_라우팅 테이블 편집하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/30-vpc/400-create-sg'
output_path = '1-2-3. EC2_네트워크 구성하기_보안 그룹 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/40-ec2'
output_path = '1-3. EC2_웹 서버 생성하기.pdf'
generate_pdf(url, output_path)


url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/40-ec2/100-create-ec2'
output_path = '1-3-1. EC2_웹 서버 생성하기_웹 서버 인스턴스 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/40-ec2/200-create-ami'
output_path = '1-3-2. EC2_웹 서버 생성하기_AMI 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/40-ec2/300-create-ami-ec2'
output_path = '1-3-3. EC2_웹 서버 생성하기_AMI 기반 인스턴스 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/50-elb'
output_path = '1-4. EC2_로드밸런서 구성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/50-elb/100-create-elb'
output_path = '1-4-1. EC2_로드밸런서 구성하기_로드밸런서 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/60-additional'
output_path = '1-5. EC2_(옵션)추가실습.pdf'
generate_pdf(url, output_path)


url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/60-additional/100-cloudwatch-alarm'
output_path = '1-5-1. EC2_(옵션)추가실습_모니터링.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/60-additional/200-auto-scaling'
output_path = '1-5-2. EC2_(옵션)추가실습_오토스케일링.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/60-additional/300-static-web'
output_path = '1-5-3. EC2_(옵션)추가실습_정적 웹 사이트 호스팅.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/70-cleanup'
output_path = '1-6. EC2_실습 리소스 정리.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/70-cleanup/100-clean-up'
output_path = '1-6-1. EC2_실습 리소스 정리_세션실습삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/ec2/70-cleanup/200-clean-up'
output_path = '1-6-2. EC2_실습 리소스 정리_추가실습삭제.pdf'
generate_pdf(url, output_path)


url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless'
output_path = '2. Serverless.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/100-preq'
output_path = '2-1. Serverless_워크샵 시작 전 준비 사항.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/100-preq/100-setting'
output_path = '2-1-1. Serverless_워크샵 시작 전 준비 사항_언어와 리전 설정하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/100-preq/200-account'
output_path = '2-1-1. Serverless_워크샵 시작 전 준비 사항_AWS 계정으로 시작.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/110-dynamodb'
output_path = '2-2. Serverless_Dynamodb Table 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/110-dynamodb/100-create-dynamodb'
output_path = '2-2-1. Serverless_Dynamodb Table 생성하기_DynamoDB 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/120-lambda'
output_path = '2-3. Serverless_Lambda로 앱서버 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/120-lambda/100-create-api-service-lambda'
output_path = '2-3-1. Serverless_Lambda로 앱서버 생성하기_Lambda 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/130-apigateway'
output_path = '2-4. Serverless_API Gateway 구성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/130-apigateway/100-create-apigateway'
output_path = '2-4-1. Serverless_API Gateway 구성하기_API Gateway 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/130-apigateway/200-add-apigateway'
output_path = '2-4-2. Serverless_API Gateway 구성하기_API Gateway 추가 설정.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/140-s3'
output_path = '2-5. Serverless_S3로 웹서버 기능 사용하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/140-s3/100-create-bucket'
output_path = '2-5-1. Serverless_S3로 웹서버 기능 사용하기_S3 Bucket 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/140-s3/200-static-website-hosting'
output_path = '2-5-2. Serverless_S3로 웹서버 기능 사용하기_S3 정적 웹사이트 호스팅 기능 활성화하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/150-cleanup'
output_path = '2-6. Serverless_실습 리소스 정리.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/150-cleanup/100-clean-up'
output_path = '2-6-1. Serverless_실습 리소스 정리_세션 실습 자원 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq'
output_path = '2-7. Serverless_FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/100-account-faq'
output_path = '2-7-1. Serverless_FAQ_계정 생성 FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/200-workshop-faq'
output_path = '2-7-2. Serverless_FAQ_실습 환경 FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/300-network-faq'
output_path = '2-7-1. Serverless_FAQ_네트워크 FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/400-webserver-faq'
output_path = '2-7-1. Serverless_FAQ_웹 서버 FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/500-lb-faq'
output_path = '2-7-1. Serverless_FAQ_로드 밸런서 FAQ.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/600420b7-5c4c-498f-9b80-bc7798963ba3/ko-KR/serverless/900-faq/600-resource-faq'
output_path = '2-7-1. Serverless_FAQ_실습 리소스 정리 FAQ.pdf'
generate_pdf(url, output_path)






