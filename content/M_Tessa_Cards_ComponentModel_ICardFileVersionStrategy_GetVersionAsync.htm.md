# ICardFileVersionStrategy.GetVersionAsync - метод
Возвращает общую информацию по версии файла с заданным идентификатором.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ICardFileVersionInfo> GetVersionAsync(
    	Guid versionRowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetVersionAsync ( 
    	versionRowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardFileVersionInfo)
C++ __Копировать
    Task<ICardFileVersionInfo^>^ GetVersionAsync(
    	Guid versionRowID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetVersionAsync : 
            versionRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardFileVersionInfo> 
#### Параметры
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла, информацию о которой требуется получить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardFileVersionInfo](T_Tessa_Cards_ComponentModel_ICardFileVersionInfo.htm)>  
Общая информация по версии файла с заданным идентификатором.
##  __См. также
#### Ссылки
[ICardFileVersionStrategy -
](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
