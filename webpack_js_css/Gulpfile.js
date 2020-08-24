const { src, dest, parallel } = require("gulp");
const uglify = require("gulp-uglify");
const rename = require("gulp-rename");
const concat = require("gulp-concat");
const compress = require("gulp-compress");

// https://getbootstrap.com/docs/4.0/getting-started/contents/ -> doesnt requires popperjs but jquery

function js() {
  return src([
    "./node_modules/@fortawesome/fontawesome-free/js/all.min.js",
    "./node_modules/bootstrap/dist/js/bootstrap.bundle.min.js",
    "./node_modules/jquery/dist/jquery.min.js",
    "./node_modules/tableexport.jquery.plugin/libs/FileSaver/FileSaver.min.js",
    "./node_modules/tableexport.jquery.plugin/libs/js-xlsx/xlsx.core.min.js",
    "./node_modules/tableexport.jquery.plugin/tableExport.min.js",
    // "./node_modules/xlsx/dist/xlsx.full.min.js",
    "./node_modules/bootstrap-table/dist/bootstrap-table.min.js",
    "./node_modules/bootstrap-table/dist/extensions/copy-rows/bootstrap-table-copy-rows.min.js",
    "./node_modules/bootstrap-table/dist/extensions/export/bootstrap-table-export.min.js",
  ])
    .pipe(concat("all_files.js"))
    .pipe(dest("../static"));
}

function css() {
  return src([
    "./node_modules/@fortawesome/fontawesome-free/css/all.min.css",
    "./node_modules/bootstrap/dist/css/bootstrap.min.css",
    // "../static/style.css",
    "./node_modules/bootstrap-table/dist/bootstrap-table.min.css",
  ])
    .pipe(concat("all_files.css"))
    .pipe(dest("../static"));
}

const build = parallel(css, js);

exports.js = js;
exports.css = css;
exports.build = build;
exports.default = build;
