# KrTypesCache.GetKrCardTypesAsync - метод
Возвращает типы карточек, которые были указаны в настройках типового решения
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<IReadOnlyList<CardRow>> GetKrCardTypesAsync(
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKrCardTypesAsync ( 
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of CardRow))
C++ __Копировать
     public:
    static ValueTask<IReadOnlyList<CardRow^>^> GetKrCardTypesAsync(
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKrCardTypesAsync : 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<CardRow>> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[CardRow](T_Tessa_Cards_CardRow.htm)>>  
Типы карточек, которые были указаны в настройках типового решения
##  __См. также
#### Ссылки
[KrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
