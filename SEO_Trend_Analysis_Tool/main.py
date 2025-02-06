from modules.trend_crawler import get_trend_data
from modules.seo_analysis import analyze_seo_keywords
from modules.report_generator import generate_report
from modules.notifications import send_slack_message

def main():
    print("🚀 트렌드 키워드 크롤링 시작...")
    get_trend_data()  # 트렌드 키워드 크롤링

    print("📊 SEO 분석 실행 중...")
    analyze_seo_keywords()  # SEO 분석 실행

    print("📝 보고서 생성 중...")
    generate_report()  # 보고서 생성

    print("🔔 알림 전송 중...")
    send_slack_message("📊 SEO 분석 보고서가 생성되었습니다! 🚀")

    print("✅ 모든 작업이 완료되었습니다!")

if __name__ == "__main__":
    main()