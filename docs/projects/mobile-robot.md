# 差速移动机器人导航

<span class="pill">示例项目 · 进行中</span>

## 目标与范围

在仿真中完成差速机器人建模、建图、定位与路径跟踪，保存一组可重现实验配置。此页面提供项目跟踪的起始结构。

## 里程碑

勾选项保存在当前浏览器；可导出记录，再同步回项目源文件。

```{raw} html
<div class="tracker" data-project="mobile-robot"><p><strong id="progress-label">40% · 2 / 5 已完成</strong></p><progress id="progress" max="5" value="2"></progress><label><input type="checkbox" checked> 明确需求与仿真环境</label><label><input type="checkbox" checked> 建立差速运动学模型</label><label><input type="checkbox"> 完成地图构建与定位验证</label><label><input type="checkbox"> 接入全局规划与路径跟踪</label><label><input type="checkbox"> 记录实验指标与复盘</label><button id="export-progress">导出进度 JSON</button><p class="muted">仅本机保存 · 不会自动同步给其他设备</p></div>
```

## 核心模型

轮半径为 $r$，左右轮间距为 $b$，角速度分别为 $\omega_L,\omega_R$：

$$ v=\frac r2(\omega_R+\omega_L),\qquad \omega=\frac rb(\omega_R-\omega_L) $$

## 验收与实验日志

| 实验 | 指标 | 当前结果 |
| --- | --- | --- |
| 直线跟踪 | 横向误差 RMS（m） | 待实验 |
| 目标点导航 | 成功率、耗时 | 待实验 |
| 避障 | 最小间隙（m） | 待实验 |

## 关联知识

[坐标变换](../notes/robotics.md) · [SLAM](../notes/slam.md) · [运动规划](../notes/planning.md) · [控制](../notes/control.md)
