# CardSchemeInfoProviderAdapter.GetTablesAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IEnumerable<SchemeTable>> GetTablesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTablesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of SchemeTable))
C++ __Копировать
     public:
    virtual ValueTask<IEnumerable<SchemeTable^>^> GetTablesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTablesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemeTable>> 
    override GetTablesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemeTable>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>>
#### Реализации
[ISchemeService.GetTablesAsync(CancellationToken)](M_Tessa_Scheme_ISchemeService_GetTablesAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
