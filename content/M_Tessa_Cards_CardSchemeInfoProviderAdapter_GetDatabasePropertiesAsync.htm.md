# CardSchemeInfoProviderAdapter.GetDatabasePropertiesAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeDatabaseProperties> GetDatabasePropertiesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetDatabasePropertiesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeDatabaseProperties)
C++ __Копировать
     public:
    virtual ValueTask<SchemeDatabaseProperties^> GetDatabasePropertiesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetDatabasePropertiesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeDatabaseProperties> 
    override GetDatabasePropertiesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeDatabaseProperties> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeDatabaseProperties](T_Tessa_Scheme_SchemeDatabaseProperties.htm)>
#### Реализации
[ISchemeService.GetDatabasePropertiesAsync(CancellationToken)](M_Tessa_Scheme_ISchemeService_GetDatabasePropertiesAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
