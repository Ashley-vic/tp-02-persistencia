from datetime import datetime, date
from Database import create_db_and_tables, get_session
from Models import Evento, Palestrante, Participante, Sessao, Inscricao
from uuid import uuid4


def populate_database():
    with get_session() as session:
        
        eventos = [
            Evento(
                nome="Semana da Computação",
                data_inicio=date(2025, 3, 10),
                data_termino=date(2025, 3, 15),
                local="Auditório Central - Campus A",
                descricao="Evento voltado à troca de conhecimentos em tecnologia e inovação."
            ),
            Evento(
                nome="Workshop de Inteligência Artificial",
                data_inicio=date(2025, 4, 5),
                data_termino=date(2025, 4, 5),
                local="Sala 202 - Bloco B",
                descricao="Workshop sobre aplicações práticas de IA no mercado."
            ),
            Evento(
                nome="Hackathon de Desenvolvimento Web",
                data_inicio=date(2025, 5, 20),
                data_termino=date(2025, 5, 22),
                local="Laboratório de Informática - Campus C",
                descricao="Competição para desenvolver soluções inovadoras em 48 horas."
            ),
            Evento(
                nome="Fórum de Educação e Tecnologia",
                data_inicio=date(2025, 6, 1),
                data_termino=date(2025, 6, 3),
                local="Centro de Convenções",
                descricao="Discussões sobre o impacto da tecnologia na educação."
            ),
            Evento(
                nome="Seminário de Redes de Computadores",
                data_inicio=date(2025, 7, 15),
                data_termino=date(2025, 7, 15),
                local="Auditório de Engenharia",
                descricao="Seminário sobre avanços em redes e conectividade."
            ),
            Evento(
                nome="Palestra sobre DevOps",
                data_inicio=date(2025, 8, 10),
                data_termino=date(2025, 8, 10),
                local="Sala de Conferências - Bloco D",
                descricao="Introdução aos conceitos e práticas de DevOps."
            ),
            Evento(
                nome="Congresso de Ciência de Dados",
                data_inicio=date(2025, 9, 18),
                data_termino=date(2025, 9, 20),
                local="Auditório Principal",
                descricao="Congresso sobre tendências e desafios em ciência de dados."
            ),
            Evento(
                nome="Maratona de Programação",
                data_inicio=date(2025, 10, 10),
                data_termino=date(2025, 10, 11),
                local="Laboratório de Computação",
                descricao="Desafio de programação para estudantes universitários."
            ),
            Evento(
                nome="Semana de Segurança da Informação",
                data_inicio=date(2025, 11, 5),
                data_termino=date(2025, 11, 7),
                local="Centro Acadêmico de Tecnologia",
                descricao="Discussões sobre ameaças e proteções no mundo digital."
            ),
            Evento(
                nome="Encontro de Desenvolvedores Mobile",
                data_inicio=date(2025, 12, 12),
                data_termino=date(2025, 12, 12),
                local="Sala de Workshop - Bloco F",
                descricao="Exploração de novas ferramentas e frameworks para mobile."
            )
        ]
        session.add_all(eventos)
        session.commit()

        
        palestrantes = [
            Palestrante(nome="Carlos Eduardo", email="carlos.eduardo@tech.com", biografia="Engenheiro de software com 10 anos de experiência em IA."),
            Palestrante(nome="Mariana Souza", email="mariana.souza@dev.com", biografia="Especialista em desenvolvimento web e palestrante internacional."),
            Palestrante(nome="João Batista", email="joao.batista@cloud.com", biografia="Arquiteto de soluções em computação em nuvem."),
            Palestrante(nome="Ana Clara", email="ana.clara@security.com", biografia="Pesquisadora em segurança da informação."),
            Palestrante(nome="Rafael Lima", email="rafael.lima@data.com", biografia="Cientista de dados com foco em machine learning."),
            Palestrante(nome="Gabriela Almeida", email="gabriela.almeida@devops.com", biografia="Consultora em práticas de DevOps."),
            Palestrante(nome="Vinícius Santos", email="vinicius.santos@networks.com", biografia="Especialista em redes de computadores."),
            Palestrante(nome="Laura Martins", email="laura.martins@mobile.com", biografia="Desenvolvedora mobile e instrutora."),
            Palestrante(nome="Pedro Henrique", email="pedro.henrique@workshop.com", biografia="Organizador de workshops e eventos acadêmicos."),
            Palestrante(nome="Julia Pereira", email="julia.pereira@edu.com", biografia="Professora e entusiasta em educação e tecnologia.")
        ]
        session.add_all(palestrantes)
        session.commit()

        participantes = [
            Participante(nome="Lucas Silva", email="lucas.silva@example.com", instituicao="Universidade Federal de Tecnologia"),
            Participante(nome="Beatriz Santos", email="beatriz.santos@example.com", instituicao="Instituto de Tecnologia e Inovação"),
            Participante(nome="Fernando Costa", email="fernando.costa@example.com", instituicao="Centro Universitário de Engenharia"),
            Participante(nome="Juliana Oliveira", email="juliana.oliveira@example.com", instituicao="Faculdade de Informática Aplicada"),
            Participante(nome="Rafael Pereira", email="rafael.pereira@example.com", instituicao="Escola de Computação Avançada"),
            Participante(nome="Camila Alves", email="camila.alves@example.com", instituicao="Universidade Estadual de Tecnologia"),
            Participante(nome="Diego Matos", email="diego.matos@example.com", instituicao="Faculdade de Tecnologia Digital"),
            Participante(nome="Patrícia Rocha", email="patricia.rocha@example.com", instituicao="Instituto Superior de Sistemas"),
            Participante(nome="Leonardo Almeida", email="leonardo.almeida@example.com", instituicao="Universidade de Ciências da Computação"),
            Participante(nome="Carolina Ribeiro", email="carolina.ribeiro@example.com", instituicao="Centro Tecnológico de Programação")
        ]
        session.add_all(participantes)
        session.commit()

        sessoes = [
            Sessao(nome="Introdução à IA", data_hora=datetime(2025, 3, 10, 9, 0), evento_id=eventos[0].id, palestrante_id=palestrantes[0].id),
            Sessao(nome="Redes de Computadores Avançadas", data_hora=datetime(2025, 7, 15, 14, 0), evento_id=eventos[4].id, palestrante_id=palestrantes[6].id),
            Sessao(nome="Práticas de DevOps", data_hora=datetime(2025, 8, 10, 10, 0), evento_id=eventos[5].id, palestrante_id=palestrantes[5].id),
            Sessao(nome="Segurança da Informação: O Futuro", data_hora=datetime(2025, 11, 5, 11, 0), evento_id=eventos[8].id, palestrante_id=palestrantes[3].id),
            Sessao(nome="Data Science na Prática", data_hora=datetime(2025, 9, 18, 16, 0), evento_id=eventos[6].id, palestrante_id=palestrantes[4].id),
            Sessao(nome="Mobile: Frameworks Modernos", data_hora=datetime(2025, 12, 12, 13, 0), evento_id=eventos[9].id, palestrante_id=palestrantes[7].id),
        ]
        session.add_all(sessoes)
        session.commit()

        inscricoes = [
            Inscricao(evento_id=eventos[0].id, participante_id=participantes[0].id),
            Inscricao(evento_id=eventos[1].id, participante_id=participantes[1].id),
            Inscricao(evento_id=eventos[2].id, participante_id=participantes[2].id),
            Inscricao(evento_id=eventos[3].id, participante_id=participantes[3].id),
            Inscricao(evento_id=eventos[4].id, participante_id=participantes[4].id),
        ]
        session.add_all(inscricoes)
        session.commit()


if __name__ == "__main__":
    create_db_and_tables()
    populate_database()
