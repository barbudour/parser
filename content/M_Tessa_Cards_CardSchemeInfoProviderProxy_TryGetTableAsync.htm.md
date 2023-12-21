# CardSchemeInfoProviderProxy.TryGetTableAsync - метод
Возвращает таблицу по идентификатору или null, если таблица не найдена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeTable> TryGetTableAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetTableAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeTable)
C++ __Копировать
     public:
    virtual ValueTask<SchemeTable^> TryGetTableAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetTableAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
    override TryGetTableAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор таблицы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>  
Запрошенная таблица или null, если таблица не найдена.
#### Реализации
[ICardSchemeInfoProvider.TryGetTableAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardSchemeInfoProvider_TryGetTableAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderProxy -
](T_Tessa_Cards_CardSchemeInfoProviderProxy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
