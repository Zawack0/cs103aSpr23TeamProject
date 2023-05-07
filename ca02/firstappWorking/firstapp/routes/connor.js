const express = require('express');
const router = express.Router();
const RecipeItem = require('../models/RecipeItem')
const axios = require('axios');
const OPENAI_API_SECRET_KEY = process.env.OPENAI_API_SECRET_KEY;
const OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/completions';

router.get('/connor', (req,res,next) => {
    res.render('connor')
})

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

router.get('/cookbook/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /cookbook/remove/:itemId")
      await RecipeItem.deleteOne({_id:req.params.itemId});
      res.redirect('/cookbook')
});

  router.post('/addrecipe',
  isLoggedIn,
  async (req, res, next) => {
    const message = req.body.message;
    console.log(message);
    const prompt = message;
    
    const { Configuration, OpenAIApi } = require("openai");
    const configuration = new Configuration({
      apiKey: process.env.OPENAI_API_SECRET_KEY,
    });
    const openai = new OpenAIApi(configuration);
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      max_tokens: 700,
      temperature: 0,
    });
    const generatedText = response.data.choices[0].text;
    const firstLine = generatedText.split('\n')[1]
    console.log(generatedText)
    const recipe = new RecipeItem(
      {
        userId: req.user._id,
        Name: firstLine,
        Prompt: prompt,
        Recipe: generatedText,
        Favorite: false,
      }
    )
    await recipe.save();
    res.redirect('/cookbook')

});

router.post('/cookbook/rename/:itemId', isLoggedIn, async (req, res) => {
  const recipeId = req.params.itemId;
  const newRecipeName = req.body.name;
  const ToChange = await RecipeItem.findByIdAndUpdate(
    {_id:req.params.itemId},
    { $set: { Name: newRecipeName } },
    { new: true }
  );
  console.log("updated recipe name to:", newRecipeName);
  await ToChange.save();

  // Update the recipe name in the database using the recipeId and newRecipeName variables
  res.redirect('/cookbook'); // Redirect to the cookbook page after the recipe has been updated
});

router.post('/cookbook/makefav/:itemId', isLoggedIn, async (req, res) => {
  const recipeId = req.params.itemId;
  const newRecipeName = req.body.name;
  const old = await RecipeItem.findById(recipeId)
  newFavorite = !old.Favorite
  const ToChange = await RecipeItem.findByIdAndUpdate(
    {_id:req.params.itemId},
    { $set: { Favorite: newFavorite } },
    { new: true }
  );
  console.log("updated recipe to favorite");
  await ToChange.save();

  // Update the recipe name in the database using the recipeId and newRecipeName variables
  res.redirect('/cookbook'); // Redirect to the cookbook page after the recipe has been updated
});

router.get('/cookbook', isLoggedIn, async (req, res, next) => {
  const recipes = await RecipeItem.find({ userId: req.user._id });
  res.render('cookbook', { recipes });
});


module.exports = router;