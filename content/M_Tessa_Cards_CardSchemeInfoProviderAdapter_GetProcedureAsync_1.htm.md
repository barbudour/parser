# CardSchemeInfoProviderAdapter.GetProcedureAsync(String, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeProcedure> GetProcedureAsync(
    	string name,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetProcedureAsync ( 
    	name As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeProcedure)
C++ __Копировать
     public:
    virtual ValueTask<SchemeProcedure^> GetProcedureAsync(
    	String^ name, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetProcedureAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeProcedure> 
    override GetProcedureAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeProcedure> 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeProcedure](T_Tessa_Scheme_SchemeProcedure.htm)>
#### Реализации
[ISchemeService.GetProcedureAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetProcedureAsync_1.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetProcedureAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetProcedureAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
