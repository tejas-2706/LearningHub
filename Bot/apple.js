import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'

puppeteer.use(StealthPlugin())

const url = "https://www.apple.com/shop/buy-iphone/iphone-16-pro";

const givePage = async() => {
    const browser = await puppeteer.launch({headless:false});
    let page = await browser.newPage();
    return page
}

const add_to_cart = async(page) => {
    let selector = "input[id=':r5:']"
    await page.waitForSelector(selector)

    await page.evaluate(()=>{
        document.querySelector("input[id=':r5:']").click()
    })

    
    selector = "input[value='blacktitanium']";
    await page.waitForSelector(selector);
    await page.evaluate((s) => document.querySelector(s).click(),selector)

    await smart_clcik_with_pause(page,"input[data-autom='dimensionCapacity256gb']",0)
}

const run = async() => {
    let page = await givePage();
    await page.goto(url);
    await add_to_cart(page);
}    


const shipping = async(page) => {
    await smart_clcik_with_pause(page, "button[name='proceed]",0)
}


const smart_clcik_with_pause = async(page,selector,pause) => {
    await page.waitForSelector(selector);
    await page.evaluate((s) => document.querySelector(s).click(),selector);
    await new Promise(r => setTimeout(r,pause)) // 1.5 seconds
}

run();

// document.querySelector("input[value='blacktitanium']").click()



// page.type for writing
// multipleclicks