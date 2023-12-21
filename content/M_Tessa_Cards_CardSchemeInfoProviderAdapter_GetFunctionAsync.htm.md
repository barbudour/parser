# CardSchemeInfoProviderAdapter.GetFunctionAsync(Guid, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeFunction> GetFunctionAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFunctionAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeFunction)
C++ __Копировать
     public:
    virtual ValueTask<SchemeFunction^> GetFunctionAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFunctionAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeFunction> 
    override GetFunctionAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeFunction> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeFunction](T_Tessa_Scheme_SchemeFunction.htm)>
#### Реализации
[ISchemeService.GetFunctionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetFunctionAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetFunctionAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetFunctionAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
