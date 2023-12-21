# CardSchemeInfoProviderAdapter.RemoveTableAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> RemoveTableAsync(
    	SchemeTable table,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RemoveTableAsync ( 
    	table As SchemeTable,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ RemoveTableAsync(
    	SchemeTable^ table, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RemoveTableAsync : 
            table : SchemeTable * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override RemoveTableAsync : 
            table : SchemeTable * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
table [SchemeTable](T_Tessa_Scheme_SchemeTable.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[ISchemeService.RemoveTableAsync(SchemeTable,
CancellationToken)](M_Tessa_Scheme_ISchemeService_RemoveTableAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
