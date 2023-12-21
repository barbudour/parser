# IFilterPolicy.GetFilterContextAsync - метод
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<Object> GetFilterContextAsync(
    	ExtensionBuildKey buildKey,
    	ExtensionExecutionKey executionKey,
    	IExtensionPolicyContainer policies,
    	Object extensionContext
    )
VB __Копировать
     Function GetFilterContextAsync ( 
    	buildKey As ExtensionBuildKey,
    	executionKey As ExtensionExecutionKey,
    	policies As IExtensionPolicyContainer,
    	extensionContext As Object
    ) As ValueTask(Of Object)
C++ __Копировать
     ValueTask<Object^> GetFilterContextAsync(
    	ExtensionBuildKey^ buildKey, 
    	ExtensionExecutionKey executionKey, 
    	IExtensionPolicyContainer^ policies, 
    	Object^ extensionContext
    )
F# __Копировать
     abstract GetFilterContextAsync : 
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
##  __См. также
#### Ссылки
[IFilterPolicy - ](T_Tessa_Extensions_IFilterPolicy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
