// https://github.com/puppeteer/puppeteer/
const puppeteer = require('puppeteer');


async function scrape(url) {

    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);
   
//  1st element
    const [el] = await page.$x('');//xpath
    const text = await el.getProperty('textContent');
    const name = await text.jsonValue();
  
//  2nd element
    const [el2] = await page.$x('//*[@id="img"]');//xpath
    const src = await el2.getProperty('src');
    const avatarURL = await src.jsonValue();

    browser.close();

    return {name, avatarURL}
    
}

// module.exports = {
//     scrape
// }
