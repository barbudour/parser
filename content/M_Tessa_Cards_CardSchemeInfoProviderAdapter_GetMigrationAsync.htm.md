# CardSchemeInfoProviderAdapter.GetMigrationAsync(Guid, CancellationToken) -
метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<SchemeMigration> GetMigrationAsync(
    	Guid id,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMigrationAsync ( 
    	id As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SchemeMigration)
C++ __Копировать
     public:
    virtual ValueTask<SchemeMigration^> GetMigrationAsync(
    	Guid id, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetMigrationAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeMigration> 
    override GetMigrationAsync : 
            id : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SchemeMigration> 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SchemeMigration](T_Tessa_Scheme_SchemeMigration.htm)>
#### Реализации
[ISchemeService.GetMigrationAsync(Guid,
CancellationToken)](M_Tessa_Scheme_ISchemeService_GetMigrationAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[GetMigrationAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter_GetMigrationAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
