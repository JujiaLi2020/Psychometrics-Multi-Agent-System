pr <- plumber::pr("plumber.R")
pr$setDocs(TRUE)
pr$run(host="0.0.0.0", port=8002, reload=TRUE)
