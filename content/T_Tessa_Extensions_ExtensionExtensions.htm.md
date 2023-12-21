# ExtensionExtensions - класс
Методы-расширения для пространства имён Tessa.Extensions.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ExtensionExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ExtensionExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class ExtensionExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ExtensionExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExtensionExtensions
##  __Методы
[FindAndRegisterExtensionsOnClient](M_Tessa_Extensions_ExtensionExtensions_FindAndRegisterExtensionsOnClient.htm)|
Выполняет поиск и исполнение клиентских регистраторов расширений в папке
приложения.  
---|---  
[FindAndRegisterExtensionsOnServer](M_Tessa_Extensions_ExtensionExtensions_FindAndRegisterExtensionsOnServer.htm)|
Выполняет поиск и исполнение серверных регистраторов расширений в папке
приложения.  
[OrderBySpecifiedOrder](M_Tessa_Extensions_ExtensionExtensions_OrderBySpecifiedOrder.htm)|
Упорядочивает типы
[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm) по
их явно заданному порядку.  
[RegisterDefaults](M_Tessa_Extensions_ExtensionExtensions_RegisterDefaults.htm)|
Регистрирует стратегии и политики по умолчанию для этапов
[Initialize](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Regulate](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Resolve](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Filter](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Execute](T_Tessa_Extensions_ExtensionStrategyStage.htm) и
[TearDown](T_Tessa_Extensions_ExtensionStrategyStage.htm).  
[RegisterExtensionContainers](M_Tessa_Extensions_ExtensionExtensions_RegisterExtensionContainers.htm)|
Выполняет регистрацию контейнеров расширений в контейнере Unity. В контейнере
гарантированно зарегистрированы зависимости по умолчанию
[RegisterDefaults(IExtensionContainer)](M_Tessa_Extensions_ExtensionExtensions_RegisterDefaults.htm).  
[ResolveAssemblyInfo](M_Tessa_Extensions_ExtensionExtensions_ResolveAssemblyInfo.htm)|
Получает объект
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm) с
информацией по сборкам из контейнера Unity. Если объект не зарегистрирован, то
создаёт новый объект, регистрирует его и возвращает.  
[WhenFunc(IExtensionPolicyContainer, Func<IExtensionContext,
Boolean>)](M_Tessa_Extensions_ExtensionExtensions_WhenFunc.htm)|  Регистрирует
политику фильтрации выполнения методов любых расширений
[IExtension](T_Tessa_Extensions_IExtension.htm) в соответствии с функцией
isAllowedFunc, которая проверяет контекст расширений. Если зарегистрировано
несколько политик, то должны выполняться все из них.  
[WhenFunc<TContext>(IExtensionPolicyContainer, Func<TContext,
Boolean>)](M_Tessa_Extensions_ExtensionExtensions_WhenFunc__1.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IExtension](T_Tessa_Extensions_IExtension.htm), принимающих указанный тип
контекста TContext, в соответствии с функцией isAllowedFunc, которая проверяет
контекст расширений. Если зарегистрировано несколько политик, то должны
выполняться все из них. Если тип контекста отличается от указанного, то
политика игнорируется, т.е. возвращает true.  
[WithDefaultConstructor](M_Tessa_Extensions_ExtensionExtensions_WithDefaultConstructor.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством их конструкторов по умолчанию. Если класс расширения реализует
интерфейс [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то
для каждого созданного экземпляра будет вызвана асинхронная инициализация.  
[WithFunc](M_Tessa_Extensions_ExtensionExtensions_WithFunc.htm)|  Регистрирует
политику, указывающую на способ получения экземпляров расширений посредством
заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию непосредственно
внутри функции.  
[WithInstance](M_Tessa_Extensions_ExtensionExtensions_WithInstance.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданной ссылки на этот экземпляр. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию перед тем, как
передать экземпляр расширения в этот метод.  
[WithLazy(IExtensionPolicyContainer,
Func<Task<IExtension>>)](M_Tessa_Extensions_ExtensionExtensions_WithLazy.htm)|
Регистрирует политику, указывающую на способ отложенного получения экземпляров
расширений посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию внутри лямбда-
выражения.  
[WithLazy(IExtensionPolicyContainer,
Func<IExtension>)](M_Tessa_Extensions_ExtensionExtensions_WithLazy_1.htm)|
Регистрирует политику, указывающую на способ отложенного получения экземпляров
расширений посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
[WithLazy(IExtensionPolicyContainer,
Lazy<IExtension>)](M_Tessa_Extensions_ExtensionExtensions_WithLazy_2.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством отложенной ссылки на экземпляр расширения. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
[WithLazy(IExtensionPolicyContainer,
AsyncLazy<IExtension>)](M_Tessa_Extensions_ExtensionExtensions_WithLazy_3.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством отложенной ссылки на экземпляр расширения. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию в лямбда-выражении,
переданном в другую реализацию метода.  
[WithOrder](M_Tessa_Extensions_ExtensionExtensions_WithOrder.htm)|
Регистрирует политику, указывающую порядок выполнения расширения в цепочке.  
[WithSingleton](M_Tessa_Extensions_ExtensionExtensions_WithSingleton.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений,
являющихся синглтонами, посредством их конструкторов по умолчанию. Если класс
расширения реализует интерфейс
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то для
созданного экземпляра один раз будет выполнена асинхронная инициализация.  
[WithUnity](M_Tessa_Extensions_ExtensionExtensions_WithUnity.htm)|
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданного контейнера IUnityContainer. Если класс расширения
реализует интерфейс
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то
инициализация будет вызвана при каждом резолве из контейнера, т.е. для каждой
цепочки расширений.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
