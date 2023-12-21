# CardSchemeInfoProviderAdapter.GetPartitionAsync(Guid, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemePartition> GetPartitionAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetPartitionAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemePartition)
C++ __Копировать
     public:
    virtual ValueTask<SchemePartition^> GetPartitionAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetPartitionAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemePartition> 
    override GetPartitionAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemePartition> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemePartition](T_Tessa_Scheme_SchemePartition.htm)>
#### Реализации
[ISchemeService.GetPartitionAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetPartitionAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetPartitionAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetPartitionAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
