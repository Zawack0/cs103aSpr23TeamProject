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

router.get('/transaction/edit/:itemId', 
  isLoggedIn, 
  async (req, res, next) => {
    console.log('made it to edit function')
    try {
      const transaction = await TransactionItem.findOne({_id:req.params.itemId});
      if (!transaction) {
        return res.status(404).send('Transaction not found');
      }
  
      // Autofill the form fields with the transaction data
      const description = transaction.description;
      const amount = transaction.amount;
      const category = transaction.category;
      const date = transaction.date;
  
      // Render the edit transaction form with the autofilled data
      res.render('edit-transaction', { title: 'Edit Transaction', itemId: req.params.itemId, description, amount, category, date });
    } catch (err) {
      console.error(err);
      return res.status(500).send('Internal server error');
    }
  });

  router.post('/transaction/edit/:itemId', isLoggedIn, async (req, res, next) => {
    const { description, amount, category, date } = req.body;
    const updatedTransaction = {
      description,
      amount,
      category,
      date
    };
  
    try {
      const transactionItem = await TransactionItem.findByIdAndUpdate(
        req.params.itemId,
        updatedTransaction,
        { new: true }
      );
      console.log('Transaction updated successfully:', transactionItem);
  
      res.redirect('/transaction');
    } catch (err) {
      console.error('Error updating transaction:', err);
      next(err);
    }
  });





module.exports = router;
