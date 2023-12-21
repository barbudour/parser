# ConfigurationManagerLazy - класс
Объект, управляющий конфигурацией приложений Tessa. В отличии от
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm) конфигурация
создается и инициализируется при первом обращении к свойствам
[IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm) или при
вызове
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
К объекту возможно одновременное обращение из нескольких потоков.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConfigurationManagerLazy : IConfigurationManager, 
    	IAsyncInitializable
VB __Копировать
     Public NotInheritable Class ConfigurationManagerLazy
    	Implements IConfigurationManager, IAsyncInitializable
C++ __Копировать
     public ref class ConfigurationManagerLazy sealed : IConfigurationManager, 
    	IAsyncInitializable
F# __Копировать
     [<SealedAttribute>]
    type ConfigurationManagerLazy = 
        class
            interface IConfigurationManager
            interface IAsyncInitializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConfigurationManagerLazy
Implements
    [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), [IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm)
##  __Заметки
После создания объекта рекомендуется вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Конструкторы
[ConfigurationManagerLazy](M_Tessa_Platform_ConfigurationManagerLazy__ctor.htm)|
Инициализирует новый экземпляр класса ConfigurationManagerLazy  
---|---  
##  __Свойства
[Configuration](P_Tessa_Platform_ConfigurationManagerLazy_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[DefinedSymbols](P_Tessa_Platform_ConfigurationManagerLazy_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Errors](P_Tessa_Platform_ConfigurationManagerLazy_Errors.htm)| Ошибки,
которые возникли при разборе файлов конфигурации сервера.  
##  __Методы
[CreateDefault](M_Tessa_Platform_ConfigurationManagerLazy_CreateDefault.htm)|
Создает конфигурацию приложения  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Platform_ConfigurationManagerLazy_InitializeAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryGetConfigurationException](M_Tessa_Platform_PlatformExtensions_TryGetConfigurationException.htm)|
Возвращает исключение, описывающее все ошибки, которые произошли при
инициализации конфигурации, или null, если ошибок не было. Такое исключение
можно выбросить, чтобы передать больше информации о проблеме с конфигурацией.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
