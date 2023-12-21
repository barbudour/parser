# ConditionCompilationCache - конструктор
Инициализирует новый экземпляр класса
[ConditionCompilationCache](T_Tessa_Compilation_Conditions_ConditionCompilationCache.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Conditions](N_Tessa_Compilation_Conditions.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public ConditionCompilationCache(
    	IDbScope dbScope,
    	ICardCache cardCache,
    	IConditionCompiler conditionCompiler,
    	[OptionalDependencyAttribute] IUnityDisposableContainer container = null
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	cardCache As ICardCache,
    	conditionCompiler As IConditionCompiler,
    	<OptionalDependencyAttribute> Optional container As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    ConditionCompilationCache(
    	IDbScope^ dbScope, 
    	ICardCache^ cardCache, 
    	IConditionCompiler^ conditionCompiler, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ container = nullptr
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            cardCache : ICardCache * 
            conditionCompiler : IConditionCompiler * 
            [<OptionalDependencyAttribute>] ?container : IUnityDisposableContainer 
    (* Defaults:
            let _container = defaultArg container null
    *)
    -> ConditionCompilationCache
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
conditionCompiler
[IConditionCompiler](T_Tessa_Platform_Conditions_IConditionCompiler.htm)
container
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[ConditionCompilationCache -
](T_Tessa_Compilation_Conditions_ConditionCompilationCache.htm)
[Tessa.Compilation.Conditions - пространство
имён](N_Tessa_Compilation_Conditions.htm)
