# Statistics exercises interpretation

## Goal
Introductory exploration of sampling sizes, confidence intervals and hypothesis testing.

## Results
### Exercise 1
The full dataset GDP mean is 560334.59
The 10 sample dataset GDP mean is 1236244.08
The 25 sample dataset GDP mean is 696094.21
The 50 sample dataset GDP mean is 562314.58

### Exercise 2
The 95% confidence interval for GDP per capita is 5.66 - 10.18

### Exercise 3
|   | Mean | Standard deviation    | Sample size |
| -------- | :-------: | :-------:    | :-------: |
| Strong growth  | 9.99    | 12.91    | 50 |
| Decline growth type | 4.23 | 2.04    | 8 |

## Interpretation
- Samples vary because of the random sub-selection of *cantones* to include in the analysis is varied. As expected, as the sub-sample size increases, the value of the mean gets closer to the population mean. In this specific example, the value of the mean for a sample of 10 is more than double the population mean. The configuration of the GDP values across *cantones*, which is highly skewed, can substantially affect the mean. 

- The confidence interval (in this case 95%) provides a plausible range for the mean GDP per capita values. Repeatedly collecting similar samples and calculating confidence intervals with the same method would result in 95% of those intervals containing the population mean.

- While the means of GDP per capita in 'Strong' growth *cantones* vs those in the 'Declining' growth type is higher, it is also possible to see that the standard deviation is higher in Strong-growth *cantones*, indicating that the GDP per capita is much more variable. This condition suggests that not all Strong-growth *cantones* achieve similar levels of economic output per resident.

## Conclusion

It is important to take into consideration that sample size can influence the reliability of statistical estimates, particularly in highly variable data. Confidence intervals can be used to quantitfy uncertainty around an estimate. Comparing means, while a valid way of viewing preliminary insights, needs to take into consideration variability within the groups before generating robust conclusions.