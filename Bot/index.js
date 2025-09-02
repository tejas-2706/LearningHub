import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'

puppeteer.use(StealthPlugin())

const run = async() => {
    const browser = await puppeteer.launch({headless:false});
    const page = await browser.newPage();
    await page.goto("https://fill.dev/form/credit-card-simple")

    // await new Promise(resolve => setTimeout(resolve, 5000)); // Waits for 5 seconds

    let selector = "input[id='cc-name']";
    await page.waitForSelector(selector);
    await page.type(selector,"Tejas Pangaonkar");

    selector = "select[id='cc-type']";
    await page.select(selector,"visa");


    // document.querySelector("input[id=':r5:']").click()
    // document.querySelector("input[value='blacktitanium']").click()
}

run();




