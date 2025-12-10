/**
 * Dependencies
 */
const path = require('path');
const browserify = require('browserify');
const babelify   = require('babelify');
const source     = require('vinyl-source-stream');
const through2   = require('through2');

/**
 * Module body / Expose
 */
module.exports = (entry, config) => {
  config = config || {};
  const built = browserify(entry)
    .transform(babelify);
  // vinyl-source-stream retourne un objet File sans marqueur _isVinyl attendu par vinyl-fs.
  // On l'ajoute pour éviter l'erreur "Received a non-Vinyl object in `dest()`".
  return built.bundle()
    .pipe(source(path.basename(entry)))
    .pipe(through2.obj((file, enc, cb) => {
      file._isVinyl = true;
      cb(null, file);
    }));
};
