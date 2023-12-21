# PlaceholderExtensionCompilationCache - конструктор
Инициализирует новый экземпляр класса
[PlaceholderExtensionCompilationCache](T_Tessa_Compilation_Placeholders_PlaceholderExtensionCompilationCache.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Compilation.Placeholders](N_Tessa_Compilation_Placeholders.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public PlaceholderExtensionCompilationCache(
    	IPlaceholderCompilationStorage compilationStorage,
    	IPlaceholderExtensionCompiler compiler,
    	IPlaceholderExtensionScriptDescriptionProvider scriptDescriptionProvider,
    	ICardCache cardCache,
    	[OptionalDependencyAttribute] IUnityDisposableContainer unityDisposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	compilationStorage As IPlaceholderCompilationStorage,
    	compiler As IPlaceholderExtensionCompiler,
    	scriptDescriptionProvider As IPlaceholderExtensionScriptDescriptionProvider,
    	cardCache As ICardCache,
    	<OptionalDependencyAttribute> Optional unityDisposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    PlaceholderExtensionCompilationCache(
    	IPlaceholderCompilationStorage^ compilationStorage, 
    	IPlaceholderExtensionCompiler^ compiler, 
    	IPlaceholderExtensionScriptDescriptionProvider^ scriptDescriptionProvider, 
    	ICardCache^ cardCache, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ unityDisposableContainer = nullptr
    )
F# __Копировать
     new : 
            compilationStorage : IPlaceholderCompilationStorage * 
            compiler : IPlaceholderExtensionCompiler * 
            scriptDescriptionProvider : IPlaceholderExtensionScriptDescriptionProvider * 
            cardCache : ICardCache * 
            [<OptionalDependencyAttribute>] ?unityDisposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _unityDisposableContainer = defaultArg unityDisposableContainer null
    *)
    -> PlaceholderExtensionCompilationCache
#### Параметры
compilationStorage
[IPlaceholderCompilationStorage](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderCompilationStorage.htm)
compiler
[IPlaceholderExtensionCompiler](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderExtensionCompiler.htm)
scriptDescriptionProvider
[IPlaceholderExtensionScriptDescriptionProvider](T_Tessa_Platform_Placeholders_Compilation_IPlaceholderExtensionScriptDescriptionProvider.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
unityDisposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[PlaceholderExtensionCompilationCache -
](T_Tessa_Compilation_Placeholders_PlaceholderExtensionCompilationCache.htm)
[Tessa.Compilation.Placeholders - пространство
имён](N_Tessa_Compilation_Placeholders.htm)
