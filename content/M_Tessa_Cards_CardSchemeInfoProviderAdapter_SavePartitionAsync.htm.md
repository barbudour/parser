# CardSchemeInfoProviderAdapter.SavePartitionAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SavePartitionAsync(
    	SchemePartition partition,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SavePartitionAsync ( 
    	partition As SchemePartition,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SavePartitionAsync(
    	SchemePartition^ partition, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SavePartitionAsync : 
            partition : SchemePartition * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SavePartitionAsync : 
            partition : SchemePartition * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
partition [SchemePartition](T_Tessa_Scheme_SchemePartition.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SavePartitionAsync(SchemePartition,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SavePartitionAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
