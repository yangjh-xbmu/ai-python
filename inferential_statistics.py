"""
推论统计（Inferential Statistics）的必要性与核心概念示例

推论统计的必要性：
1. 总体研究的局限性：
   - 研究整个总体往往成本过高或不现实
   - 某些研究场景下无法获取所有数据
   - 时间和资源的限制

2. 科学决策的需求：
   - 需要通过样本数据推断总体特征
   - 验证假设和理论
   - 预测未来趋势和结果

3. 实践应用价值：
   - 质量控制和产品抽检
   - 民意调查和市场研究
   - 医学临床试验
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. 抽样分布（Sampling Distribution）
def sampling_distribution_demo():
    # 创建一个总体分布（正态分布）
    population = np.random.normal(loc=100, scale=15, size=10000)
    
    # 多次抽样，计算样本均值
    sample_means = []
    sample_size = 30
    n_samples = 1000
    
    for _ in range(n_samples):
        sample = np.random.choice(population, size=sample_size)
        sample_means.append(np.mean(sample))
    
    print("\n1. 抽样分布示例：")
    print(f"总体均值: {np.mean(population):.2f}")
    print(f"样本均值的均值: {np.mean(sample_means):.2f}")
    print(f"样本均值的标准差: {np.std(sample_means):.2f}")
    print(f"理论标准误: {np.std(population)/np.sqrt(sample_size):.2f}")

# 2. 置信区间（Confidence Interval）
def confidence_interval_demo():
    # 生成样本数据
    sample_data = np.random.normal(loc=100, scale=15, size=30)
    
    # 计算95%置信区间
    confidence_level = 0.95
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)  # ddof=1 for sample standard deviation
    
    ci = stats.t.interval(confidence_level, 
                         len(sample_data)-1,
                         loc=sample_mean,
                         scale=sample_std/np.sqrt(len(sample_data)))
    
    print("\n2. 置信区间示例：")
    print(f"样本均值: {sample_mean:.2f}")
    print(f"95%置信区间: ({ci[0]:.2f}, {ci[1]:.2f})")

# 3. 假设检验（Hypothesis Testing）
def hypothesis_testing_demo():
    # 生成两组数据
    group1 = np.random.normal(loc=100, scale=15, size=30)  # 对照组
    group2 = np.random.normal(loc=110, scale=15, size=30)  # 实验组
    
    # 进行独立样本t检验
    t_stat, p_value = stats.ttest_ind(group1, group2)
    
    print("\n3. 假设检验示例（独立样本t检验）：")
    print(f"t统计量: {t_stat:.4f}")
    print(f"p值: {p_value:.4f}")
    print(f"结论: {'拒绝原假设' if p_value < 0.05 else '接受原假设'}")

# 4. 效应量（Effect Size）
def effect_size_demo():
    # 生成两组数据
    group1 = np.random.normal(loc=100, scale=15, size=30)
    group2 = np.random.normal(loc=110, scale=15, size=30)
    
    # 计算Cohen's d效应量
    cohens_d = (np.mean(group2) - np.mean(group1)) / np.sqrt(
        ((len(group1) - 1) * np.var(group1, ddof=1) + 
         (len(group2) - 1) * np.var(group2, ddof=1)) / 
        (len(group1) + len(group2) - 2))
    
    print("\n4. 效应量示例：")
    print(f"Cohen's d: {cohens_d:.4f}")
    
    if abs(cohens_d) < 0.2:
        effect = "微小"
    elif abs(cohens_d) < 0.5:
        effect = "小"
    elif abs(cohens_d) < 0.8:
        effect = "中等"
    else:
        effect = "大"
    
    print(f"效应大小: {effect}")

if __name__ == "__main__":
    # 运行所有示例
    sampling_distribution_demo()
    confidence_interval_demo()
    hypothesis_testing_demo()
    effect_size_demo()
