# IKrTypesCache.InvalidateAsync - метод
Сбрасывает кэш типов. При следующем их запросе они будут перерасчитаны.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     Task InvalidateAsync(
    	bool cardTypes = false,
    	bool docTypes = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InvalidateAsync ( 
    	Optional cardTypes As Boolean = false,
    	Optional docTypes As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InvalidateAsync(
    	bool cardTypes = false, 
    	bool docTypes = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InvalidateAsync : 
            ?cardTypes : bool * 
            ?docTypes : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardTypes = defaultArg cardTypes false
            let _docTypes = defaultArg docTypes false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypes [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Выполняет сброс кэша типов карточек.
docTypes [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Выполняет сброс кэша типов документов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IKrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
