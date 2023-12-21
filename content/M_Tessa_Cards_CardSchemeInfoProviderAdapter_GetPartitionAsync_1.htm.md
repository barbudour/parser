# CardSchemeInfoProviderAdapter.GetPartitionAsync(String, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemePartition> GetPartitionAsync(
    	string name,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetPartitionAsync ( 
    	name As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemePartition)
C++ __Копировать
     public:
    virtual ValueTask<SchemePartition^> GetPartitionAsync(
    	String^ name, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetPartitionAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemePartition> 
    override GetPartitionAsync : 
            name : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemePartition> 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemePartition](T_Tessa_Scheme_SchemePartition.htm)>
#### Реализации
[ISchemeService.GetPartitionAsync(String,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetPartitionAsync_1.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetPartitionAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetPartitionAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
