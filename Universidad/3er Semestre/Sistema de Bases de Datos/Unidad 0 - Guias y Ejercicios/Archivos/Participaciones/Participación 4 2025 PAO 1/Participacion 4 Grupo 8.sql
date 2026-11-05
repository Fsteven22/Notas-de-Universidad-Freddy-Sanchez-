use iswc;

create table if not exists tblResumenPapers(
	nombre varchar(50),
    apellido varchar(50),
    nombre_topico varchar(50),
    cantidad_papers int
);

delimiter %%
create trigger tgrResumenPapers after insert on rel_paper_topic
	for each row
	begin
	set @idpersona_paper=(select PersonID from rel_person_paper where PaperID = new.PaperID);
    set @idtopico_paper = (select TopicID from rel_paper_topic where PaperID = new.PaperID);
    set @nombre = (select FirstName from persons where PerID=@idpersona_paper);
    set @apellido = (select LastName from persons where PerID=@idpersona_paper);
    set @nombre_topico = (select TopicName from topics where TopicID=@idtopico_paper);
    set @total = (select count(*) from rel_person_paper rpp
	inner join papers pp on rpp.PaperID=pp.PaperID
    inner join rel_paper_topic rpt on pp.PaperID=rpt.PaperID 
    where rpp.PersonID=@idpersona_paper and
    rpt.TopicID=@idtopico_paper); 
    insert into tblResumenPapers values (@nombre,@apellido,@nombre_topico,@total);
	end;
%%

drop trigger tgrResumenPapers;

DELIMITER $$
CREATE PROCEDURE spPaper (
  IN PaperID INT,
  IN Title VARCHAR(200),
  IN Abstract MEDIUMTEXT,
  IN URI VARCHAR(200),
  IN Year INT,
  IN Conference INT,
  IN Publish TINYINT(1),
  IN AuthorID INT,
  IN TopicID INT
)
BEGIN  
  INSERT INTO papers (PaperID, Title, Abstract, URI, Year, Conference, Publish)
  VALUES (PaperID, Title, Abstract, URI, Year, Conference, Publish);

  INSERT INTO rel_person_paper (PersonID, PaperID)
  VALUES (AuthorID, PaperID);

  INSERT INTO rel_paper_topic (PaperID, TopicID)
  VALUES (PaperID, TopicID);
END $$
DELIMITER ;

drop procedure spPaper;


call spPaper(16,"hola","ola","ola",2025,23541,1,1,1);

select * from tblResumenPapers;

delete from tblResumenPapers where cantidad_papers=0;