/*
  transaction.js -- Router for the Transactions
*/
const express = require('express');
const router = express.Router();
const TransactionItem = require('../models/TransactionItem')




isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
      res.locals.items = await TransactionItem.find({userId:req.user._id})
      res.render('transaction');
});

//const TransactionItem = require('./transactionItem'); // assuming transactionItem.js exports the TransactionItem schema


/* add the value in the body to the list associated to the key */

router.post('/addtransaction',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new TransactionItem(
        {
         userId: req.user._id,
         description: req.body.description,
         category: req.body.category,
         amount: req.body.amount,
         date: req.body.date
          //item:req.body.item,
         //createdAt: new Date(),
         //complete: false,
         //userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});


router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/transaction')
});



module.exports = router;
