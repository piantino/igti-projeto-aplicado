-- Base: acordao
-- Serviço: ojuris_suporte.world

select
          cdprocesso codigo,
          nuprocesso processo,
          dtmovimentacao movimentacao,
          relator,
          orgaojulgador,
          dtjulgamento julgamento,
          foro,
          vara,
          comarca,
          ementa ementa
          from documentos_saj5
          where
          ementa is not null
          AND (ORGAOJULGADOR LIKE '%Direito Civil%' OR ORGAOJULGADOR LIKE '%Direito Comercial%')