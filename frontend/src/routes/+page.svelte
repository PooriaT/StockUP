<script lang="ts">
    import { onMount } from 'svelte';
    import '../app.css';
    let imgSrc = '/home_page_img_1.webp';

    let data: any;
    let stock_history = new Map<string, any>();
    let stock_news = new Map<string, any>();
    

    onMount(async () => {
        const response = await fetch("http://0.0.0.0:8000/big_seven");
        data = await response.json();
        for (const [key, value] of Object.entries(data.big_seven_info as Record<string, { stock_history: any, stock_news: any[] }>)) {
            stock_history.set(key, value.stock_history);
            stock_news.set(key, value.stock_news);
        }
    });
</script>

<div>
    <h1>Welcome to StockUP</h1>

    <img src={imgSrc} alt="StockUP" />

    <p>
        StockUP is an AI-driven stock market analysis tool designed to provide
        insightful information on stocks. This application is a prototype and serves
        as an educational platform to demonstrate how AI can be leveraged in financial
        analysis.
    </p>

    <p>Features:</p>
    <ul>
        <li>
            Easy-to-use interface for retrieving general stock information, historical data, and news
            updates for any given stock symbol.
        </li>
        <li>
            Utilizes the Gemini AI platform to generate detailed reports and trading recommendations based
            on the latest available data.
        </li>
    </ul>
    {#if data}
        <h2>Stock Data</h2>
        {#each Array.from(stock_news.keys()) as key}
            <div>
                <summary>{key}</summary>
                {#each stock_news.get(key) as item}
                    <h3>{item.content.title}</h3>
                    {#if item.content.thumbnail?.resolutions?.length > 1}
                        <img src={item.content.thumbnail.resolutions[1].url} alt={item.content.title} />
                    {/if}
                    <p>Publisher: {item.content.provider.displayName}</p>
                    {#if item.content.summary}
                        <p>Summary: {item.content.summary}</p>
                    {/if}
                    <p>Published on: {new Date(item.content.pubDate).toLocaleString()}</p>
                    {#if item.content.clickThroughUrl}
                        <p><a href={item.content.clickThroughUrl.url}>Read more</a></p>
                    {/if}
                    <hr />
                {/each}
            </div>
        {/each}
    {:else}
        <p>Loading...</p>
    {/if}
</div>

