scoring_agent <- function(req, res) {
  # Example: simple echo
  data <- jsonlite::fromJSON(req$postBody)
  list(
    status = "ok",
    received = data
  )
}
