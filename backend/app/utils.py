def analyze_file(file_path: str):
    return {
        "generation_id": 12345,
        "analysis": {
            "color_harmony_score": {"name": "Гармония цветов", "value": 8},
            "size_similarity_score": {"name": "Схожесть размеров", "value": 6},
            "contrast_score": {"name": "Контрастность", "value": 7},
            "overall_rating": {"name": "Общая оценка", "value": 7},
        },
        "recommendations": [
            {"name": "Общий стиль", "text": "Добавьте аксессуары для усиления стиля."},
            {"name": "Цветовая палитра", "text": "Попробуйте подобрать более яркие элементы для контраста."},
            {"name": "Размеры одежды", "text": "Одежда на верхней части тела слегка не соответствует размеру."},
        ],
    }
