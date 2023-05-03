//THIS is right i hope
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var transactionSchema = Schema( {
  userId: ObjectId,
  amount: Number,
  category: String,
  date: String,
  description: String,
  day: Number,
  month: Number,
  year: Number
} );

module.exports = mongoose.model( 'TransactionItem', transactionSchema );