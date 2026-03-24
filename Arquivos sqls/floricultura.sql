--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2026-03-23 21:43:20

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
-- TOC entry 217 (class 1259 OID 16439)
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    cpf integer NOT NULL,
    rg integer,
    telefone integer,
    endereco character varying,
    nome character varying
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16453)
-- Name: compras; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.compras (
    id_compra integer NOT NULL,
    nome_cliente character varying,
    dt_compra date,
    valor_total numeric(10,2),
    cpf integer,
    id_produto integer
);


ALTER TABLE public.compras OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16446)
-- Name: produtos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtos (
    id_produto integer NOT NULL,
    nome character varying(100),
    tipo character varying,
    preco numeric(10,2),
    qtde_estoque integer
);


ALTER TABLE public.produtos OWNER TO postgres;

--
-- TOC entry 4801 (class 0 OID 16439)
-- Dependencies: 217
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (cpf, rg, telefone, endereco, nome) FROM stdin;
\.


--
-- TOC entry 4803 (class 0 OID 16453)
-- Dependencies: 219
-- Data for Name: compras; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.compras (id_compra, nome_cliente, dt_compra, valor_total, cpf, id_produto) FROM stdin;
\.


--
-- TOC entry 4802 (class 0 OID 16446)
-- Dependencies: 218
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produtos (id_produto, nome, tipo, preco, qtde_estoque) FROM stdin;
\.


--
-- TOC entry 4649 (class 2606 OID 16445)
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (cpf);


--
-- TOC entry 4653 (class 2606 OID 16459)
-- Name: compras compras_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_pkey PRIMARY KEY (id_compra);


--
-- TOC entry 4651 (class 2606 OID 16452)
-- Name: produtos produtos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pkey PRIMARY KEY (id_produto);


--
-- TOC entry 4654 (class 2606 OID 16460)
-- Name: compras compras_cpf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_cpf_fkey FOREIGN KEY (cpf) REFERENCES public.clientes(cpf);


--
-- TOC entry 4655 (class 2606 OID 16465)
-- Name: compras compras_id_produto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_id_produto_fkey FOREIGN KEY (id_produto) REFERENCES public.produtos(id_produto);


-- Completed on 2026-03-23 21:43:20

--
-- PostgreSQL database dump complete
--

