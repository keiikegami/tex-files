# HW1-2
## read data
corrected_inflation <- read_csv("~/Desktop/2018summer/macro/hw1/empirics/corrected_inflation.csv")

# time series format
ORI <- ts(corrected_inflation[["original"]])
LOG <- ts(corrected_inflation[["log"]])
MA <- ts(corrected_inflation[["ma"]])

# ma
AIC_ma <- 1:24
for (i in 1:24){
  result <- arima(MA, order = c(i,0,0))
  AIC_ma[i] <- result$aic
}

ma_optimal_p <- which.min(AIC_ma)

# log
AIC_log <- 1:24
for (i in 1:24){
  result <- arima(LOG, order = c(i,0,0))
  AIC_log[i] <- result$aic
}

log_optimal_p <- which.min(AIC_log)

# (3)




# HW1-4

## (1)
official_gap <- ts(official_gap[["gap"]], c(1949,1),,4)
ts.plot(official_gap)

## (2)
install.packages("mFilter")
library(mFilter)
real_gdp <- read_csv("~/Desktop/2018summer/macro/hw1/empirics/real_gdp.csv")

rgdp <- ts(real_gdp[["rgdp"]], c(1947),,4)
hp_result <- hpfilter(rgdp)
hp_trend <- hp_result$trend
hp_cycle <- hp_result$cycle
ts.plot(hp_cycle)


## (3) unit root test
install.packages("tseries")
library(tseries)
### ADF test
result_adf <- adf.test(rgdp)
### DF test
result_df <- adf.test(rgdp, k = 0)
### p-value = 0.6631, so it is not significant

## (c)BN decomposition
first_diff_rgdp <- diff(rgdp)
### find the optimal model for the first difference series.
AIC_diff <- 1:5
for (i in 1:5){
  result <- arima(first_diff_rgdp, order = c(i,0,0))
  AIC_diff[i] <- result$aic
}

diff_optimal_p <- which.min(AIC_diff)
### the chosen order is 2, so I assume the first difference series follows AR(2)
### then I use the result of problem 3
result <- arima(first_diff_rgdp, order = c(2,0,0))
beta1 <- result$coef[1]
beta2 <- result$coef[2]
BN_trend <- 1:length(rgdp)-2
for (i in 3:length(rgdp)){
  BN_trend[i-2] <- rgdp[i] + ((beta1+beta2)*first_diff_rgdp[i] + beta2*first_diff_rgdp[i-1])/(1-beta1-beta2)
}
BN_cycle <- ts(rgdp[3:length(rgdp)] - BN_trend, c(1947,7),,4)
ts.plot(BN_cycle, ylim=c(-400, 400))


## (d) Kinked trend
ind <- (1973 - 1947) * 4 + 2
# Before kink
before <- rgdp[1:ind]
# After kink
after <- rgdp[ind:length(rgdp)]
# make trend terms
before_trend <- time(before)
after_trend <- time(after)

# regression
before_result <- lm(before ~ before_trend)
before_gap <- residuals((before_result))
after_result <- lm(after ~ after_trend)
after_gap <- residuals((after_result))
kinked_gap <- ts(c(data.frame(before_gap)$before_gap, data.frame(after_gap)$after_gap),c(1947,1),,4)
ts.plot(kinked_gap)












