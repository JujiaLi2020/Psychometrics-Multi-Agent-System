# plumber.R
#* @apiTitle Multi-Agent Psychometrics API

#* @get /hello
function() list(msg = "world")

#* @post /score
function(req, res) {
  source("agents/scoring/scoring_agent.R")
  scoring_agent(req, res)
}
