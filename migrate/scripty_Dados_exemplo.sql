USE financas;

INSERT INTO tb_usuarios (login, senha) VALUES 
('Giovanni', 'giovanni00'),
('AnaMaria', 'senha123'),
('CarlosEduardo', 'carlos2026'),
('BeatrizLima', 'bea45678');


INSERT INTO tb_categorias (login, tipo) VALUES 
('Giovanni', 'Transporte'),       
('Giovanni', 'Alimentação'),      
('AnaMaria', 'Moradia'),          
('AnaMaria', 'Saúde'),            
('CarlosEduardo', 'Lazer'),       
('CarlosEduardo', 'Educação'),    
('BeatrizLima', 'Alimentação'),   
('BeatrizLima', 'Transporte');    


INSERT INTO tb_dispesas (id_categoria, valor, descricao, data, hora) VALUES 
(1, 5.00, 'Passagem de ônibus', '2026-09-10', '08:30:00'),
(1, 45.00, 'Recarga de bilhete único', '2026-09-15', '09:10:00'),
(2, 25.50, 'Almoço no restaurante', '2026-09-10', '12:15:00'),
(2, 12.00, 'Café da tarde', '2026-09-11', '16:00:00'),


(3, 1250.00, 'Aluguel do apartamento', '2026-09-05', '10:00:00'),
(3, 180.30, 'Conta de energia', '2026-09-10', '14:20:00'),
(4, 85.00, 'Medicamentos na farmácia', '2026-09-12', '18:45:00'),


(5, 60.00, 'Ingresso de cinema', '2026-09-18', '20:30:00'),
(5, 120.00, 'Jantar de fim de semana', '2026-09-20', '21:15:00'),
(6, 350.00, 'Mensalidade do curso', '2026-09-01', '08:00:00'),


(7, 310.45, 'Compras de mercado', '2026-09-08', '11:00:00'),
(8, 28.90, 'Corrida de aplicativo', '2026-09-14', '19:50:00');