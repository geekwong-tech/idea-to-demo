# 安装与更新

只安装Skill，实际需求与生成结果保存在你另行打开的项目目录中。

## 下载包安装

从[发布页](https://github.com/geekwong-tech/idea-to-demo/releases)下载版本压缩包。解压后应该是 `idea-to-demo/SKILL.md`，同级有 `agents/`、`references/` 等。不要只复制入口文件，也不要多嵌套一层同名目录。

选择一个安装位置：

| 范围 | 位置 |
| --- | --- |
| 个人全部项目 | `~/.agents/skills/idea-to-demo/` |
| 一个项目 | `<项目目录>/.agents/skills/idea-to-demo/` |

Windows的 `~` 通常是 `C:\Users\你的用户名`；macOS/Linux一般是用户主目录。两处择一，避免同名Skill同时出现。Codex在当前项目中可使用 `$idea-to-demo` 调用；CLI/IDE还可以用 `/skills` 查找。未出现时检查路径并重启。

## 使用 Git 安装

在项目根目录执行（目标目录须不存在）：

```sh
git clone https://github.com/geekwong-tech/idea-to-demo.git .agents/skills/idea-to-demo
```

只影响当前项目的Skill目录，不会把当前项目发布到GitHub。若父项目会提交文件，可根据团队约定采用普通目录副本或独立管理此嵌套仓库；不用Git也可直接按下载包方式安装。

## 更新与移除

下载包安装：先备份自行修改的Skill，再用新版本替换同名目录；不要混入旧版本的不同文件。Git安装且没有本地修改时，可在Skill目录运行 `git pull --ff-only`。若有修改，先保存并比较差异，不强制覆盖。

移除只需移走该Skill目录；不要删除存放需求成果的 `alignment/` 目录。已生成的HTML和Markdown可独立保留。

Codex本身的安装、登录与可用功能由你的环境决定，本包不调整账户、模型、全局设置或其他Skill。[官方Skill说明](https://learn.chatgpt.com/docs/build-skills)（核对日期2026-10-10）。
