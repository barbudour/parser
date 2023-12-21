# CardDeleteMethodFilterPolicy.FilterAsync - метод
Возвращает признак того, что выполнение метода с заданным параметром разрешено
для экземпляра расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> FilterAsync(
    	ExtensionBuildKey buildKey,
    	ExtensionResolveKey resolveKey,
    	ExtensionExecutionKey executionKey,
    	IExtensionPolicyContainer policies,
    	IExtension extension,
    	Object extensionContext,
    	Object filterContext
    )
VB __Копировать
     Public Function FilterAsync ( 
    	buildKey As ExtensionBuildKey,
    	resolveKey As ExtensionResolveKey,
    	executionKey As ExtensionExecutionKey,
    	policies As IExtensionPolicyContainer,
    	extension As IExtension,
    	extensionContext As Object,
    	filterContext As Object
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> FilterAsync(
    	ExtensionBuildKey^ buildKey, 
    	ExtensionResolveKey^ resolveKey, 
    	ExtensionExecutionKey executionKey, 
    	IExtensionPolicyContainer^ policies, 
    	IExtension^ extension, 
    	Object^ extensionContext, 
    	Object^ filterContext
    ) sealed
F# __Копировать
     abstract FilterAsync : 
            buildKey : ExtensionBuildKey * 
            resolveKey : ExtensionResolveKey * 
            executionKey : ExtensionExecutionKey * 
            policies : IExtensionPolicyContainer * 
            extension : IExtension * 
            extensionContext : Object * 
            filterContext : Object -> ValueTask<bool> 
    override FilterAsync : 
            buildKey : ExtensionBuildKey * 
            resolveKey : ExtensionResolveKey * 
            executionKey : ExtensionExecutionKey * 
            policies : IExtensionPolicyContainer * 
            extension : IExtension * 
            extensionContext : Object * 
            filterContext : Object -> ValueTask<bool> 
#### Параметры
buildKey [ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm)
    Ключ, используемый для идентификации типа расширения.
resolveKey [ExtensionResolveKey](T_Tessa_Extensions_ExtensionResolveKey.htm)
    Ключ, используемый для идентификации экземпляра расширения.
executionKey
[ExtensionExecutionKey](T_Tessa_Extensions_ExtensionExecutionKey.htm)
    Ключ, используемый для идентификации выполняемого метода.
policies
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер для политик, связанных с экземпляром расширения.
extension [IExtension](T_Tessa_Extensions_IExtension.htm)
    Экземпляр расширения.
extensionContext
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Параметр выполняемого метода.
filterContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Контекст фильтрации расширения.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если выполнение метода для расширения разрешено; false, если выполнение
метода для расширения запрещено.
#### Реализации
[IFilterPolicy.FilterAsync(ExtensionBuildKey, ExtensionResolveKey,
ExtensionExecutionKey, IExtensionPolicyContainer, IExtension, Object,
Object)](M_Tessa_Extensions_IFilterPolicy_FilterAsync.htm)  
##  __См. также
#### Ссылки
[CardDeleteMethodFilterPolicy -
](T_Tessa_Cards_Extensions_CardDeleteMethodFilterPolicy.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
