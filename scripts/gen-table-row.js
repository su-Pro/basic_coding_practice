import path from "path";
import fs, { promises } from "fs";
import _ from "lodash";
import { parse } from "node-html-parser";

const path_README = path.resolve("./README.md");
const start_table_README = "#### Leetcode";
const start_table_Tag = "> 📌";
const end_table_README = "#### AC-wing";
const end_table_Tag = "#### Leetcode";

const path_SOURCE = path.resolve("./leetcode/processed");
const totalTag = new Set();

class FileBasic {
  constructor(path) {
    this._content = "";
    this._path = path;
    this.obNameLink = "";
    this.tag = "";
    this.popular = 0;
  }

  async init() {
    const content = await promises.readFile(this._path);
    this._content = content.toString();
    this.pickMetadata();
  }

  pickMetadata() {
    this.genObNameLink(this._path);
    this.genTagAndPopular(this._content);
  }

  genObNameLink(path) {
    const fileName = _.last(path.split("/")).slice(0, -3);
    this.obNameLink = `[[${fileName}]]`;
  }

  genTagAndPopular(content) {
    const root = parse(
      content.substring(
        content.indexOf("Related Topics") - 10,
        content.indexOf("<strong> solution: </strong>")
      )
    );

    const target = root
      .getElementsByTagName("li")
      .map((tag) => tag.innerHTML)
      .slice(0, -1);

    const tags = target.slice(0, -1);
    const popular = target.slice(-1)[0];
    this.tag = tags.map((tag) => `#${tag} `).join(" ");

    this.popular = parseInt(popular.split(" ")[1], 10);

    totalTag.add(...tags);
  }
}

function doEncaseTable(fileBasic) {
  let tableTemplate = `
| Problem | Tag | popular |
    | --------- | --- | -------- |`;

  for (const f of fileBasic) {
    tableTemplate = `${tableTemplate}
    | ${f.obNameLink} | ${f.tag} | ${f.popular} |`;
  }

  return tableTemplate;
}

function replaceContent(newTable, newTags, filePath = path_README) {
  fs.readFile(filePath, "utf8", function (err, data) {
    if (err) {
      return console.log(err);
    }
    let result = data.replace(
      data.substring(
        data.indexOf(start_table_README),
        data.indexOf(end_table_README)
      ),
      `${start_table_README}
            ${newTable}
`
    );
    result = result.replace(
      result.substring(
        result.indexOf(start_table_Tag),
        result.indexOf(end_table_Tag)
      ),
      `> 📌 ${newTags.map((t) => `#${t}`).join(" ")}

`
    );
    fs.writeFile(filePath, result, "utf8", function (err, data) {
      if (err) return console.log(err);
    });
  });
}

async function main() {
  let filenameList = (
    await promises
      .readdir(path_SOURCE)
      .then((list) => list.map((f) => `${path_SOURCE}/${f}`))
  ).map((fPath) => new FileBasic(fPath));

  await Promise.all(filenameList.map((f) => f.init()));

  const completeTable = doEncaseTable(
    filenameList.sort((a, b) => b.popular - a.popular)
  );

  replaceContent(completeTable, Array.from(totalTag));
}

main();