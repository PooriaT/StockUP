<script>
  import { page } from '$app/stores';
  import '../app.css';

  let isMenuOpen = false;
  const toggleMenu = () => (isMenuOpen = !isMenuOpen);
</script>

<div class="app-container">
  <!-- Sidebar/Navigation -->
  <nav class:open={isMenuOpen} class="sidebar">
    <button class="menu-toggle" on:click={toggleMenu}>
      <span class="hamburger"></span>
      <span class="visually-hidden">Toggle menu</span>
    </button>

    <div class="nav-items">
      <a href="/" class="nav-item" class:active={$page.url.pathname === '/'}>
        <span class="icon">🏠</span>
        <span class="text">Home</span>
      </a>

      <a
        href="/stock_information"
        class="nav-item"
        class:active={$page.url.pathname === '/stock_information'}
      >
        <span class="icon">📈</span>
        <span class="text">Stock Information</span>
      </a>

      <a
        href="/general_ai_analysis"
        class="nav-item"
        class:active={$page.url.pathname === '/general_ai_analysis'}
      >
        <span class="icon">🤖</span>
        <span class="text">GENERAL AI ANALYSIS</span>
      </a>

      <a href="/ai_chat" class="nav-item" class:active={$page.url.pathname === '/ai_chat'}>
        <span class="icon">💬</span>
        <span class="text">AI Chat</span>
      </a>

      <a href="/about" class="nav-item" class:active={$page.url.pathname === '/about'}>
        <span class="icon">ℹ️</span>
        <span class="text">ABOUT</span>
      </a>
    </div>
  </nav>

  <!-- Main Content -->
  <main class="main-content">
    <slot />
  </main>
</div>

<footer class="footer">
  <p>{new Date().getFullYear()} - Pooria Taghdiri</p>
</footer>
