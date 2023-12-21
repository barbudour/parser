# CardSchemeInfoProviderAdapter.GetTableAsync(String, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeTable> GetTableAsync(
    	string name,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTableAsync ( 
    	name As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeTable)
C++ __Копировать
     public:
    virtual ValueTask<SchemeTable^> GetTableAsync(
    	String^ name, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTableAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
    override GetTableAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeTable> 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>
#### Реализации
[ISchemeService.GetTableAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetTableAsync_1.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetTableAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetTableAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
