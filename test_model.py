# 创建测试脚本：test_model.py
import joblib
import pandas as pd
import numpy as np

def test_model_loading():
    """测试模型加载"""
    try:
        # 加载模型
        model = joblib.load('./models/best_model_XGBoost.pkl')
        scaler = joblib.load('./models/scaler.pkl')
        feature_names = joblib.load('./models/feature_names.pkl')
        
        print("✅ 模型加载成功")
        print(f"   特征数量: {len(feature_names)}")
        
        # 测试预测
        test_features = np.zeros(len(feature_names))
        test_scaled = scaler.transform([test_features])
        prediction = model.predict(test_scaled)
        probability = model.predict_proba(test_scaled)
        
        print("✅ 预测功能正常")
        print(f"   预测结果: {prediction[0]}")
        print(f"   预测概率: {probability[0]}")
        
        return True
        
    except Exception as e:
        print(f"❌ 模型加载失败: {e}")
        return False

# 运行测试
if __name__ == "__main__":
    test_model_loading()