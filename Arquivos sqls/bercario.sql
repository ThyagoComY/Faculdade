--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2026-03-23 21:42:46

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
-- TOC entry 219 (class 1259 OID 16401)
-- Name: bebe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bebe (
    cpf integer NOT NULL,
    dt_nasc_bebe date,
    peso integer,
    altura integer,
    mae_do_bebe integer,
    med_do_bebe integer,
    nome_bebe integer,
    id_mae integer,
    id_medico integer
);


ALTER TABLE public.bebe OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16394)
-- Name: mae; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mae (
    dt_nasc_mae integer,
    endereco integer,
    telefone_mae integer,
    cpf integer NOT NULL,
    nome_mae character varying
);


ALTER TABLE public.mae OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16389)
-- Name: medico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medico (
    crm integer NOT NULL,
    nome_med integer,
    telefone_med integer,
    especialidade integer
);


ALTER TABLE public.medico OWNER TO postgres;

--
-- TOC entry 4803 (class 0 OID 16401)
-- Dependencies: 219
-- Data for Name: bebe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bebe (cpf, dt_nasc_bebe, peso, altura, mae_do_bebe, med_do_bebe, nome_bebe, id_mae, id_medico) FROM stdin;
\.


--
-- TOC entry 4802 (class 0 OID 16394)
-- Dependencies: 218
-- Data for Name: mae; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mae (dt_nasc_mae, endereco, telefone_mae, cpf, nome_mae) FROM stdin;
\.


--
-- TOC entry 4801 (class 0 OID 16389)
-- Dependencies: 217
-- Data for Name: medico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medico (crm, nome_med, telefone_med, especialidade) FROM stdin;
\.


--
-- TOC entry 4653 (class 2606 OID 16405)
-- Name: bebe bebe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bebe
    ADD CONSTRAINT bebe_pkey PRIMARY KEY (cpf);


--
-- TOC entry 4651 (class 2606 OID 16400)
-- Name: mae mae_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mae
    ADD CONSTRAINT mae_pkey PRIMARY KEY (cpf);


--
-- TOC entry 4649 (class 2606 OID 16393)
-- Name: medico medico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (crm);


--
-- TOC entry 4654 (class 2606 OID 16406)
-- Name: bebe bebe_id_mae_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bebe
    ADD CONSTRAINT bebe_id_mae_fkey FOREIGN KEY (id_mae) REFERENCES public.mae(cpf);


--
-- TOC entry 4655 (class 2606 OID 16411)
-- Name: bebe bebe_id_medico_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bebe
    ADD CONSTRAINT bebe_id_medico_fkey FOREIGN KEY (id_medico) REFERENCES public.medico(crm);


-- Completed on 2026-03-23 21:42:47

--
-- PostgreSQL database dump complete
--

