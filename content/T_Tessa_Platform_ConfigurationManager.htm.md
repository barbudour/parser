# ConfigurationManager - класс
Объект, управляющий конфигурацией приложений Tessa. К объекту возможно
одновременное обращение из нескольких потоков.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
    [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), [IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm)
##  __Заметки
После создания объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Конструкторы
[ConfigurationManager(ConfigurationObject, IEnumerable<KeyValuePair<String,
String>>)](M_Tessa_Platform_ConfigurationManager__ctor_2.htm)|  Создаёт
экземпляр класса с указанием значений его свойств. После создания объекта
необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
---|---  
[ConfigurationManager(String, IEnumerable<KeyValuePair<String,
String>>)](M_Tessa_Platform_ConfigurationManager__ctor_1.htm)|  Создаёт
экземпляр класса с указанием полного пути до файла с конфигурацией. Вызов
конструктора не может завершиться исключением. После создания объекта
необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
[ConfigurationManager(Assembly, String, IEnumerable<KeyValuePair<String,
String>>)](M_Tessa_Platform_ConfigurationManager__ctor.htm)|  Создаёт
экземпляр класса с указанием сборки, рядом с которой лежит файл конфигурации
app.json. Вызов конструктора не может завершиться исключением. После создания
объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
## __Свойства
[Configuration](P_Tessa_Platform_ConfigurationManager_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[Connections](P_Tessa_Platform_ConfigurationManager_Connections.htm)|  Строки
подключения для приложения, доступные по умолчанию. В качестве ключа выступает
имя строки подключения, а в качестве значения - сама строка.  
[Default](P_Tessa_Platform_ConfigurationManager_Default.htm)|  Конфигурация
приложения, доступная по умолчанию. Рекомендуется использовать метод
[GetDefaultAsync(CancellationToken)](M_Tessa_Platform_ConfigurationManager_GetDefaultAsync.htm)
для асинхронной инициализации конфигурации.  
[DefinedSymbols](P_Tessa_Platform_ConfigurationManager_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Dynamic](P_Tessa_Platform_ConfigurationManager_Dynamic.htm)|  Объект,
позволяющий получить любые свойства для текущего приложения. Например: string
serverCode = ConfigurationManager.Dynamic.Settings.ServerCode;  
[Errors](P_Tessa_Platform_ConfigurationManager_Errors.htm)| Ошибки, которые
возникли при разборе файлов конфигурации сервера.  
[GlobalDefinedSymbols](P_Tessa_Platform_ConfigurationManager_GlobalDefinedSymbols.htm)|
Глобально объявленные символы по умолчанию, доступные для всех объектов
конфигурации. По умолчанию соответствуют операционной системе, разрядности
процессора и другим параметрам среды выполнения. Используются для
инициализации начального значения свойства
[DefinedSymbols](P_Tessa_Platform_ConfigurationManager_DefinedSymbols.htm) для
каждого объекта конфигурации.  
[Settings](P_Tessa_Platform_ConfigurationManager_Settings.htm)|  Настройки для
приложения, доступные по умолчанию. В качестве ключа выступает имя настройки,
а в качестве значения - её значение (строка, число и т.п.). Целые числа обычно
представление как тип
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
## __Методы
[CreateDbManager](M_Tessa_Platform_ConfigurationManager_CreateDbManager.htm)|
Создаёт объект [DbManager](T_Tessa_Platform_Data_DbManager.htm) с
использованием строки подключения с заданным именем.  
---|---  
[CreateDefaultAsync](M_Tessa_Platform_ConfigurationManager_CreateDefaultAsync.htm)|
Создает конфигурацию приложения  
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
[GetConfigurationDataProviderFromType](M_Tessa_Platform_ConfigurationManager_GetConfigurationDataProviderFromType.htm)|
Возвращает объект
[ConfigurationDataProvider](T_Tessa_Platform_ConfigurationDataProvider.htm) по
строке, которая описывает его имя (алиас), полное имя типа или пространство
имён.  
[GetCurrentSymbols](M_Tessa_Platform_ConfigurationManager_GetCurrentSymbols.htm)|
Возвращает текущие объявленные символы
[DefinedSymbols](P_Tessa_Platform_ConfigurationManager_DefinedSymbols.htm),
соответствующие операционной системе, разрядности процессора и другим
параметрам среды выполнения.  
[GetDataProvider](M_Tessa_Platform_ConfigurationManager_GetDataProvider.htm)|
Получает объект IDataProvider с использованием строки подключения с заданным
именем.  
[GetDbProviderFactory](M_Tessa_Platform_ConfigurationManager_GetDbProviderFactory.htm)|
Получает объект
[DbProviderFactory](https://learn.microsoft.com/dotnet/api/system.data.common.dbproviderfactory)
с использованием строки подключения с заданным именем.  
[GetDefaultAsync](M_Tessa_Platform_ConfigurationManager_GetDefaultAsync.htm)|
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
[InitializeAsync](M_Tessa_Platform_ConfigurationManager_InitializeAsync.htm)|
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
##  __Поля
[DefaultSymbolValue](F_Tessa_Platform_ConfigurationManager_DefaultSymbolValue.htm)|
Значение по умолчанию для символов.  
---|---  
[DefineDirective](F_Tessa_Platform_ConfigurationManager_DefineDirective.htm)|
Директива в конфигурационном файле, выполняющая включение или исключение
символов из текущей конфигурации. Символы в дальнейшей используются в
директиве
[IfDirective](F_Tessa_Platform_ConfigurationManager_IfDirective.htm). Пример:
".define": [ "addedSymbol", "!removedSymbol" ]  
[IfDirective](F_Tessa_Platform_ConfigurationManager_IfDirective.htm)|
Директива в конфигурационном файле, выполняющая включение в текущую
конфигурацию нижележащего блока при условии, что выполняется условие,
связанное с перечисленными символами. Пример: ".if": [ [ "existentSymbol",
"!absentSymbol" ], { "Key": value } ]  
[IncludeDirective](F_Tessa_Platform_ConfigurationManager_IncludeDirective.htm)|
Директива в конфигурационном файле, выполняющая включение содержимого
указанного файла в текущую конфигурацию. Пример: ".include": "../app.json"  
[LinuxSymbol](F_Tessa_Platform_ConfigurationManager_LinuxSymbol.htm)|  Символ,
объявленный при выполнении на Linux.  
[Process32BitSymbol](F_Tessa_Platform_ConfigurationManager_Process32BitSymbol.htm)|
Символ, объявленный при выполнении в 32-битном процессе.  
[Process64BitSymbol](F_Tessa_Platform_ConfigurationManager_Process64BitSymbol.htm)|
Символ, объявленный при выполнении в 64-битном процессе.  
[WindowsSymbol](F_Tessa_Platform_ConfigurationManager_WindowsSymbol.htm)|
Символ, объявленный при выполнении на Windows.  
[WineSymbol](F_Tessa_Platform_ConfigurationManager_WineSymbol.htm)|  Символ,
объявленный при выполнении на Wine (Windows, эмулируемый в Linux).  
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
[TryGetConfigurationException](M_Tessa_Platform_PlatformExtensions_TryGetConfigurationException.htm)|
Возвращает исключение, описывающее все ошибки, которые произошли при
инициализации конфигурации, или null, если ошибок не было. Такое исключение
можно выбросить, чтобы передать больше информации о проблеме с конфигурацией.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
