# ExtensionExtensions.WithLazy - метод
##  __Список перегрузок
[WithLazy(IExtensionPolicyContainer,
Func<Task<IExtension>>)](M_Tessa_Extensions_ExtensionExtensions_WithLazy.htm)|
Регистрирует политику, указывающую на способ отложенного получения экземпляров
расширений посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию внутри лямбда-
выражения.  
---|---  
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
## __См. также
#### Ссылки
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
