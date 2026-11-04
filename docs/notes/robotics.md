# 机器人学基础

<span class="pill">知识笔记 · 入门示例</span>

标签：[运动学](../tags.md) · [坐标变换](../tags.md)

## 刚体位姿

在三维空间中，旋转与平移共同描述刚体位姿。下面约定 $T_{AB}$ 将 B 系坐标转换到 A 系。

$$
T_{AB}=\begin{bmatrix}R_{AB}&t_{AB}\\0^\top&1\end{bmatrix}\in SE(3)
$$

## 变换的组合

$$ T_{AC}=T_{AB}T_{BC},\qquad p_A=R_{AB}p_B+t_{AB} $$

相乘顺序体现坐标系的连接关系；调试时首先检查上下标是否能够衔接。

## 最小实现

```python
import numpy as np

def transform_point(R, t, p):
    """R: (3,3), t/p: (3,)；将 B 系点转换至 A 系。"""
    return R @ p + t

R = np.eye(3)
t = np.array([1., 0., 0.])
assert np.allclose(transform_point(R, t, np.zeros(3)), t)
```

## 学习检查

- 能解释主动旋转与坐标变换的区别。
- 能通过单位矩阵和逆变换验证实现。
- 下一步：推导差速运动学与雅可比矩阵。
