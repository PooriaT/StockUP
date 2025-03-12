<script lang="ts">
    import { marked } from 'marked';
    import './ai_chat.css';
    import '../../app.css';
  
    let symbol = 'AAPL';
    let userPrompt = '';
    let aiResponse: any;
    let aiResponseText: string | null = null;
    let isLoading = false;
    let error: string | null = null;
    let stockInfo: any = null;
  
    async function fetchAIResponse() {
      error = null;
      isLoading = true;
      
      try {
        const infoResponse = await fetch(`http://0.0.0.0:8000/stock/${symbol}`);
        const stockData = await infoResponse.json();
        if (!('longName' in stockData.stock_general_info)) {
          throw new Error('Invalid stock symbol');
        }
        stockInfo = stockData;

        const response = await fetch(`http://0.0.0.0:8000/ai_chatbot/${symbol}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain',
          },
          body: JSON.stringify({ user_prompt: userPrompt })
        });

        console.log(response);
  
        if (!response.ok) {
          throw new Error('Error fetching AI analysis');
        }
        aiResponse = await response.json();
        aiResponseText = aiResponse.response;
        
      } catch (err: unknown) {
        error = err instanceof Error ? err.message : 'An unexpected error occurred';
        aiResponse = null;
      } finally {
        isLoading = false;
      }
    }
</script>
  
<div class="page-content">
    <h1>General AI chatbot</h1>
    
    <div class="search-bar">
      <input 
        type="text" 
        placeholder="Enter stock symbol" 
        bind:value={symbol}
      />
    </div>
    <div class="search-bar">
        <textarea
        placeholder="Enter your question about the stock..."
        bind:value={userPrompt}
        rows="3"
      ></textarea>
    </div>
    <div class="search-bar">
      <button on:click={fetchAIResponse}>Submit</button>
    </div>

    {#if isLoading}
      <div class="loading">
        <div class="wheel"></div>
      </div>
    {/if}

    {#if error}
      <div class="error">
        <p>🚨 {error}</p>
      </div>
    {/if}

    {#if aiResponse && !isLoading && !error && stockInfo}
      <div class="analysis">
        {@html marked.parse(aiResponseText || '')}
      </div>
    {/if}
</div>