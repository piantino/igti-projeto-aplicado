select proc.cdprocesso CODIGO,
proc.nuprocesso PROCESSO, 
--tjsc_seqprocesso(proc.cdprocesso),
matde.DEMATERIA GABINETE,
espmat.DEESPECMATERIA ROTULO_MANUAL
from SAJ.EFSGPROCESSO proc
join SAJ.EFSGPROCMATERIA mat on proc.cdprocesso = mat.cdprocesso and mat.CDFORO = 900
join SAJ.EFSGMATERIA matde on mat.CDMATERIA = matde.CDMATERIA and mat.cdlocal = matde.cdlocal and mat.CDTIPOLOCAL = matde.CDTIPOLOCAL
join SAJ.EFSGESPECMATERIA espmat on mat.CDMATERIA = espmat.CDMATERIA and mat.CDESPECMATERIA = espmat.CDESPECMATERIA and mat.CDLOCAL = espmat.CDLOCAL and mat.CDTIPOLOCAL = matde.CDTIPOLOCAL
where 
proc.FLTIPOCLASSE <> 5 and proc.cdprocesso in
(
  select dist.cdprocesso from SAJ.EFSGDISTPROCESSO dist 
  where dist.cdprocesso = proc.cdprocesso and
  dist.CDFORO = 900 and dist.CDVARA = 29
  and dist.DTDISTRIBUICAO >= TO_DATE('01/01/2018', 'dd/mm/yyyy')
)
AND REGEXP_LIKE(espmat.DEESPECMATERIA, '^[A-Z]{3,5}$')
AND espmat.DEESPECMATERIA not in ('Geral', 'ICMS');


select 
espmat.DEESPECMATERIA ROTULO_MANUAL,
count(*)
from SAJ.EFSGPROCESSO proc
join SAJ.EFSGPROCMATERIA mat on proc.cdprocesso = mat.cdprocesso and mat.CDFORO = 900
join SAJ.EFSGMATERIA matde on mat.CDMATERIA = matde.CDMATERIA and mat.cdlocal = matde.cdlocal and mat.CDTIPOLOCAL = matde.CDTIPOLOCAL
join SAJ.EFSGESPECMATERIA espmat on mat.CDMATERIA = espmat.CDMATERIA and mat.CDESPECMATERIA = espmat.CDESPECMATERIA and mat.CDLOCAL = espmat.CDLOCAL and mat.CDTIPOLOCAL = matde.CDTIPOLOCAL
where 
proc.FLTIPOCLASSE <> 5 and proc.cdprocesso in
(
  select dist.cdprocesso from SAJ.EFSGDISTPROCESSO dist 
  where dist.cdprocesso = proc.cdprocesso and
  dist.CDFORO = 900 and dist.CDVARA = 29
  and dist.DTDISTRIBUICAO >= TO_DATE('01/01/2018', 'dd/mm/yyyy')
)
AND REGEXP_LIKE(espmat.DEESPECMATERIA, '^[A-Z]{3,5}$')
AND espmat.DEESPECMATERIA not in ('Geral', 'ICMS')
group by espmat.DEESPECMATERIA
order by 2 desc;