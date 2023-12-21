# CardFileTypeFilterPolicy.GetFilterContextAsync - метод
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<Object> GetFilterContextAsync(
    	ExtensionBuildKey buildKey,
    	ExtensionExecutionKey executionKey,
    	IExtensionPolicyContainer policies,
    	Object extensionContext
    )
VB __Копировать
     Public Function GetFilterContextAsync ( 
    	buildKey As ExtensionBuildKey,
    	executionKey As ExtensionExecutionKey,
    	policies As IExtensionPolicyContainer,
    	extensionContext As Object
    ) As ValueTask(Of Object)
C++ __Копировать
     public:
    virtual ValueTask<Object^> GetFilterContextAsync(
    	ExtensionBuildKey^ buildKey, 
    	ExtensionExecutionKey executionKey, 
    	IExtensionPolicyContainer^ policies, 
    	Object^ extensionContext
    ) sealed
F# __Копировать
     abstract GetFilterContextAsync : 
            buildKey : ExtensionBuildKey * 
            executionKey : ExtensionExecutionKey * 
            policies : IExtensionPolicyContainer * 
            extensionContext : Object -> ValueTask<Object> 
    override GetFilterContextAsync : 
            buildKey : ExtensionBuildKey * 
            executionKey : ExtensionExecutionKey * 
            policies : IExtensionPolicyContainer * 
            extensionContext : Object -> ValueTask<Object> 
#### Параметры
buildKey [ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm)
    Ключ, используемый для идентификации типа расширения.
executionKey
[ExtensionExecutionKey](T_Tessa_Extensions_ExtensionExecutionKey.htm)
    Ключ, используемый для идентификации выполняемого метода.
policies
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер для политик, связанных с типом расширения.
extensionContext
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Параметр выполняемого метода.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Контекст фильтрации, используемый для определение разрешений на выполнение
метода для экземпляров расширений.
#### Реализации
[IFilterPolicy.GetFilterContextAsync(ExtensionBuildKey, ExtensionExecutionKey,
IExtensionPolicyContainer,
Object)](M_Tessa_Extensions_IFilterPolicy_GetFilterContextAsync.htm)  
##  __См. также
#### Ссылки
[CardFileTypeFilterPolicy -
](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
