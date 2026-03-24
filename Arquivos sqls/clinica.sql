--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2026-03-23 21:43:10

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
-- TOC entry 220 (class 1259 OID 16547)
-- Name: consulta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.consulta (
    dt_consulta integer,
    valor integer,
    hora integer,
    cpf integer,
    crm integer NOT NULL
);


ALTER TABLE public.consulta OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16542)
-- Name: convenio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.convenio (
    percentual integer,
    nome integer,
    codigo integer NOT NULL
);


ALTER TABLE public.convenio OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16537)
-- Name: medico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medico (
    crm integer NOT NULL,
    nome integer,
    especialidade integer,
    telefone integer
);


ALTER TABLE public.medico OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16530)
-- Name: paciente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paciente (
    cpf integer NOT NULL,
    nome character varying,
    dt_nascimento date,
    endereco character varying,
    telefone integer
);


ALTER TABLE public.paciente OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16552)
-- Name: rel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rel (
    cpf integer,
    codigo integer NOT NULL
);


ALTER TABLE public.rel OWNER TO postgres;

--
-- TOC entry 4818 (class 0 OID 16547)
-- Dependencies: 220
-- Data for Name: consulta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.consulta (dt_consulta, valor, hora, cpf, crm) FROM stdin;
\.


--
-- TOC entry 4817 (class 0 OID 16542)
-- Dependencies: 219
-- Data for Name: convenio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.convenio (percentual, nome, codigo) FROM stdin;
\.


--
-- TOC entry 4816 (class 0 OID 16537)
-- Dependencies: 218
-- Data for Name: medico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medico (crm, nome, especialidade, telefone) FROM stdin;
\.


--
-- TOC entry 4815 (class 0 OID 16530)
-- Dependencies: 217
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paciente (cpf, nome, dt_nascimento, endereco, telefone) FROM stdin;
\.


--
-- TOC entry 4819 (class 0 OID 16552)
-- Dependencies: 221
-- Data for Name: rel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rel (cpf, codigo) FROM stdin;
\.


--
-- TOC entry 4663 (class 2606 OID 16551)
-- Name: consulta consulta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_pkey PRIMARY KEY (crm);


--
-- TOC entry 4661 (class 2606 OID 16546)
-- Name: convenio convenio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.convenio
    ADD CONSTRAINT convenio_pkey PRIMARY KEY (codigo);


--
-- TOC entry 4659 (class 2606 OID 16541)
-- Name: medico medico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (crm);


--
-- TOC entry 4657 (class 2606 OID 16536)
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (cpf);


--
-- TOC entry 4665 (class 2606 OID 16556)
-- Name: rel rel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rel
    ADD CONSTRAINT rel_pkey PRIMARY KEY (codigo);


--
-- TOC entry 4666 (class 2606 OID 16557)
-- Name: consulta consulta_cpf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_cpf_fkey FOREIGN KEY (cpf) REFERENCES public.paciente(cpf);


--
-- TOC entry 4667 (class 2606 OID 16562)
-- Name: consulta consulta_crm_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_crm_fkey FOREIGN KEY (crm) REFERENCES public.medico(crm);


--
-- TOC entry 4668 (class 2606 OID 16572)
-- Name: rel rel_codigo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rel
    ADD CONSTRAINT rel_codigo_fkey FOREIGN KEY (codigo) REFERENCES public.convenio(codigo);


--
-- TOC entry 4669 (class 2606 OID 16567)
-- Name: rel rel_cpf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rel
    ADD CONSTRAINT rel_cpf_fkey FOREIGN KEY (cpf) REFERENCES public.paciente(cpf);


-- Completed on 2026-03-23 21:43:10

--
-- PostgreSQL database dump complete
--

