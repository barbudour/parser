# CardSchemeInfoProviderAdapter.RemoveMigrationAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> RemoveMigrationAsync(
    	SchemeMigration migration,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RemoveMigrationAsync ( 
    	migration As SchemeMigration,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ RemoveMigrationAsync(
    	SchemeMigration^ migration, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RemoveMigrationAsync : 
            migration : SchemeMigration * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override RemoveMigrationAsync : 
            migration : SchemeMigration * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
migration [SchemeMigration](T_Tessa_Scheme_SchemeMigration.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[ISchemeService.RemoveMigrationAsync(SchemeMigration,
CancellationToken)](M_Tessa_Scheme_ISchemeService_RemoveMigrationAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
