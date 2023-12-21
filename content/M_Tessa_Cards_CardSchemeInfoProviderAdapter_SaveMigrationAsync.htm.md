# CardSchemeInfoProviderAdapter.SaveMigrationAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveMigrationAsync(
    	SchemeMigration migration,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveMigrationAsync ( 
    	migration As SchemeMigration,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveMigrationAsync(
    	SchemeMigration^ migration, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveMigrationAsync : 
            migration : SchemeMigration * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveMigrationAsync : 
            migration : SchemeMigration * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
migration [SchemeMigration](T_Tessa_Scheme_SchemeMigration.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SaveMigrationAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SaveMigrationAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
