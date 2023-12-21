# CardFileVersionStrategy.GetVersionsAsync - метод
Возвращает список с общей информацией по версиям файла с заданным
идентификатором.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IList<ICardFileVersionInfo>> GetVersionsAsync(
    	Guid fileID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetVersionsAsync ( 
    	fileID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IList(Of ICardFileVersionInfo))
C++ __Копировать
     public:
    virtual Task<IList<ICardFileVersionInfo^>^>^ GetVersionsAsync(
    	Guid fileID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetVersionsAsync : 
            fileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<ICardFileVersionInfo>> 
    override GetVersionsAsync : 
            fileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<ICardFileVersionInfo>> 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, список версий которого требуется получить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ICardFileVersionInfo](T_Tessa_Cards_ComponentModel_ICardFileVersionInfo.htm)>>  
Список с общей информацией по версиям файла с заданным идентификатором.
#### Реализации
[ICardFileVersionStrategy.GetVersionsAsync(Guid,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_GetVersionsAsync.htm)  
##  __См. также
#### Ссылки
[CardFileVersionStrategy -
](T_Tessa_Cards_ComponentModel_CardFileVersionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
