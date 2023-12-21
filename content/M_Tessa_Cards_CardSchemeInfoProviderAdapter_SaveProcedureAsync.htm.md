# CardSchemeInfoProviderAdapter.SaveProcedureAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveProcedureAsync(
    	SchemeProcedure procedure,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveProcedureAsync ( 
    	procedure As SchemeProcedure,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveProcedureAsync(
    	SchemeProcedure^ procedure, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveProcedureAsync : 
            procedure : SchemeProcedure * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveProcedureAsync : 
            procedure : SchemeProcedure * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
procedure [SchemeProcedure](T_Tessa_Scheme_SchemeProcedure.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SaveProcedureAsync(SchemeProcedure,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SaveProcedureAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
