--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2026-03-23 21:43:31

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16507)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    status character varying,
    limite_credito numeric(10,2),
    telefone integer,
    endereco character varying,
    nome character varying,
    codigo_cliente integer NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16514)
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    dt_elaboracao integer,
    num_pedido integer NOT NULL,
    codigo integer,
    codigo_cliente integer
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16500)
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    preco numeric(10,2),
    categoria character varying,
    codigo integer NOT NULL,
    nome_produto character varying
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- TOC entry 4802 (class 0 OID 16507)
-- Dependencies: 218
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (status, limite_credito, telefone, endereco, nome, codigo_cliente) FROM stdin;
\.


--
-- TOC entry 4803 (class 0 OID 16514)
-- Dependencies: 219
-- Data for Name: pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedido (dt_elaboracao, num_pedido, codigo, codigo_cliente) FROM stdin;
\.


--
-- TOC entry 4801 (class 0 OID 16500)
-- Dependencies: 217
-- Data for Name: produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produto (preco, categoria, codigo, nome_produto) FROM stdin;
\.


--
-- TOC entry 4651 (class 2606 OID 16513)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (codigo_cliente);


--
-- TOC entry 4653 (class 2606 OID 16518)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (num_pedido);


--
-- TOC entry 4649 (class 2606 OID 16506)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (codigo);


--
-- TOC entry 4654 (class 2606 OID 16524)
-- Name: pedido pedido_codigo_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_codigo_cliente_fkey FOREIGN KEY (codigo_cliente) REFERENCES public.cliente(codigo_cliente);


--
-- TOC entry 4655 (class 2606 OID 16519)
-- Name: pedido pedido_codigo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_codigo_fkey FOREIGN KEY (codigo) REFERENCES public.produto(codigo);


-- Completed on 2026-03-23 21:43:31

--
-- PostgreSQL database dump complete
--

