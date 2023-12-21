# DeleteTableRowMergeResultItem.ApplyAsync - метод
Применяет результат слияния к объекту.
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.MergeResultItems](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask ApplyAsync(
    	Card o,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function ApplyAsync ( 
    	o As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask ApplyAsync(
    	Card^ o, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract ApplyAsync : 
            o : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override ApplyAsync : 
            o : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
o [Card](T_Tessa_Cards_Card.htm)
    Объект к которому применяется результат миграции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
#### Реализации
[IMergeResultItem<TMergeObject>.ApplyAsync(TMergeObject,
CancellationToken)](M_Tessa_SmartMerge_IMergeResultItem_1_ApplyAsync.htm)  
##  __См. также
#### Ссылки
[DeleteTableRowMergeResultItem -
](T_Tessa_Cards_SmartMerge_MergeResultItems_DeleteTableRowMergeResultItem.htm)
[Tessa.Cards.SmartMerge.MergeResultItems - пространство
имён](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)
