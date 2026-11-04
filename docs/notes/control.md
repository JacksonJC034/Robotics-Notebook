# 控制理论

<span class="pill">知识笔记 · 入门示例</span>

标签：[控制](../tags.md) · [PID](../tags.md)

## 从误差出发

定义跟踪误差 $e(t)=r(t)-y(t)$。连续时间 PID 的基本形式为：

$$ u(t)=K_p e(t)+K_i\int_0^t e(\tau)d\tau+K_d\frac{de(t)}{dt} $$

## 离散实现要点

```python
def pi_step(error, integral, dt, kp, ki, limit):
    candidate = integral + error * dt
    raw = kp * error + ki * candidate
    output = max(-limit, min(limit, raw))
    # 简单条件积分；工程使用前需验证边界行为
    if abs(raw) <= limit or error * raw < 0:
        integral = candidate
    return output, integral
```

## 验证顺序

1. 检查反馈符号、单位和采样周期。
2. 在受限输入下验证阶跃响应。
3. 记录超调、稳态误差和调节时间。
4. 检查饱和、噪声和延迟下的行为。

## 后续扩展

建立状态空间模型，逐步加入 LQR 与 MPC 的推导和对比实验。
