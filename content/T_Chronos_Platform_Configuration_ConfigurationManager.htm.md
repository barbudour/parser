# ConfigurationManager - класс
Объект, управляющий конфигурацией приложений Chronos. К объекту возможно
одновременное обращение из нескольких потоков.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConfigurationManager : IConfigurationManager, 
    	IAsyncInitializable
VB __Копировать
     Public NotInheritable Class ConfigurationManager
    	Implements IConfigurationManager, IAsyncInitializable
C++ __Копировать
     public ref class ConfigurationManager sealed : IConfigurationManager, 
    	IAsyncInitializable
F# __Копировать
     [<SealedAttribute>]
    type ConfigurationManager = 
        class
            interface IConfigurationManager
            interface IAsyncInitializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConfigurationManager
Implements
    [IConfigurationManager](T_Chronos_Platform_Configuration_IConfigurationManager.htm), [IAsyncInitializable](T_Chronos_Platform_IAsyncInitializable.htm)
##  __Заметки
После создания объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Конструкторы
[ConfigurationManager(ConfigurationObject, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств. После создания
объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
---|---  
[ConfigurationManager(String, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor_2.htm)|
Создаёт экземпляр класса с указанием полного пути до файла с конфигурацией.
Вызов конструктора не может завершиться исключением. После создания объекта
необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
[ConfigurationManager(Assembly, String, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor_1.htm)|
Создаёт экземпляр класса с указанием сборки, рядом с которой лежит файл
конфигурации app.json. Вызов конструктора не может завершиться исключением.
После создания объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
## __Свойства
[Configuration](P_Chronos_Platform_Configuration_ConfigurationManager_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[Default](P_Chronos_Platform_Configuration_ConfigurationManager_Default.htm)|
Конфигурация приложения, доступная по умолчанию. Рекомендуется использовать
метод
[GetDefaultAsync(CancellationToken)](M_Chronos_Platform_Configuration_ConfigurationManager_GetDefaultAsync.htm)
для асинхронной инициализации конфигурации.  
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Errors](P_Chronos_Platform_Configuration_ConfigurationManager_Errors.htm)|
Ошибки, которые возникли при разборе файлов конфигурации сервера.  
[GlobalDefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_GlobalDefinedSymbols.htm)|
Глобально объявленные символы по умолчанию, доступные для всех объектов
конфигурации. По умолчанию соответствуют операционной системе, разрядности
процессора и другим параметрам среды выполнения. Используются для
инициализации начального значения свойства
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm)
для каждого объекта конфигурации.  
[Settings](P_Chronos_Platform_Configuration_ConfigurationManager_Settings.htm)|
Настройки для приложения, доступные по умолчанию. В качестве ключа выступает
имя настройки, а в качестве значения - её значение (строка, число и т.п.).
Целые числа обычно представление как тип
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
## __Методы
[CreateDefaultAsync](M_Chronos_Platform_Configuration_ConfigurationManager_CreateDefaultAsync.htm)|
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
[GetCurrentSymbols](M_Chronos_Platform_Configuration_ConfigurationManager_GetCurrentSymbols.htm)|
Возвращает текущие объявленные символы
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm),
соответствующие операционной системе, разрядности процессора и другим
параметрам среды выполнения.  
[GetDefaultAsync](M_Chronos_Platform_Configuration_ConfigurationManager_GetDefaultAsync.htm)|
Получает конфигурацию приложения, доступную по умолчанию.  
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
[InitializeAsync](M_Chronos_Platform_Configuration_ConfigurationManager_InitializeAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DefaultSymbolValue](F_Chronos_Platform_Configuration_ConfigurationManager_DefaultSymbolValue.htm)|
Значение по умолчанию для символов.  
---|---  
[DefineDirective](F_Chronos_Platform_Configuration_ConfigurationManager_DefineDirective.htm)|
Директива в конфигурационном файле, выполняющая включение или исключение
символов из текущей конфигурации. Символы в дальнейшей используются в
директиве
[IfDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IfDirective.htm).
Пример: ".define": [ "addedSymbol", "!removedSymbol" ]  
[IfDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IfDirective.htm)|
Директива в конфигурационном файле, выполняющая включение в текущую
конфигурацию нижележащего блока при условии, что выполняется условие,
связанное с перечисленными символами. Пример: ".if": [ [ "existentSymbol",
"!absentSymbol" ], { "Key": value } ]  
[IncludeDirective](F_Chronos_Platform_Configuration_ConfigurationManager_IncludeDirective.htm)|
Директива в конфигурационном файле, выполняющая включение содержимого
указанного файла в текущую конфигурацию. Пример: ".include": "../app.json"  
[LinuxSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_LinuxSymbol.htm)|
Символ, объявленный при выполнении на Linux.  
[Process32BitSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_Process32BitSymbol.htm)|
Символ, объявленный при выполнении в 32-битном процессе.  
[Process64BitSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_Process64BitSymbol.htm)|
Символ, объявленный при выполнении в 64-битном процессе.  
[WindowsSymbol](F_Chronos_Platform_Configuration_ConfigurationManager_WindowsSymbol.htm)|
Символ, объявленный при выполнении на Windows.  
## __Методы расширения
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
##  __См. также
#### Ссылки
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
