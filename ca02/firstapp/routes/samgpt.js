router.get('/samgpt/',
  isLoggedIn,
  async (req, res, next) => {
      res.render('samgpt');
});