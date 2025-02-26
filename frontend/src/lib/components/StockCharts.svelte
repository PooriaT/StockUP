<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import * as echarts from 'echarts';
    export let stock_history: any;
    let chart: echarts.ECharts;
    const chartId = `chart-${Math.random().toString(36).substr(2, 9)}`;

    onMount(async () => {
        const chartDom = document.getElementById(chartId);
        chart = echarts.init(chartDom);
        let dates = Object.keys(stock_history['Open']);
        let prices: number[][] = [];
        
        for (let i = 0; i < dates.length; i++) {
            prices.push([
            stock_history['Open'][dates[i]],
            stock_history['Close'][dates[i]],
            stock_history['Low'][dates[i]],
            stock_history['High'][dates[i]]
            ]);
        }
        let date = dates.map(d => d.split('T')[0]);
  
     const option = {
            xAxis: {
                data: date
            },
            yAxis: {},
            series: [
                {
                type: 'candlestick',
                data: prices
                }
            ]
        };
        chart.setOption(option);
    });

    onDestroy(() => {
        if (chart) {
            chart.dispose();
        }
    });
</script>

<div id={chartId} style="width: 600px; height: 400px;"></div>
