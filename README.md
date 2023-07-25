# PFSE - Privacy Focused CLI Based Search Engine

PFSE (Privacy Focused CLI Based Search Engine) is a command-line tool that allows you to perform searches on popular search engines like Google and DuckDuckGo while maintaining your privacy. It ensures that your identity (IP) remains hidden from the search engines, providing you with a more secure and private search experience.

## Features

- Privacy: PFSE ensures that your IP address is not exposed to the search engines while performing searches.
- Multiple Search Engines: Currently, PFSE supports Google and DuckDuckGo, with more search engines planned to be added in the future.
- No Proxy or VPN Required: Unlike other privacy-focused solutions, PFSE doesn't require you to set up proxies or use VPNs to hide your IP address from the search engines.
- Grabengine: PFSE utilizes an online hosted compiler  to fetch HTML content from the search engines. It generates randomized IP addresses for each request, adding an extra layer of privacy to your searches.
- Beta Version: PFSE is currently in beta, and user feedback is highly encouraged. If you encounter any issues or bugs, please report them on the project's GitHub Issues page.


## WorkFlow
  
<div style="text-align: center;">
  <img src="https://i.ibb.co/QNGzD8V/Flowchart.png" alt="PFSE">
</div>

## OverView
<div style="text-align: center;">
  <img src="https://i.ibb.co/68SK2v7/image.png" alt="PFSE">
</div>


PFSE will then fetch the search results from search engine while ensuring your privacy is protected.

# Code Explanation
### Search Engine Queries

The `SearchEngineQueries` class provides methods to create Bash queries for Google and DuckDuckGo searches as well as WikiLeaks search.

### HTML Get

The `htmlGet` class has methods to fetch HTML content from Google, DuckDuckGo, and WikiLeaks.

### Content Processor

The `ContentProcessor` class contains methods to extract links and data from the HTML content fetched by the `htmlGet` class.

### Compilers

The `Compilers` class compiles the Bash queries using the Paiza API.

### Classes:

- `KeywordDataset`: Contains keyword datasets for WikiLeaks and other platforms.

- `SearchEngineQueries`: Provides methods to generate Bash queries for Google and DuckDuckGo searches as well as WikiLeaks search.

- `htmlGet`: Contains methods to fetch HTML content from Google, DuckDuckGo, and WikiLeaks.

- `ContentProcessor`: Contains methods to process HTML content and extract links/data from it.

- `Compilers`: Compiles the Bash queries using the Paiza API.

### Usage

To use the PTSE script, follow the command-line format given below:

```bash
python search.py -q "Your search query" -p <number_of_pages> -o <output_file>
```

## Contributing

We welcome contributions to PFSE to make it even better. If you have any suggestions, improvements, or bug fixes, please submit a pull request on our GitHub repository.

## Disclaimer

PFSE is an open-source project designed to enhance privacy during online searches. However, no tool can guarantee absolute anonymity. While PFSE takes measures to protect your IP address, other factors may still compromise your privacy. Use PFSE responsibly and be aware of the potential risks involved in online activities.

Remember to respect the terms of service of the search engines you use with PFSE. Using any tool to circumvent restrictions or violate policies is not encouraged.

Happy private searching with PFSE! 🕵️‍♂️

