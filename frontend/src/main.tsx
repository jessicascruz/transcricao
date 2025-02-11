import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/global.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

// componentes
import { Home } from './components/Home'
import { Testes } from './components/Testes'



createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/testes' element={<Testes />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
