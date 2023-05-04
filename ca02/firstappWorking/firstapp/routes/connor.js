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


  router.post('/addrecipe',
  isLoggedIn,
  async (req, res, next) => {
    const message = req.body.message;
    console.log(message);
    const prompt = message;
    
    const { Configuration, OpenAIApi } = require("openai");
    const configuration = new Configuration({
      apiKey: process.env.OPENAI_API_KEY,
    });
    const openai = new OpenAIApi(configuration);
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      max_tokens: 700,
      temperature: 0,
    });
    const generatedText = response.data.choices[0].text;
    console.log(generatedText)
    res.redirect('/connor')

});

module.exports = router;