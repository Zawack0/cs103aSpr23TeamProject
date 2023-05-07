//THIS is right i hope
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var recipeSchema = Schema( {
  userId: ObjectId,
  Name: String,
  Prompt: String,
  Recipe: String,
  Favorite: Boolean
} );

module.exports = mongoose.model( 'RecipeItem', recipeSchema );