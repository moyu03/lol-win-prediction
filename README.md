# 🎮 英雄联盟胜率预测系统

基于机器学习的英雄联盟游戏胜负预测模型，通过分析游戏数据预测比赛结果。

## 📊 项目概述

本项目旨在通过机器学习模型预测英雄联盟排位赛的胜负结果。通过分析游戏的前期数据（如前10分钟的经济、击杀、目标控制等），构建能够准确预测最终胜负的模型。

### 主要功能
- 📈 游戏数据预处理与特征工程
- 🤖 多种机器学习模型对比
- 📉 模型性能评估与可视化
- 🔮 实时胜率预测
- 📊 特征重要性分析

## 🏗️ 项目结构
```
lol-win-prediction/
├── data/ # 数据目录
│ ├── raw/ # 原始数据（不提交到Git）
│ ├── processed/ # 处理后的数据
│ └── external/ # 外部数据（英雄信息等）
├── notebooks/ # Jupyter笔记本
│ ├── 01_data_exploration.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_model_training.ipynb
│ └── 04_model_evaluation.ipynb
├── src/ # 源代码
│ ├── init.py
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model_training.py
│ ├── utils.py
│ └── predict.py
├── models/ # 训练好的模型
├── tests/ # 测试文件
├── docs/ # 文档
├── images/ # 图片资源
├── requirements.txt # Python依赖
├── environment.yml # Conda环境配置
├── .gitignore # Git忽略配置
└── README.md # 项目说明
```
## 🚀 快速开始

### 环境配置

1. **使用Conda（推荐）**
```bash
创建新环境
conda env create -f environment.yml
激活环境
conda activate lol-ml
复制
```
2. **使用pip**
```bash
安装依赖
pip install -r requirements.txt
```
### 数据准备

1. 从Kaggle下载数据集：[League of Legends Ranked Matches](https://www.kaggle.com/datasets/datasnaek/league-of-legends/data)
2. 将下载的数据放入 `data/raw/` 目录
3. 运行数据预处理脚本：
```bash
python src/data_preprocessing.py
```
### 运行分析

1. 启动Jupyter Notebook：
```bash
jupyter notebook
```
2. 按顺序运行notebooks中的文件：
   - `01_data_exploration.ipynb` - 数据探索
   - `02_feature_engineering.ipynb` - 特征工程
   - `03_model_training.ipynb` - 模型训练
   - `04_model_evaluation.ipynb` - 模型评估

## 📈 模型性能

| 模型 | 准确率 | 精确率 | 召回率 | F1分数 | 训练时间 |
|------|--------|--------|--------|--------|----------|
| 逻辑回归 | 0.72 | 0.73 | 0.71 | 0.72 | 2s |
| 随机森林 | 0.78 | 0.79 | 0.77 | 0.78 | 15s |
| XGBoost | 0.81 | 0.82 | 0.80 | 0.81 | 25s |
| 神经网络 | 0.79 | 0.80 | 0.78 | 0.79 | 120s |

## 🔍 关键特征

根据特征重要性分析，影响胜负的关键因素包括：

1. **前10分钟经济差** - 权重最高
2. **首条小龙控制** - 胜率+8%
3. **一塔获取** - 胜率+6%
4. **击杀参与率** - 团队协同指标
5. **补刀优势** - 对线能力体现

## 🎯 使用方法

### 训练模型
```python
from src.model_training import ModelTrainer
trainer = ModelTrainer()
trainer.train('data/processed/train_data.csv')
trainer.save_model('models/best_model.pkl')
```
### 进行预测
```python
from src.predict import Predictor
predictor = Predictor('models/best_model.pkl')
result = predictor.predict(game_data)
print(f"胜率预测: {result['probability']:.2%}")
print(f"建议: {result['suggestion']}")
```
### 批量预测
```bash
python src/predict.py --input data/test_data.csv --output predictions.csv
```
## 📊 可视化结果

项目包含多种可视化图表：
- 特征重要性柱状图
- 相关性热力图
- 学习曲线图
- 混淆矩阵
- ROC曲线

## 🧪 测试

运行测试套件：
```bash
python -m pytest tests/
```
## 📁 数据集说明

本项目使用Kaggle上的英雄联盟数据集，包含以下主要特征：

- **游戏信息**: 时长、模式、版本
- **经济数据**: 金币、经验值差异
- **战斗数据**: 击杀、死亡、助攻
- **目标控制**: 小龙、大龙、防御塔
- **玩家数据**: 英雄选择、符文、召唤师技能

## 🤝 贡献指南

1. Fork本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 数据集提供：[Kaggle League of Legends Dataset](https://www.kaggle.com/datasnaek/league-of-legends)
- 参考实现：[League Ranked Match Predictor](https://www.kaggle.com/code/jadjaraisy/league-ranked-match-predictor)
- 技术支持：Scikit-learn, XGBoost, Pandas社区

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 项目Issue：[GitHub Issues](https://github.com/moyu03/lol-win-prediction/issues)

---

**⭐ 如果这个项目对你有帮助，请给个Star！**