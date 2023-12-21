# CardSchemeInfoProviderAdapter.GetTableAsync(Guid, CancellationToken) - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeTable> GetTableAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTableAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeTable)
C++ __Копировать
     public:
    virtual ValueTask<SchemeTable^> GetTableAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTableAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
    override GetTableAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>
#### Реализации
[ISchemeService.GetTableAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetTableAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetTableAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetTableAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
