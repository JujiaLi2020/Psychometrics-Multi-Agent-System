#* @apiTitle Scoring Agent (R)

#* @get /ping
function() list(status="ok", agent="scoring")

#* @post /score
function(req, res) {
  body <- if (nzchar(req$postBody)) jsonlite::fromJSON(req$postBody) else list()
  score <- if (!is.null(body$value)) as.numeric(body$value) * 2 else NA_real_
  list(agent="scoring", score=score)
}
