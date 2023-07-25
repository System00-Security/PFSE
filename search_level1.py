import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore
from urllib.parse import unquote
import json
import re
import random


class randomized:
    user_agents = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240", "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17", "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4", "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36", "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16", "Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4", "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0", "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53", "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2", "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4", "Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53", "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4", "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0", "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko", "Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53", "Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56", "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"]


class KeywordDataset:
    wikileaks = ["Vault7","Vault8","US Embassy Shopping List", "Amazon Atlas", "Dealmaker: Al Yousef", "Vault 8: Hive", "Spy Files: Russia", "Vault 7: Protego", "Vault 7: Angelfire", "Vault 7: ExpressLane", "Vault 7: CouchPotato", "Vault 7: Dumbo", "Vault 7: Imperial", "Vault 7: UCL / Raytheon", "Vault 7: Highrise", "Vault 7: BothanSpy", "Vault 7: Outlaw Country", "Vault 7: Elsa", "Vault 7: Brutal Kangaroo", "Vault 7: Cherry Blossom", "Vault 7: Pandemic", "Vault 7: Athena", "Vault 7: After Midnight", "Vault 7: Archimedes", "Vault 7: Scribbles", "Vault 7: Weeping Angel", "Vault 7: HIVE", "Vault 7: Grasshopper Framework", "Vault 7: Marble Framework", "Vault 7: Project Dark Matter", "Vault 7: CIA Hacking Tools Revealed", "CIA espionage orders for the 2012 French presidential election", "German BND-NSA Inquiry Exhibits", "NSA targets world leaders for US geopolitical interests", "NSA World Spying", "Hacking Team", "German BND-NSA Inquiry", "CIA Series", "Spy Files", "Detainee Policies", "Global Intelligence Files", "Macron Campaign Emails", "Trade in Services Agreement", "TTIP Chapters", "IMF internal: Anticipated Greek 'Disaster' - may leave Troika", "The New Dirty War for Africa's uranium and mineral rights", "Trans-Pacific Partnership Agreement", "AKP Email Archive", "EU military ops against refugee flows", "United Nations Confidential Reports", "SourceAmerica Tapes", "Sony Files", "Bank Julius Baer Documents", "Hillary Clinton Email Archive", "Public Library of US Diplomacy", "DNC Email Archive", "Saudi Cables", "Brennan Emails", "Syria Files", "Secret Congressional Reports", "Guantánamo Files", "Iraq War Logs", "Afghan War Logs", "Collateral Murder", "US Military Equipment in Iraq", "Military Dictionary", "US Military Equipment in Afghanistan"]
    ddosecrets = [".Win Network", "29 Leaks", "ACPeds", "ACS Law emails", "AKP", "ALET", "Aban Offshore", "Accent Capital", "Achinsk City Government", "Adopt A Trucker founder emails", "Aerial Surveillance Footage", "Aerogas", "Agencia Nacional de Hidrocarburos", "Airman Teixeira Leaks", "Alet", "Aliansce Sonae", "Alliance Coal", "AnibalLeaks", "Antiproprietary torrents", "Apex Mobile", "ArianTel", "Arron Banks", "Arteris", "Ashley Madison", "AssangeLeaks", "Australia Queensland", "Azusa Police Department", "BMK", "Bahamas Registry", "Banco de Poupança e Crédito", "Bangkok Airways", "Bedford County, PA Emails", "Blagoveshchensk City Administration", "BlueLeaks", "Bob Otto emails", "Bouygues Construction", "Boy Scouts of America", "Bradley Foundation", "CEIEC", "Cablegate", "Capital Legal Services", "Casagrande Group", "Casolaro Files", "Cayman National Bank and Trust", "Cellebrite Mobilogy", "Cellebrite Team Foundation Server", "Cellebrite and MSAB", "Central Bank of Russia", "Chamber of Mines (South Africa)", "Chamber of Mines of South Africa", "Chinese Ministry of Commerce", "Chinga La Migra", "CitizenGo", "CitizenGo & HatzeOir databases", "CityComp", "Comando Conjunto de las Fuerzas Armadas", "Comando General de las Fuerzas Militares de Colombia", "Comet Group", "Condie Construction Company", "Constellis", "Contact", "Conti ransomware chats", "Continent Express", "Contribute", "Convex", "Cook Islands registry", "CorpMSP", "CorruptBrazil", "Cosan", "Council for National Policy", "Cryptome Archive", "CyberAnakin", "DNC Emails", "Dark Side of the Kremlin", "Darknet Market", "Denver PD Crowd Management Manual", "Dept. for Church Charity and Social Service of the Russian Orthodox Church", "Dept of Education of the Strezhevoy City District Administration", "Distributed Denial of Secrets", "Documents from US Espionage Den", "Donate", "Donetsk People's Republic emails", "Doxxing-Adventskalender", "Drug War Genesis Interviews", "Durham", "Dussmann Group", "ECM", "EGM", "ENAMI EP", "Ejército del Perú", "El Salvador Police Database", "Elektrocentromontazh", "Elvees", "Embassy of Ecuador, Moscow", "Enerpred", "Enron emails", "Enron files", "Epik", "Equifax", "Estado Mayor Conjunto de la Defensa de Chile", "Estado Mayor Conjunto de las Fuerza Armadas de Chile", "Euroleaks", "Exconfidential Telegram channel", "ExecuPharm", "FAQ", "FBI-DHS leak", "FBI’s Secret Rules", "FSB employee leak", "Filippobaloo tiscali.it.zip", "Finfisher", "Fiscalia of Colombia", "Fisher & Paykel", "Fishrot Files", "Forest", "Fraternal Order of Police", "Frequently Asked Questions", "Fuck FBI Friday", "Fuerza Armada de El Salvador", "Fundação Nacional de Artes", "GOP Election Theft", "GQLeaks", "GUOV I GS - General Dept. of Troops and Civil Construction", "GabLeaks", "Gamma Group", "Gazprom Linde Engineering", "Gazregion", "German Chambers of Commerce", "GiveSendGo", "GiveSendGo 2.0", "GiveSendGo 3.0", "GiveSendGo 4.0", "GiveSendGo 5.0", "GiveSendGo Freedom Convoy donor info", "GorraLeaks", "Green Atom", "Groupe Comet", "Guccifer 2.0", "Guccifer Archive", "Gulf Copper", "HART", "HBGary", "Hacked Team", "Hacking Team", "Harita Group", "Henning Harders", "Heritage Foundation", "Hofeller Files", "Hunter Biden Laptop", "Hunter Biden emails", "Hunter Biden iPhone and iPad Backups", "INAFOR", "Identity Evropa Discord logs", "Igor.piliaiev@gmail.com", "Illinois Attorney General", "India Bulls", "Ingerop", "Innodata", "Innwa Bank", "Integrity Initiative", "Intolerance Network", "Iron March", "Italian State Police", "J.Irwin Company", "Jeb Bush Emails", "Jhonlin Group", "Jones Day", "KCSA Strategic Communications", "Khava-d@mail.ru", "LAPD Headshots", "LATAM Air", "LATAM Airlines", "LLC Capital", "LeakyMails", "LetMeSpy", "Liberty Counsel", "LineStar", "MAS Holdings", "MK Brokers", "MO Proud Boys videos", "MSpy", "MVTEC", "Macron leaks", "Major Investigations", "Manafort texts", "Marathon Group", "MashOil", "McLanahan Russia", "Medical Diagnostics Laboratories", "MeritServus and MeritKapital", "Metprom Group", "Metropolitan Police Department D.C.", "MilicoLeaks", "Mining Secrets", "Ministerio de Ambiente y Recursos Naturales", "Ministerio de Justicia of Chile", "Ministry of Communications and IT of Azerbaijan", "Ministry of Culture of the Russian Federation", "Ministry of Foreign Affairs of Cambodia", "Mosekspertiza", "Municipal Court of Princeton", "Myanmar Financials", "Myanmar Internal Revenue Department", "Myanmar Investments", "Myatt Blume & Osburn", "Myattcpa", "NPO VS", "NSA Report on Russia Spearphishing", "NZF DNR feb2017.tgz", "Nauru Police Force", "Neocom Geoservice", "Netzsch", "New Granada Energy Corporation", "Newbridge Securities", "No Fly List", "North American Roofing", "Nuclear Power Production and Development Company of Iran", "Nusantara Regas", "ODIN Intelligence", "OSCE Vienna", "Oakland City Hall", "Oath Keepers", "Odebrecht", "Office of Industrial Economics, Thailand", "OptimEyes", "Oryx Resources", "PSCB", "PT Rea Kaltim Plantations and Group", "PacoLeaks", "Parkland", "Parler", "Patriot Front", "Patriot Front audio", "Perceptics", "Petrofort", "Petrolimex", "Petroworks", "Pfeiffer Nuclear Weapon and National Security Archive", "Phoenix Program Interviews", "Planatol", "Podesta emails", "Polar Branch of the Russian Federal Research Institute of Fisheries and Oceanography", "Policía Nacional Civil de El Salvador", "Popov Files", "Port and Railway Projects Service of JSC UMMC", "Prav.cmr@gmail.com", "Prepara Brasil", "President Donald Trump’s Private Schedules", "Presque Isle Police Department", "Private Office of Sheikh Hazza bin Zayed Al Nahyan", "Procuradoria-Geral da Fazenda Nacional", "Project Whispers", "Public Chamber of the Krasnoyarsk", "Quiborax", "RKPLaw", "ROSOBORONEXPORT", "Rosatom", "Roskomnadzor", "Roskomnadzor 2.0 (GRFC)", "Roskomnadzor Moscow", "Rossi + MPS", "RostProekt", "RussianCensorFiles", "Russian Interior Ministry", "Russian soldier leak", "SOCAR Energoresource", "Saltos del Francoli", "Salvini emails", "Sawatzky", "Sberbank of Russia", "Secretaría de la Defensa Nacional de México", "Shell", "Sherwood", "Sholtai Boltai", "Shooting Sheriffs Saturday", "Snowden archive", "Sony", "Special State Protection Service of Azerbaijan", "Staminus", "Stratfor emails", "Surveillance Catalogs", "Synesis Surveillance System", "Syria files", "Syrian Censorship logs", "Syrian Ministry of Foreign Affairs", "THSA", "TIME Magazine Vault", "Technoserv", "Technotec", "Tejucana", "Tendertech", "Tetraedr", "Thailand Judicial Management Database", "TheDonald.win", "Thozis Corp", "TigerSwan", "Toll Group", "Tools of the Trade", "Torrents", "Transneft", "Trump Transition leak", "Trust Capital Funding", "Truth Will Out Films Customer Database", "Turkey National Police", "Turkish Takedown Thursday", "Tver Governor's office", "Twitch", "Ukraine General Prosecutor offices", "United Northern and Southern Knights of the Ku Klux Klan", "VGTRK", "VZ-US Corruption", "Varela Leaks", "Very English Coop d'Etat", "Virginia Department of Military Affairs", "Vyberi Radio", "W&T Offshore", "W.L. Contractors", "Washington County Sheriff", "Washington D.C. Metropolitan PD", "Worldwide Invest", "WtSpy", "Роскомнадзор"]
    prism = "Waihopai, INFOSEC, Information Security, Information Warfare, IW, IS, Priavacy, Information Terrorism, Terrorism Defensive Information, Defense Information Warfare, Offensive Information, Offensive Information Warfare, National Information Infrastructure, InfoSec, Reno, Compsec, Computer Terrorism, Firewalls, Secure Internet Connections, ISS, Passwords, DefCon V, Hackers, Encryption, Espionage, USDOJ, NSA, CIA, S/Key, SSL, FBI, Secert Service, USSS, Defcon, Military, White House, Undercover, NCCS, Mayfly, PGP, PEM, RSA, Perl-RSA, MSNBC, bet, AOL, AOL TOS, CIS, CBOT, AIMSX, STARLAN, 3B2, BITNET, COSMOS, DATTA, E911, FCIC, HTCIA, IACIS, UT/RUS, JANET, JICC, ReMOB, LEETAC, UTU, VNET, BRLO, BZ, CANSLO, CBNRC, CIDA, JAVA, Active X, Compsec 97, LLC, DERA, Mavricks, Meta-hackers, Steve Case, Tools, Telex, Military Intelligence, Scully, Flame, Infowar, Bubba, Freeh, Archives, Sundevil, jack, Investigation, ISACA, NCSA, spook words, Verisign, Secure, ASIO, Lebed, ICE, NRO, Lexis-Nexis, NSCT, SCIF, FLiR, Lacrosse, Flashbangs, HRT, DIA, USCOI, CID, BOP, FINCEN, FLETC, NIJ, ACC, AFSPC, BMDO, NAVWAN, NRL, RL, NAVWCWPNS, NSWC, USAFA, AHPCRC, ARPA, LABLINK, USACIL, USCG, NRC, CDC, DOE, FMS, HPCC, NTIS, SEL, USCODE, CISE, SIRC, CIM, ISN, DJC, SGC, UNCPCJ, CFC, DREO, CDA, DRA, SHAPE, SACLANT, BECCA, DCJFTF, HALO, HAHO, FKS, 868, GCHQ, DITSA, SORT, AMEMB, NSG, HIC, EDI, SAS, SBS, UDT, GOE, DOE, GEO, Masuda, Forte, AT, GIGN, Exon Shell, CQB, CONUS, CTU, RCMP, GRU, SASR, GSG-9, 22nd SAS, GEOS, EADA, BBE, STEP, Echelon, Dictionary, MD2, MD4, MDA, MYK, 747,777, 767, MI5, MI6, 757, Kh-11, Shayet-13, SADMS, Spetznaz, Recce, 707, CIO, NOCS, Halcon, Duress, RAID, Psyops, grom, D-11, SERT, VIP, ARC, S.E.T. Team, MP5k, DREC, DEVGRP, DF, DSD, FDM, GRU, LRTS, SIGDEV, NACSI, PSAC, PTT, RFI, SIGDASYS, TDM. SUKLO, SUSLO, TELINT, TEXTA. ELF, LF, MF, VHF, UHF, SHF, SASP, WANK, Colonel, domestic disruption, smuggle, 15kg, nitrate, Pretoria, M-14, enigma, Bletchley Park, Clandestine, nkvd, argus, afsatcom, CQB, NVD, Counter Terrorism Security, Rapid Reaction, Corporate Security, Police, sniper, PPS, ASIS, ASLET, TSCM, Security Consulting, High Security, Security Evaluation, Electronic Surveillance, MI-17, Counterterrorism, spies, eavesdropping, debugging, interception, COCOT, rhost, rhosts, SETA, Amherst, Broadside, Capricorn, Gamma, Gorizont, Guppy, Ionosphere, Mole, Keyhole, Kilderkin, Artichoke, Badger, Cornflower, Daisy, Egret, Iris, Hollyhock, Jasmine, Juile, Vinnell, B.D.M.,Sphinx, Stephanie, Reflection, Spoke, Talent, Trump, FX, FXR, IMF, POCSAG, Covert Video, Intiso, r00t, lock picking, Beyond Hope, csystems, passwd, 2600 Magazine, Competitor, EO, Chan, Alouette,executive, Event Security, Mace, Cap-Stun, stakeout, ninja, ASIS, ISA, EOD, Oscor, Merlin, NTT, SL-1, Rolm, TIE, Tie-fighter, PBX, SLI, NTT, MSCJ, MIT, RIT, Time, MSEE, Cable & Wireless, CSE, Embassy, ETA, Porno, Fax, finks, Fax encryption, white noise, pink noise, CRA, M.P.R.I., top secret, Mossberg, 50BMG, Macintosh Security, Macintosh Internet Security, Macintosh Firewalls, Unix Security, VIP Protection, SIG, sweep, Medco, TRD, TDR, sweeping, TELINT, Audiotel, Harvard, 1080H, SWS, Asset, Satellite imagery, force, Cypherpunks, Coderpunks, TRW, remailers, replay, redheads, RX-7, explicit, FLAME, Pornstars, AVN, Playboy, Anonymous, Sex, chaining, codes, Nuclear, subversives, SLIP, toad, fish, data havens, unix, Elvis, quiche, DES 1*, NATIA, NATOA, sneakers, counterintelligence, industrial espionage, PI, TSCI, industrial intelligence, H.N.P, Juiliett Class Submarine, loch, Ingram Mac-10, sigvoice, ssa, E.O.D., SEMTEX, penrep, racal, OTP, OSS, Blowpipe, CCS, GSA, Kilo Class, squib, primacord, RSP, Becker, Nerd, fangs, Austin, Comirex, GPMG, Speakeasy, humint, GEODSS, SORO, M5, ANC, zone, SBI, DSS, S.A.I.C., Minox, Keyhole, SAR, Rand Corporation, Wackenhutt, EO, Wackendude, mol, Hillal, GGL, CTU, botux, Virii, CCC, Blacklisted 411, Internet Underground, XS4ALL, Retinal Fetish, Fetish, Yobie, CTP, CATO, Phon-e, Chicago Posse, l0ck, spook keywords, PLA, TDYC, W3, CUD, CdC, Weekly World News, Zen, World Domination, Dead, GRU, M72750, Salsa, Blowfish, Gorelick, Glock, Ft. Meade, press-release, Indigo, wire transfer, e-cash, Bubba the Love Sponge, Digicash, zip, SWAT, Ortega, PPP, crypto-anarchy, AT&T, SGI, SUN, MCI, Blacknet, Middleman, KLM, Blackbird, plutonium, Texas, jihad, SDI, Uzi, Fort Meade, supercomputer, bullion, 3, Blackmednet, Propaganda, ABC, Satellite phones, Planet-1, cryptanalysis, nuclear, FBI, Panama, fissionable, Sears Tower, NORAD, Delta Force, SEAL, virtual, Dolch, secure shell, screws, Black-Ops, Area51, SABC, basement, data-haven, black-bag, TEMPSET, Goodwin, rebels, ID, MD5, IDEA, garbage, market, beef, Stego, unclassified, utopia, orthodox, Alica, SHA, Global, gorilla, Bob, Pseudonyms, MITM, Gray Data, VLSI, mega, Leitrim, Yakima, Sugar Grove, Cowboy, Gist, 8182, Gatt, Platform, 1911, Geraldton, UKUSA, veggie, 3848, Morwenstow, Consul, Oratory, Pine Gap, Menwith, Mantis, DSD, BVD, 1984, Flintlock, cybercash, government, hate, speedbump, illuminati, president, freedom, cocaine, $, Roswell, ESN, COS, E.T., credit card, b9, fraud, assasinate, virus, anarchy, rogue, mailbomb, 888, Chelsea, 1997, Whitewater, MOD, York, plutonium, William Gates, clone, BATF, SGDN, Nike, Atlas, Delta, TWA, Kiwi, PGP 2.6.2., PGP 5.0i, PGP 5.1, siliconpimp, Lynch, 414, Face, Pixar, IRIDF, eternity server, Skytel, Yukon, Templeton, LUK, Cohiba, Soros, Standford, niche, 51, H&K, USP, sardine, bank, EUB, USP, PCS, NRO, Red Cell, Glock 26, snuffle, Patel, package, ISI, INR, INS, IRS, GRU, RUOP, GSS, NSP, SRI, Ronco, Armani, BOSS, Chobetsu, FBIS, BND, SISDE, FSB, BfV, IB, froglegs, JITEM, SADF, advise, TUSA, HoHoCon, SISMI, FIS, MSW, Spyderco, UOP, SSCI, NIMA, MOIS, SVR, SIN, advisors, SAP, OAU, PFS, Aladdin, chameleon man, Hutsul, CESID, Bess, rail gun, Peering, NB, CBM, CTP, Sardine, SBIRS, SGDN, ADIU, DEADBEEF, IDP, IDF, Halibut, SONANGOL, Flu,Loin, PGP 5.53, EG&G, AIEWS, AMW, WORM, MP5K-SD, 1071, WINGS, cdi, DynCorp, UXO, Ti, THAAD. PRIME, SURVIAC"


