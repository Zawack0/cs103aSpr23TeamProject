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


/* add the value in the body to the list associated to the key */
// RIPPED FROM THE TODO VERSION, modify plz
// router.post('/transaction',
//   isLoggedIn,
//   async (req, res, next) => {
//       const todo = new ToDoItem(
//         {item:req.body.item,
//          createdAt: new Date(),
//          complete: false,
//          userId: req.user._id
//         })
//       await todo.save();
//       res.redirect('/todo')
// });


router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/tranaction')
});



module.exports = router;
