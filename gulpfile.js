var gulp = require("gulp");
var ts = require("gulp-typescript");
const tsProject = ts.createProject("./tsconfig.json");
const path = {
  controller : "src/controllers",
  routes: "src/routes"
}

//console.log(dataOnel.dataTwo)

gulp.task("default", function () {
  return tsProject.src().pipe(tsProject()).js.pipe(gulp.dest(path.controller));
});

/*gulp.task("controllers", function () {
  return tsProjectTwo.src().pipe(tsProjectTwo()).js.pipe(gulp.dest("src/controllers"));
});*/
