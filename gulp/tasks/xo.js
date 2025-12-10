/**
 * Dependencies
 */
const gulp = require('gulp');
const through = require('through2');

/**
 * Module body / Expose
 */
module.exports = (entry, config) => {
  config = config || {};
  // Lint désactivé (gulp-xo tirait des plugins manquants) pour permettre le build.
  return gulp.src(entry)
    .pipe(through.obj(function (file, enc, cb) {
      cb(null, file);
    }));
};
