# WfHelper.TypeSupportsWorkflowAsync - метод
Возвращает признак того, что тип поддерживает бизнес-процессы Workflow, на
основании настроек типового решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> TypeSupportsWorkflowAsync(
    	IKrTypesCache krTypesCache,
    	CardType cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TypeSupportsWorkflowAsync ( 
    	krTypesCache As IKrTypesCache,
    	cardType As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> TypeSupportsWorkflowAsync(
    	IKrTypesCache^ krTypesCache, 
    	CardType^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TypeSupportsWorkflowAsync : 
            krTypesCache : IKrTypesCache * 
            cardType : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
krTypesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
     Кэш с настройками типового решения. Не может быть равен null. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки, который требуется проверить. Может быть равен null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если тип поддерживает бизнес-процессы Workflow; false в противном
случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
