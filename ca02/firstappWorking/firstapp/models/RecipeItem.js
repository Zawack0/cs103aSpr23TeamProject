//THIS is right i hope
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var recipeSchema = Schema( {
  userId: ObjectId,
  description: String,
  Keywords: String,
  day: Number,
  month: Number,
  year: Number
} );

module.exports = mongoose.model( 'RecipeItem', recipeSchema );