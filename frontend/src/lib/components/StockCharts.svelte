<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import * as echarts from 'echarts';
    interface StockHistory {
        Open: Record<string, number>;
        Close: Record<string, number>;
        Low: Record<string, number>;
        High: Record<string, number>;
    }
    export let stock_history: StockHistory;
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
        let date = dates.map(d => {
            let [datePart, timePart] = d.split('T');
            let [year, month, day] = datePart.split('-');
            let [hour, minute] = timePart.split(':');
            if (dates[0].split('T')[0] === dates[dates.length - 1].split('T')[0]) {
                return `${year}-${month}-${day} ${hour}:${minute}`;
            } else {
                return `${year}-${month}-${day}`;
            }
        });
  
     const option = {
            xAxis: {
                data: date
            },
            yAxis: {
                scale: true
            },
            dataZoom: [
                {
                type: 'inside',
                start: 0,
                end: 100
                },
                {
                show: true,
                type: 'slider',
                top: '90%',
                start: 50,
                end: 100
                }
            ],
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
