<script lang="ts">
    import { marked } from 'marked';
    import DOMPurify from 'dompurify';
    import './ai_chat.css';
    import '../../app.css';
  
    interface AIResponse {
        response: string;
    }

    interface StockInfo {
        stock_general_info: {
            longName: string;
            [key: string]: unknown;
        };
    }
  
    let symbol = 'AAPL';
    let userPrompt = '';
    let aiResponse: AIResponse | null = null;
    let aiResponseText: string = '';
    let isLoading = false;
    let error: string | null = null;
    let stockInfo: StockInfo | null = null;
    let safeAIResponseText: string = '';
  
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
        aiResponseText = await marked.parse(aiResponse?.response || 'NO RESPONSE FROM AI');
        safeAIResponseText = DOMPurify.sanitize(aiResponseText);
        
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

    {#if aiResponse && !isLoading && !error && stockInfo && aiResponseText}
      <div class="analysis">
        <!-- eslint-disable-next-line svelte/no-at-html-tags -->
        {@html safeAIResponseText}
      </div>
    {/if}
</div>