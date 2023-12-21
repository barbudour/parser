# CardSchemeInfoProviderAdapter.GetPartitionsAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IEnumerable<SchemePartition>> GetPartitionsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetPartitionsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of SchemePartition))
C++ __Копировать
     public:
    virtual ValueTask<IEnumerable<SchemePartition^>^> GetPartitionsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetPartitionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemePartition>> 
    override GetPartitionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemePartition>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemePartition](T_Tessa_Scheme_SchemePartition.htm)>>
#### Реализации
[ISchemeService.GetPartitionsAsync(CancellationToken)](M_Tessa_Scheme_ISchemeService_GetPartitionsAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
