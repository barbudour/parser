# ICardFileSourceMapping.Map - метод
Создаёт отображение между файлом с заданными параметрами отображения и
указанным объектом источника контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void Map(
    	Guid fileID,
    	Guid versionRowID,
    	ICardFileContentSource contentSource
    )
VB __Копировать
     Sub Map ( 
    	fileID As Guid,
    	versionRowID As Guid,
    	contentSource As ICardFileContentSource
    )
C++ __Копировать
     void Map(
    	Guid fileID, 
    	Guid versionRowID, 
    	ICardFileContentSource^ contentSource
    )
F# __Копировать
     abstract Map : 
            fileID : Guid * 
            versionRowID : Guid * 
            contentSource : ICardFileContentSource -> unit 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор отображаемого файла.
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор отображаемой версии файла.
contentSource
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm)
    Источник контента файла, для которого строится отображение.
##  __См. также
#### Ссылки
[ICardFileSourceMapping - ](T_Tessa_Cards_ICardFileSourceMapping.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
