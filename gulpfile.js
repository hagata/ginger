var gulp = require('gulp'),
    path = require('path'),
    fs = require('fs'),
    merge = require('merge-stream'),
    rename = require('gulp-rename'),
    header = require('gulp-header'),
    concat = require('gulp-concat'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    foreach = require('gulp-foreach');


/**
 * Include Html files Task
 * Moves the .html files from each prototype folder in _dev and creates a /content file for JINJA
 */
gulp.task('html-includes', function() {
  return gulp.src('_frontend/includes/**/*.html')
    .pipe(foreach(function(stream, file){
      return stream
        .pipe(gulp.dest('templates/includes'));
    }))
})


