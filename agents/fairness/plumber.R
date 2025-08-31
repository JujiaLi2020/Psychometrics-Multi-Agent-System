#* @apiTitle Fairness Agent (R)

#* @get /ping
function() list(status="ok", agent="fairness")

#* @post /audit
function(req, res) {
  body <- if (nzchar(req$postBody)) jsonlite::fromJSON(req$postBody) else list()
  # toy fairness check
  list(agent="fairness", fairness_score=0.93, notes="demo")
}
