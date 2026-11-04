公司内部发表前审批：英文原稿及中文全文
制作日期：2026-11-02；最新同步：2026-11-05

交付文件
../../output/pdf/blockchains-4630703-internal-approval-en-zh.pdf
（上述路径相对于本目录。）

来源与范围
英文采用 output/pdf/blockchains-4630703-author-corrected.pdf，即 2026-11-05
更正基金编号并补入全体作者同意出版声明后的 31 页校正稿。
中文基金编号同步为 2026ZD1501701，并补入对应的作者同意声明。
原英文页面、图像和高亮保持原样。
中文从合并文件第 32 页开始，依次覆盖标题、摘要、关键词、11 章正文、
12 张表、7 幅图的图题、公式、作者贡献、经费、各项声明、缩略语和参考文献。
依用户要求，7 幅图片直接引用原英文图，不翻译或重绘图片。
123 条参考文献保留原始书目信息并补充中文题名。章节、图表和引文编号对应原稿。
中文交叉引用使用独立的 zh. PDF 目标命名空间，确保跳转到中文部分。

可编辑来源
main.tex、frontmatter.tex、sections/、backmatter.tex：中文内容与排版。
reference-titles-zh.json：按原始引文键排列的全部中文参考文献题名。
references-zh.tex：从最新校正 TeX 和中文题名生成的参考文献。
verification.json：构建时的来源哈希、页数及内容/结构检查结果。

重建
在仓库根目录使用具有 pypdf 的 Python 环境执行：
  python scripts/build_internal_approval.py
需要可用的 XeLaTeX/ctex/xeCJK，以及 Windows 宋体、黑体、楷体字体。
构建与诊断文件写入已忽略的 tmp/pdfs/internal-approval/。

本机 TeX 兼容处理
本次环境的 LaTeX 内核为 2023-11-01，而全局 xeCJK 为 2026 版本。
在 tmp/pdfs/internal-approval/tex-compat/ 中从 CTeX 官方发布标签
xeCJK-v3.9.1 的 xeCJK/xeCJK.dtx 用 xetex 提取兼容样式，并在构建进程的
TEXINPUTS 中优先使用该目录。没有修改全局 TeX 安装。
来源：https://github.com/CTeX-org/ctex-kit/tree/xeCJK-v3.9.1/xeCJK
在此工作区重建时，可先在 PowerShell 中设置：
  $env:TEXINPUTS=(Resolve-Path 'tmp/pdfs/internal-approval/tex-compat').Path + ';'
TeX 包与临时工作文件不纳入 Git。

核验
构建检查章节/小节、图表、数学表达式、交叉引用标签、引文出现次数、
123 条参考文献题名、中文字体缺字及溢出诊断。合并后比较全部英文页面内容流
与提取文本，并验证中英文命名目标页和链接注释数量。PDF 页面经渲染检查。
