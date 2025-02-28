<script lang="ts">
    import { onMount } from 'svelte';
    import '../app.css';
    import './home.css';
    import StockCharts from '$lib/components/StockCharts.svelte';
  
    let imgSrc = '/home_page_img_1.webp';
    let data: any;
    let stock_history = new Map<string, any>();
    let stock_news = new Map<string, any>();
  
    let selectedCompany = "AAPL";
  
    onMount(async () => {
      const response = await fetch("http://0.0.0.0:8000/big_seven");
      data = await response.json();
      for (const [key, value] of Object.entries(data.big_seven_info as Record<string, { stock_history: any, stock_news: any[] }>)) {
        stock_history.set(key, value.stock_history);
        stock_news.set(key, value.stock_news);
      }
    });
  </script>
  
  <div class="page-content">
    <h1>Welcome to StockUP</h1>
    <img src={imgSrc} alt="StockUP" class="hero-img" />
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
      <div class="grid-container">
        {#each Array.from(stock_history.entries()) as [key, value]}
          <div class="chart-item">
            <h3>{key}</h3>
            <StockCharts stock_history={value} />
          </div>
        {/each}
      </div>
  
      <h2>Latest News</h2>
      <div class="tabs">
        {#each Array.from(stock_news.keys()) as company}
          <button
            class="tab-button {selectedCompany === company ? 'active' : ''}"
            on:click={() => selectedCompany = company}>
            {company}
          </button>
        {/each}
      </div>

      {#if stock_news.has(selectedCompany)}
        <div class="news-container">
          {#each stock_news.get(selectedCompany) as item}
            <div class="news-card">
              {#if item.content.thumbnail?.resolutions?.length > 1}
                <img src={item.content.thumbnail.resolutions[1].url} alt={item.content.title} />
              {/if}
              <h4>{item.content.title}</h4>
              <p class="news-publisher"><strong>Publisher:</strong> {item.content.provider.displayName}</p>
              {#if item.content.summary}
                <p class="news-summary">{item.content.summary}</p>
              {/if}
              <p class="news-date">{new Date(item.content.pubDate).toLocaleString()}</p>
              {#if item.content.clickThroughUrl}
                <p><a href={item.content.clickThroughUrl.url} target="_blank">Read more</a></p>
              {/if}
            </div>
          {/each}
        </div>
      {:else}
        <p>No news available for {selectedCompany}.</p>
      {/if}
    {:else}
      <p>Loading...</p>
    {/if}
  </div>
  