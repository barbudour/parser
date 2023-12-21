# CardFileSourceMapping.TryGet - метод
Возвращает источник контента файла для заданных параметров отображения или
null, если отображение не найдено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardFileContentSource TryGet(
    	Guid fileID,
    	Guid versionRowID
    )
VB __Копировать
     Public Function TryGet ( 
    	fileID As Guid,
    	versionRowID As Guid
    ) As ICardFileContentSource
C++ __Копировать
     public:
    virtual ICardFileContentSource^ TryGet(
    	Guid fileID, 
    	Guid versionRowID
    ) sealed
F# __Копировать
     abstract TryGet : 
            fileID : Guid * 
            versionRowID : Guid -> ICardFileContentSource 
    override TryGet : 
            fileID : Guid * 
            versionRowID : Guid -> ICardFileContentSource 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор отображаемого файла.
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор отображаемой версии файла.
#### Возвращаемое значение
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm)  
Источник контента файла для заданных параметров отображения или null, если
отображение не найдено.
#### Реализации
[ICardFileSourceMapping.TryGet(Guid,
Guid)](M_Tessa_Cards_ICardFileSourceMapping_TryGet.htm)  
##  __См. также
#### Ссылки
[CardFileSourceMapping - ](T_Tessa_Cards_CardFileSourceMapping.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
