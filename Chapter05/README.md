This folder contains the large language model prompts in Chapter 5.

When copying the prompts, be sure to also copy the whitespace.  The prompts and cues are sometimes set up for the LLM to output by continuing the current line, and sometimes for the output to start on a new line.

The first prompt ends with a blank line.  We want the LLM to start its output on a new, blank line after the `List of 5 nouns`.  The LLM may not number the list, because it has not been cued.

```
Generate a list of nouns. The nouns should be synonyms of 'password'.

List of 5 nouns

```

For instance, the following prompt does NOT end on a new-line.  The cue of `1. ` is placed to help the LLM create a numbered list.

```
You are a consumer contacting an online retailer via their chat service.

Generate a numbered list of nouns a consumer might use while describing their inability to log in to your service in the phrase "I forgot my password". The nouns should be synonyms of 'password'.

List of 5 nouns 
1. 
```

You are free to experiment with the prompts to see the effect of changing the instructions, the examples, the cues, or any other part!