# WfHelper.GetUsedComponentsAsync - метод
Возвращает используемые компоненты типового решения, по которым можно
определить возможность использования резолюций и других бизнес-процессов
Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<KrComponents> GetUsedComponentsAsync(
    	IKrTypesCache krTypesCache,
    	Card card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetUsedComponentsAsync ( 
    	krTypesCache As IKrTypesCache,
    	card As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of KrComponents)
C++ __Копировать
     public:
    static ValueTask<KrComponents> GetUsedComponentsAsync(
    	IKrTypesCache^ krTypesCache, 
    	Card^ card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetUsedComponentsAsync : 
            krTypesCache : IKrTypesCache * 
            card : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<KrComponents> 
#### Параметры
krTypesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
     Кэш с настройками типового решения. Не может быть равен null. 
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой требуется получить компоненты типового решения. По данным карточки определяется идентификатор типа документа. Не может быть равна null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[KrComponents](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponents.htm)>  
Используемые компоненты типового решения, по которым можно определить
возможность использования резолюций и других бизнес-процессов Workflow.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
