# CardSchemeInfoProviderAdapter.SaveDatabasePropertiesAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveDatabasePropertiesAsync(
    	SchemeDatabaseProperties properties,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveDatabasePropertiesAsync ( 
    	properties As SchemeDatabaseProperties,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveDatabasePropertiesAsync(
    	SchemeDatabaseProperties^ properties, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveDatabasePropertiesAsync : 
            properties : SchemeDatabaseProperties * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveDatabasePropertiesAsync : 
            properties : SchemeDatabaseProperties * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
properties
[SchemeDatabaseProperties](T_Tessa_Scheme_SchemeDatabaseProperties.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SaveDatabasePropertiesAsync(SchemeDatabaseProperties,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SaveDatabasePropertiesAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