class SearchEngineQueries:
    def GoogleBashQuery(query,pages):
        query = query.replace(" ", "+")
        BashCode = f"curl -s 'https://www.google.com/search?q={query}&gl=us&hl=en&start={pages}' -A '"+random.choice(randomized.user_agents)+"'"
        return BashCode
    def DuckDuckGoBashQuery(query,pages):
        query = query.replace(" ", "+")
        BashCode = f"curl -s 'https://lite.duckduckgo.com/lite/' -A ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' --data-raw 'q={query}&s={pages}&kl=&df=' "
        return BashCode
    def WikileaksBashQuery():
        BashCode = f"curl -s 'https://wikileaks.org/-Leaks-.html' -A '"+random.choice(randomized.user_agents)+"'"
        return BashCode

class htmlGet:
    def getGoogleSearch(query,pages):
        bashcode = SearchEngineQueries.GoogleBashQuery(query,pages)
        html = Compilers.ActASCoverpaiza(bashcode)
        return html
    def getDuckDuckGoSearch(query,pages):
        bashcode = SearchEngineQueries.DuckDuckGoBashQuery(query,pages)
        html = Compilers.ActASCoverpaiza(bashcode)
        return html
    def getWikileaksSearch():
        bashcode = SearchEngineQueries.WikileaksBashQuery()
        html = Compilers.ActASCoverpaiza(bashcode)
        return html

