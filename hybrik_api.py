# HybrIK 분석 모듈 샘플 (실제 모델 연동은 추후 추가)
def analyze_image(image_np):
    # 여기에 HybrIK 모델을 로딩하고 분석하는 코드를 추가 예정
    # 현재는 모의 결과 반환
    return {
        "message": "우측 어깨 상승, 좌측 기울기 보임",
        "score": 4.2,
        "shoulder_diff": 0.038
    }
