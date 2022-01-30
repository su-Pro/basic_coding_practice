import fs, {promises as fsPromises} from "fs";
import path from "path";
import _ from "lodash";

const lang = "py";
// const lang = 'js'
const codeStart = lang === "py" ? "class" : "function";
const mkdWorkDir = "leetcode/editor/cn/doc/content";
const codeWorkDir = "leetcode/editor/cn/";
const flag_codeStart =
    "# leetcode submit region begin(Prohibit modification and deletion)";
const flag_codeEnd =
    "# leetcode submit region end(Prohibit modification and deletion)";

const outPuthDir = "leetcode/processed";

async function pickBothExistFileList() {
    const [mkdFileNames, codeFileNames] = await Promise.all(
        [mkdWorkDir, codeWorkDir].map((_p) =>
            fsPromises
                .readdir(_p)
                .then((fullNames) => fullNames.map((f) => path.parse(f).name))
        )
    );
    return _.intersection(mkdFileNames, codeFileNames);
}

async function doMergedFileContent(name) {
    function pickCoreCode(content, markStart = ":", markend = ";") {
        const markedCode = content
            .replace(flag_codeStart, markStart)
            .replace(flag_codeEnd, markend);

        const start = markedCode.lastIndexOf(codeStart);
        return markedCode.substring(start, markedCode.lastIndexOf(";"));
    }

    function joinContents(code, mkd) {
        return (
            mkd +
            ` 
<br>
<strong> solution: </strong>

\`\`\`javascript
input your code
\`\`\`

\`\`\`python3
${code}
\`\`\`
  `
        );
    }

  const [mkdContents, codeContents] = await Promise.all(
    ["md", lang].map((_e) =>
      fsPromises
        .readFile(
          path.resolve(_e === "md" ? mkdWorkDir : codeWorkDir, name + '.' + _e)
        )
        .then((c) => c.toString())
    )
  );
  return joinContents(pickCoreCode(codeContents, mkdContents), mkdContents);
}

function doOutputFile(content, fileName) {
    fs.writeFile(
        path.resolve(outPuthDir + `/${fileName}` + ".md"),
        Buffer.from(content),
        (e, a) => {
            console.log(e, a);
        }
    );
}

async function main() {
    const fileNameList = (await pickBothExistFileList()).sort();
    for (const fName of fileNameList) {
        const f = await doMergedFileContent(fName);
        doOutputFile(f, fName);
    }
    // 删除对应文件
    for (const fName of fileNameList) {
        fs.unlink(path.resolve(mkdWorkDir + `/${fName}.md`), (e, v) => {
        });
        fs.unlink(path.resolve(codeWorkDir + `/${fName}.${lang}`), (e, v) => {
        });
    }
}

main();
