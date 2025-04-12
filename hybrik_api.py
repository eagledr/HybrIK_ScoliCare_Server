def analyze_image(image_np):
    # 실제로는 여기에서 HybrIK 모델을 로딩하고 관절 좌표 추출 및 분석 진행
    # 지금은 목업 결과 예시 (추후 모델 연동 시 실제 결과로 대체)

    # 예시 분석 로직 (숫자나 메시지는 임시값입니다)
    result = {
        "message": "우측 어깨 상승, 좌측 기울기 보임",
        "score": 4.2,
        "shoulder_diff": 0.038,
        "pelvis_diff": 0.025,         # 골반 높이 차이
        "back_hump": True,            # 등 험프 감지
        "lumbar_curve": "전만 과다",  # 요추 곡률 분석
        "weak_core_suspect": True     # 약한 복근 의심
    }

    return result
