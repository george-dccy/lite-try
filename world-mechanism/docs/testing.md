# Testing & Regression

工程化的目标不是让创作变成单元测试，而是让**稳定规则可以被机器检查，创作判断可以被 Golden Cases 保护**。

## 1. Schema Validation

`scripts/validate_blueprints.py` 会扫描 `examples/blueprints/*.yaml`，并用 `schemas/creative-blueprint.schema.json` 做结构校验。

它负责发现：
- 必填字段缺失；
- 字段类型漂移；
- 非法 status；
- 重复 Blueprint ID。

它不负责判断“创意好不好”。

## 2. Skill Structure Validation

`scripts/validate_skill.py` 检查：
- Skill front matter；
- 必要 reference / eval 文件；
- F / I / H / R 分层是否仍存在；
- “生产前停止” Gate 是否被误删。

## 3. Golden Case Regression

机器校验之后，核心引擎或 Skill 的重大修改还应人工回放三类案例：

- **A08**：科学 + 寓言 + 关系型；
- **H01**：历史 + 制度 + 真实事件；
- **S01**：当代社会 + 多方激励 + 非故事表达。

回归不是比较“生成文字是否一样”，而是问：
1. 问题有没有变浅？
2. 机制有没有被标题模板替代？
3. F / I / H / R 有没有串线？
4. 是否强迫所有题材进入同一种故事结构？
5. 人的 Gate 还在不在？

## 4. CI

GitHub Actions 在 push 到 `main` 和 pull request 时执行结构校验。

CI 通过只代表“工程接口没有明显断裂”，**不代表 Creative Blueprint 已获得人工批准**。