class ContentProcessor:
    def linksExtractionGoogle(html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        results = []
        for link in links:
            url = link['href']
            if url.startswith('/url?q='):
                real_url = url.split('/url?q=')[1].split('&sa=U&')[0]
                if "support.google.com" not in real_url and "accounts.google.com" not in real_url and "policies.google.com" not in real_url:
                    results.append(real_url)
        return results
    def linksExtractionDuckDuckGo(html):
        links = []
        soup = BeautifulSoup(html, 'html.parser')
        anchor_elements = soup.find_all('a', class_='result-link')
        for a in anchor_elements:
            links.append(a['href'])
        return links
    def wikileaks(html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find_all('li', class_='tile') 

            output_data = []
            for item in data:
                title = item.find('h2', class_='title').text.strip()
                link = item.find('a')['href']
                intro = item.find('div', class_='intro').p.text.strip()
                timestamp = item.find('div', class_='timestamp art700').text.strip()
                item_data = {
                    "title": title,
                    "link": link,
                    "intro": intro,
                    "timestamp": timestamp
                }

                output_data.append(item_data)
            output_json = json.dumps(output_data, indent=4)
            return output_json
        except Exception as e:
            return None

class Compilers:
    def ActASCoverpaiza(bashCode):
        endpoint = "https://paiza.io:443/api/projects.json"
        headers = {
            "Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=UTF-8",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36",
            "Referer": "https://paiza.io/en/projects/new?language=bash",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close"
        }
        compileTarget = {
            "project": {
                "language": "bash",
                "network": True,
                "output_type": None,
                "share": "private",
                "source_files": [{"body": bashCode, "filename": "Main.sh", "position": 0}]
            },
            "run": True,
            "save": True
        }
        compiledResponse = requests.post(endpoint, json=compileTarget, headers=headers)
        output = compiledResponse.json()["stdout"]
        soup = BeautifulSoup(output, "html.parser")
        htmlBeautify = soup.prettify()
        return htmlBeautify



class OLD:
    def E1WikileaksBrowser():
        coderun = f"curl -s 'https://wikileaks.org/-Leaks-.html' -A 'FireFox-Private'"
        url = "https://paiza.io:443/api/projects.json"
        headers = {
            "Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=UTF-8",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36",
            "Referer": "https://paiza.io/en/projects/new?language=bash",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close"
        }
        json_data = {
            "project": {
                "language": "bash",
                "network": True,
                "output_type": None,
                "share": "private",
                "source_files": [{"body": coderun, "filename": "Main.sh", "position": 0}]
            },
            "run": True,
            "save": True
        }
        response = requests.post(url, headers=headers, json=json_data)
        response = response.json()["stdout"]
        string_response = str(response)
        return string_response
    def wikileaks(html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find_all('li', class_='tile')  # Find all list items with class 'tile'

            output_data = []
            for item in data:
                title = item.find('h2', class_='title').text.strip()
                link = item.find('a')['href']
                intro = item.find('div', class_='intro').p.text.strip()
                timestamp = item.find('div', class_='timestamp art700').text.strip()
                item_data = {
                    "title": title,
                    "link": link,
                    "intro": intro,
                    "timestamp": timestamp
                }

                output_data.append(item_data)
            output_json = json.dumps(output_data, indent=4)
            return output_json
        except Exception as e:
            return None
    

def wikileaksProcessor(query):
    try:
        html = OLD.E1WikileaksBrowser()
        datas = OLD.wikileaks(html)
        if datas == None:
            html = OLD.E1WikileaksBrowser()
            datas = ContentProcessor.wikileaks(html)
        else:
            pass
        load = json.loads(datas)
        for data in load:
            if query.lower() in data["title"].lower():
                print(f"{Fore.YELLOW}[@@] {Fore.RESET}Title: {Fore.YELLOW}{data['title']}{Fore.RESET}")
                print(f"{Fore.YELLOW}[@@] {Fore.RESET}Link: {Fore.WHITE}{data['link']}{Fore.RESET}")
                print(f"{Fore.YELLOW}[@@] {Fore.RESET}Intro: {Fore.RED}{data['intro']}{Fore.RESET}")
                print(f"{Fore.YELLOW}[@@] {Fore.RESET}Timestamp: {Fore.GREEN}{data['timestamp']}{Fore.RESET}")
                print("--"*45)

    except:
        pass
def CVEfinder(cve):
    year = cve.split("-")[1]
    repo = f"https://raw.githubusercontent.com/nomi-sec/PoC-in-GitHub/master/{year}/{cve}.json"
    try:
        getdata = requests.get(repo)
        getdata.raise_for_status() 
        data = getdata.json()
        html_urls = []
        if isinstance(data, list):
            for item in data:
                html_url = item.get("html_url")
                if html_url:
                    html_urls.append(html_url)
            for url in html_urls:
                print(f"{Fore.YELLOW}[^_^] {Fore.RESET}Exploit URL: {Fore.WHITE}{url}{Fore.RESET}")
        else:
            pass
    except json.JSONDecodeError as e:
        pass
    except Exception as e:
        pass

def SearchProcessor(query, pages):
    try:
        pages = int(pages)
    except ValueError:
        print(f"{Fore.RED}[--] {Fore.RESET}Invalid number of pages provided. Please enter a valid integer.")
        return []

    alldata = []
    for i in range(pages):
        i = i * 10
        try:
            html = Compilers.ActASCoverpaiza(SearchEngineQueries.GoogleBashQuery(query, str(i)))
            data = ContentProcessor.linksExtractionGoogle(html)
            alldata.extend(data)
        except Exception as e:
            print(f"{Fore.RED}[--] {Fore.RESET}Error occurred while searching Google: {e}")

    for i in range(pages):
        i = i * 10
        try:
            html = Compilers.ActASCoverpaiza(SearchEngineQueries.DuckDuckGoBashQuery(query, str(i)))
            data = ContentProcessor.linksExtractionDuckDuckGo(html)
            alldata.extend(data)
        except Exception as e:
            print(f"{Fore.RED}[--] {Fore.RESET}Error occurred while searching DuckDuckGo: {e}")

    alldata = list(set(alldata))
    return alldata


def main():
    parse = argparse.ArgumentParser(description="PTSE - Privacy Templated Search Engine")
    parse.add_argument("-q", "--query", help="Query to search", required=True)
    parse.add_argument("-p", "--pages", help="Number of pages to search", required=True)
    parse.add_argument("-o", "--output", help="Output file to save results", required=False)
    args = parse.parse_args()
    query = args.query
    pages = args.pages
    prism_keywords = KeywordDataset.prism.split(", ")
    print(f"""
    █▀█ █▀▀ █▀ █▀▀
    █▀▀ █▀░ ▄█ ██▄ {Fore.CYAN}@system00_security{Fore.RESET}
    PTSE - Privacy Focused Search Engine
    [{Fore.GREEN}//{Fore.RESET}] {Fore.BLUE}Google{Fore.RESET} -> {Fore.CYAN}https://www.google.com{Fore.RESET}
    [{Fore.GREEN}//{Fore.RESET}] {Fore.BLUE}DuckDuckGo{Fore.RESET} -> {Fore.CYAN}https://lite.duckduckgo.com/lite/{Fore.RESET}
    [{Fore.YELLOW}**{Fore.RESET}] {Fore.BLUE}Active Crawler{Fore.RESET} -> {Fore.CYAN}1{Fore.RESET}
    """)

    for keyword in prism_keywords:
        if keyword.lower() in query.lower():
            print("--"*20+"Desclaimer" + "--"*20)
            print(f"{Fore.RED}[!!] {Fore.RESET}This Keyword Could Trigger PRISM {Fore.YELLOW}: [[{keyword}]]{Fore.RESET} - Know More {Fore.CYAN}https://en.wikipedia.org/wiki/PRISM{Fore.RESET}")
            print(f"{Fore.RED}[!!] {Fore.RESET}This Query Could {Fore.YELLOW}Possibly{Fore.RESET} Generate Survillance Trigger.")
            print("--"*45)
            
    for keyword in KeywordDataset.ddosecrets:
        
        if keyword.lower() in query.lower():
            print("--"*20+"Desclaimer" + "--"*20)
            print(f"{Fore.YELLOW}[00] {Fore.RESET}This Search Contains Query that matches DDOS Secrets Leaks {Fore.YELLOW}: [[{keyword}]]{Fore.RESET} - Wiki {Fore.CYAN}https://ddosecrets.com/wiki/{keyword.replace(' ', '_')}{Fore.RESET}")
            print("--"*45)
    splitedQuery = query.split(" ")
    for keyword in KeywordDataset.wikileaks:
        if keyword.lower() in query.lower():
            print("--"*20+"Desclaimer" + "--"*20)
            print(f"{Fore.YELLOW}[00] {Fore.RESET}This Search Contains Query that matches Wikileaks Leaks {Fore.YELLOW}: [[{keyword}]]{Fore.RESET} - Wiki {Fore.CYAN}https://wikileaks.org/-Leaks-.html{Fore.RESET}")
            wikileaksProcessor(keyword)
            print("--"*45)
    for keyword in splitedQuery:
        if keyword.lower() in KeywordDataset.wikileaks:
            print("--"*20+"Desclaimer" + "--"*20)
            print(f"{Fore.YELLOW}[00] {Fore.RESET}This Search Contains Query that matches Wikileaks Leaks {Fore.YELLOW}: [[{keyword}]]{Fore.RESET} - Wiki {Fore.CYAN}https://wikileaks.org/-Leaks-.html{Fore.RESET}")
            wikileaksProcessor(keyword)
            print("--"*45)
            break
    for keyword in KeywordDataset.wikileaks:
        if query.lower() in keyword.lower():
            print("--"*20+"Desclaimer" + "--"*20)
            print(f"{Fore.YELLOW}[00] {Fore.RESET}This Search Contains Query that matches Wikileaks Leaks {Fore.YELLOW}: [[{keyword}]]{Fore.RESET} - Wiki {Fore.CYAN}https://wikileaks.org/-Leaks-.html{Fore.RESET}")
            wikileaksProcessor(keyword)
            print("--"*45)
            break
    cveregex = re.compile(r"cve-\d{4}-\d{4,7}")
    cve_text = cveregex.findall(query.lower())
    if cve_text:
        print("--"*20+"Desclaimer" + "--"*20)
        for cve in cve_text:
            print(f"{Fore.YELLOW}[00] {Fore.RESET}This Search Contains Query CVE {Fore.YELLOW}: [[{cve}]]{Fore.RESET} - Details {Fore.CYAN}https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve}{Fore.RESET}")
            CVEfinder(cve.upper())
        print("--"*45)
            
    
    print(f"{Fore.GREEN}[++] {Fore.RESET}Searching for {Fore.CYAN}{query}{Fore.RESET} Scraping {Fore.CYAN}{pages}{Fore.RESET} pages")
    links = SearchProcessor(query, pages)
    if args.output:
        with open(args.output, "w") as f:
            for link in links:
                f.write(link+"\n")

    print(f"{Fore.GREEN}[++] {Fore.RESET}Found {Fore.CYAN}{len(links)}{Fore.RESET} links")
    print("-"*50)
    for link in links:
        link = unquote(link)
        print(f"{Fore.CYAN}[^^] {Fore.RESET}{link}")


if __name__ == "__main__":
    main()
