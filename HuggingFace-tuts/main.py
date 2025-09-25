from transformers import pipeline 

# model installed locatio - C:\Users\Asus\.cache\huggingface\hub

model = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
NEW DELHI: The largest-ever contract worth Rs 66,500 crore for 97 Tejas Mark-1A fighters is now all set to be inked with Hindustan Aeronautics (HAL), though the IAF is yet to get even the first such `improved’ jet of the 83 ordered earlier for Rs 46,898 crore in Feb 2021.
The mega 97-jet contract for the fourth-generation Tejas could be inked as early as Thursday, a day ahead of the retirement of 36 old MiG-21s that will drag down the IAF to its all-time low of 29 fighter squadrons (each has 16-18 jets), defence sources told TOI.
Pakistan, in contrast, is cruising close behind with 25 fighter squadrons, and will get at least 40 J-35A fifth-generation Chinese stealth jets in the near future. 
China, of course, is leagues ahead, with more than four times the number of fighters, bombers and force-multipliers as compared to India.
After Operation Sindoor, which saw Pakistan use Chinese-origin jets like J-10s armed with PL-15 beyond visual range air-to-air missiles with ranges over 200-km, an IAF internal assessment has held it will need far more than even its “authorized” 42.5 fighter squadrons to tackle the collusive and fused threat from its adversaries.
The IAF has repeatedly set the alarm bells ringing over the excruciatingly slow development saga of the single-engine Tejas fighters, stressing that operational preparedness cannot be sacrificed at the altar of `atmanirbharta’ (self-reliance) endlessly. Air Chief Marshal A P Singh himself said IAF is “very badly off in numbers” and needs to induct at least 40 fighters every year to stay combat ready.
All the 83 Tejas Mark-1A jets under the 2021 contract were to be delivered in the Feb 2024-Feb 2028 timeframe. 
The PM-led cabinet committee on security approved the acquisition of another 97 such jets on Aug 19 this year.
The IAF was insistent the new contract should not be inked before deliveries of the earlier 83 jets begin, with HAL being held accountable. The defence ministry, however, must spend its budget within specified timelines…the initial payment will go to HAL once the contract is signed,” a source said.
HAL, on its part, contends it will be able to deliver the first two of the 83 Tejas jets in Oct. 
Deliveries of the 99 GE-F404 turbofan engines by US firm General Electric, which HAL contracted for Rs 5,375 crore in Aug 2021, now appear to be stabilizing, an official said. 
GE has delivered three engines till now, with another seven slated by Dec. Thereafter, GE is expected to deliver 20 engines every year. For the 97-jet deal, HAL will ink another deal with GE for 113 more such engines for $1 billion, as earlier reported by TOI.
The IAF, however, wants to accept the first two fighters only if the ongoing firing trials of Astra beyond visual range air-to-air missiles, the advanced short-range air-to-air missiles and laser-guided bombs from them are successfully completed and properly certified.
The weapon trials and integration with the Israeli-origin Elta ELM-2052 radar and fire control system will take time. I don’t see the delivery happening before year-end unless IAF is forced to accept the fighters without certification,” a senior officer said.
HAL has promised to progressively scale up production to 20 Tejas per year, and then to 24-30 per year, with the third production line now fully functional in Nashik to add to the two existing ones at Bengaluru, apart from private sector supply chains
"""


response = model(
    text,
    max_length=100,
    min_length=10,
    do_sample=False
)

# print(response)

print(response[0]['summary_text'])


# langcahin - allows you to use multiple models together and make more advanced application and just deal with llms

