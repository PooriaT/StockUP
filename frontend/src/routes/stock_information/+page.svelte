<script lang="ts">
  import { onMount } from 'svelte';
  import StockCharts from '$lib/components/StockCharts.svelte';
  import './stock_information.css';
  import '../../app.css';

  let symbol = 'AAPL';
  let stockData: any;
  let activeTab: string = '1D';
  const tabs = ['1D', '5D', '1M', '6M', '1Y', '5Y', 'All'];

  async function fetchStock() {
    try {
      const response = await fetch(`http://0.0.0.0:8000/stock/${symbol}`);
      if (!response.ok) {
        stockData = null;
        alert("Error fetching stock data");
        return;
      }
      stockData = await response.json();
    } catch (error) {
      console.error('Error fetching stock data:', error);
    }
  }
  
  onMount(() => {
    fetchStock();
  });
</script>

<div class="page-content">
  <h1>Stock Dashboard</h1>
  <div class="search-bar">
    <input type="text" placeholder="Enter stock symbol" bind:value={symbol} on:keydown={(event) => { if (event.key === 'Enter') fetchStock(); }} />
  </div>

  {#if stockData}
  <!-- General Information -->
  <section class="section">
    <h2>General Information</h2>
    <div class="info">
      {#if stockData.stock_general_info.website}
        <p>
          <strong>Company Name:</strong>
          <a href="{stockData.stock_general_info.website}" target="_blank">
            {stockData.stock_general_info.longName}
          </a>
        </p>
      {:else}
        <p><strong>Company Name:</strong> {stockData.stock_general_info.longName}</p>
      {/if}
      <p><strong>Country:</strong> {stockData.stock_general_info.country}</p>
      <p><strong>City:</strong> {stockData.stock_general_info.city}</p>
      <p><strong>Industry:</strong> {stockData.stock_general_info.industry}</p>
      <p><strong>Sector:</strong> {stockData.stock_general_info.sector}</p>
      <p><strong>Business Summary:</strong> {stockData.stock_general_info.longBusinessSummary}</p>
    </div>
  </section>
  <!-- Finance Information -->
  <section class="section">
    <h2>Finance Information</h2>
    <p><strong>Current Price:</strong> {stockData.stock_general_info.currentPrice}</p>
    <div class="finance-grid">
      <div class="col">
        <p><strong>Previous Close:</strong> {stockData.stock_general_info.previousClose}</p>
        <p><strong>Open:</strong> {stockData.stock_general_info.open}</p>
        <p><strong>Day Low:</strong> {stockData.stock_general_info.dayLow}</p>
        <p><strong>Day High:</strong> {stockData.stock_general_info.dayHigh}</p>
        <p><strong>Volume:</strong> {stockData.stock_general_info.volume}</p>
        <p><strong>Average Volume:</strong> {stockData.stock_general_info.averageVolume}</p>
        <p><strong>Average Volume (10 days):</strong> {stockData.stock_general_info.averageVolume10days}</p>
        {#if stockData.stock_general_info.bid}
          <p><strong>Bid:</strong> {stockData.stock_general_info.bid} * {stockData.stock_general_info.bidSize}</p>
        {/if}
        {#if stockData.stock_general_info.ask}
          <p><strong>Ask:</strong> {stockData.stock_general_info.ask} * {stockData.stock_general_info.askSize}</p>
        {/if}
      </div>
      <div class="col">
        <p><strong>Market Cap:</strong> {stockData.stock_general_info.marketCap}</p>
        <p><strong>52 Week Low:</strong> {stockData.stock_general_info.fiftyTwoWeekLow}</p>
        <p><strong>52 Week High:</strong> {stockData.stock_general_info.fiftyTwoWeekHigh}</p>
        {#if stockData.stock_general_info.trailingPE}
          <p><strong>Trailing PE:</strong> {stockData.stock_general_info.trailingPE}</p>
        {/if}
        {#if stockData.stock_general_info.forwardPE}
          <p><strong>Forward PE:</strong> {stockData.stock_general_info.forwardPE}</p>
        {/if}
        <p><strong>50 Day Average:</strong> {stockData.stock_general_info.fiftyDayAverage}</p>
        <p><strong>200 Day Average:</strong> {stockData.stock_general_info.twoHundredDayAverage}</p>
        <p><strong>Currency:</strong> {stockData.stock_general_info.currency}</p>
        <p><strong>Exchange:</strong> {stockData.stock_general_info.exchange}</p>
        <p><strong>Enterprise Value:</strong> {stockData.stock_general_info.enterpriseValue}</p>
      </div>
    </div>
    <div class="finance-grid">
      <div class="col">
        {#if stockData.stock_general_info.targetHighPrice}
          <p><strong>Target High Price:</strong> {stockData.stock_general_info.targetHighPrice}</p>
        {/if}
        {#if stockData.stock_general_info.targetLowPrice}
          <p><strong>Target Low Price:</strong> {stockData.stock_general_info.targetLowPrice}</p>
        {/if}
        {#if stockData.stock_general_info.targetMeanPrice}
          <p><strong>Target Mean Price:</strong> {stockData.stock_general_info.targetMeanPrice}</p>
        {/if}
        {#if stockData.stock_general_info.targetMedianPrice}
          <p><strong>Target Median Price:</strong> {stockData.stock_general_info.targetMedianPrice}</p>
        {/if}
      </div>
      <div class="col">
        {#if stockData.stock_general_info.recommendationMean}
          <p><strong>Recommendation Mean:</strong> {stockData.stock_general_info.recommendationMean}</p>
        {/if}
        {#if stockData.stock_general_info.recommendationKey}
          <p><strong>Recommendation Key:</strong> {stockData.stock_general_info.recommendationKey}</p>
        {/if}
        {#if stockData.stock_general_info.numberOfAnalystOpinions}
          <p><strong>Number of Analyst Opinions:</strong> {stockData.stock_general_info.numberOfAnalystOpinions}</p>
        {/if}
      </div>
    </div>
  </section>
  <!-- Stock Charts -->
  <section class="section">
    <h2>Historical Data</h2>
    <div class="tabs">
      {#each tabs as tab}
        <button 
          class:active={activeTab === tab}
          on:click={() => activeTab = tab}
        >
          {tab}
        </button>
      {/each}
    </div>  
    {#if activeTab === '1D'}
      <StockCharts stock_history={stockData.stock_history_1d} />
    {:else if activeTab === '5D'}
      <StockCharts stock_history={stockData.stock_history_5d} />
    {:else if activeTab === '1M'}
      <StockCharts stock_history={stockData.stock_history_1mo} />
    {:else if activeTab === '6M'}
      <StockCharts stock_history={stockData.stock_history_6mo} />
    {:else if activeTab === '1Y'}
      <StockCharts stock_history={stockData.stock_history_1y} />
    {:else if activeTab === '5Y'}
      <StockCharts stock_history={stockData.stock_history_5y} />
    {:else if activeTab === 'All'}
      <StockCharts stock_history={stockData.stock_history_all} />
    {/if}
  </section>
  <!-- News Section -->
  <section class="section">
    <h2>News</h2>
    <div class="news-container">
      {#each stockData.stock_news as news}
        <div class="news-item">
          <h3>{news.content.title}</h3>
          {#if news.content.thumbnail?.resolutions?.length > 1}
            <img src={news.content.thumbnail.resolutions[1].url} alt={news.content.title} />
          {/if}
          <p><strong>Publisher:</strong> {news.content.provider.displayName}</p>
          {#if news.content.summary}
            <p><strong>Summary:</strong> {news.content.summary}</p>
          {/if}
          <p><strong>Published on:</strong> {new Date(news.content.pubDate).toLocaleString()}</p>
          {#if news.content.clickThroughUrl}
            <p><a href={news.content.clickThroughUrl.url} target="_blank">Read more</a></p>
          {/if}
          <hr />
        </div>
      {/each}
    </div>
  </section>
  {/if}
</div>

