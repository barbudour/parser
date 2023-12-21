# CardSchemeInfoProviderAdapter.SaveTableAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveTableAsync(
    	SchemeTable table,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveTableAsync ( 
    	table As SchemeTable,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveTableAsync(
    	SchemeTable^ table, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveTableAsync : 
            table : SchemeTable * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveTableAsync : 
            table : SchemeTable * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
table [SchemeTable](T_Tessa_Scheme_SchemeTable.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SaveTableAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SaveTableAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
