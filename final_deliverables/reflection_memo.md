# Reflection Memo

## What Worked Well

The AutoResearch framework successfully allowed experimentation on the Sephora rating prediction problem. The use of a fixed evaluation metric (validation MAE) and a fixed train/validation/test split made experiments comparable/reproducable across runs. Random Forest models consistently outperformed the baseline linear regression model, and feature engineering further improved performance.

## What Worked Poorly

Many hyperparameter tuning experiments produced little improvement over the current best model. Several model changes resulted in diminishing returns, suggesting that model selection alone was not sufficient to achieve large gains. 

## Lessons Learned

The project demonstrated that feature engineering often produced larger gains than extensive hyperparameter tuning. Maintaining a fixed evaluation pipeline was critical for ensuring valid comparisons between experiments.

## Agent Performance

The agent performed well when exploring model variations and running experiments in a consistent manner. It was effective at testing different model families, adjusting hyperparameters, and maintaining a complete experimental record. The agent also helped automate repetitive tasks that would have been time-consuming to perform manually.

However, the agent performed poorly when deciding where to focus search effort. It often continued exploring small variations of Random Forest hyperparameters even after performance had largely plateaued. The agent also struggled to generate meaningful feature engineering ideas on its own and occasionally produced implementation or configuration errors that resulted in failed runs.

## Human Judgment

Several important decisions still required human judgment. I had to determine when a line of experimentation was no longer productive, decide which model directions were worth pursuing, and interpret the meaning of the results. The most important human contribution was recognizing that feature engineering represented a more promising direction than continued hyperparameter tuning. Human judgment was also necessary to evaluate failures and determine whether a crash reflected a useful lesson or simply a coding issue.

## How I Would Redesign the Loop

If I restarted the project, I would redesign the loop to spend less time on narrow hyperparameter searches and more time exploring new features earlier in the process. 

## Overall Reflection

The project showed that AI agents can be useful tools for structured experimentation, but they are not a replacement for research design and human oversight. The strongest improvements came from decisions about feature representation and evaluation design rather than from the agent's ability to run large numbers of experiments. My biggest takeaway is that a well-designed evaluation framework and thoughtful feature engineering are often more important than extensive hyperparameter tuning.
