const hideAds = setInterval(() => {
    const adDialog = document.querySelector("div[data-dialog-name='gopro']");
    if (adDialog)
    {
        adDialog.querySelector("button").click();
        console.log('popup closed');
    }
  }, 10);