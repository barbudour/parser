# CardSchemeInfoProviderAdapter.SaveFunctionAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveFunctionAsync(
    	SchemeFunction function,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveFunctionAsync ( 
    	function As SchemeFunction,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveFunctionAsync(
    	SchemeFunction^ function, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveFunctionAsync : 
            function : SchemeFunction * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveFunctionAsync : 
            function : SchemeFunction * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
function [SchemeFunction](T_Tessa_Scheme_SchemeFunction.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISchemeService.SaveFunctionAsync(SchemeFunction,
CancellationToken)](M_Tessa_Scheme_ISchemeService_SaveFunctionAsync.htm)  
##  __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
