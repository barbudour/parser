# CardMetadataSchemeInfoProvider.GetTablesAsync - метод
Получает все таблицы, доступные в рамках схемы данных текущего объекта.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyCollection<SchemeTable>> GetTablesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTablesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyCollection(Of SchemeTable))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyCollection<SchemeTable^>^> GetTablesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTablesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyCollection<SchemeTable>> 
    override GetTablesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyCollection<SchemeTable>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>>  
Запрошенные таблицы.
#### Реализации
[ICardSchemeInfoProvider.GetTablesAsync(CancellationToken)](M_Tessa_Cards_ICardSchemeInfoProvider_GetTablesAsync.htm)  
##  __См. также
#### Ссылки
[CardMetadataSchemeInfoProvider -
](T_Tessa_Cards_CardMetadataSchemeInfoProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
