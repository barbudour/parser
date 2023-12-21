# CardSchemeInfoProviderAdapter.GetMigrationsAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IEnumerable<SchemeMigration>> GetMigrationsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMigrationsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of SchemeMigration))
C++ __Копировать
     public:
    virtual ValueTask<IEnumerable<SchemeMigration^>^> GetMigrationsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetMigrationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemeMigration>> 
    override GetMigrationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<SchemeMigration>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeMigration](T_Tessa_Scheme_SchemeMigration.htm)>>
#### Реализации
[ISchemeService.GetMigrationsAsync(CancellationToken)](M_Tessa_Scheme_ISchemeService_GetMigrationsAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
