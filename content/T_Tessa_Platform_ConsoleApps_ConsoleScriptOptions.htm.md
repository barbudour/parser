# ConsoleScriptOptions - класс
Настройки, переданные в скрипт в командной строке.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ConsoleScriptOptions : IConsoleScriptOptions
VB __Копировать
     Public Class ConsoleScriptOptions
    	Implements IConsoleScriptOptions
C++ __Копировать
     public ref class ConsoleScriptOptions : IConsoleScriptOptions
F# __Копировать
     type ConsoleScriptOptions = 
        class
            interface IConsoleScriptOptions
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleScriptOptions
Implements
    [IConsoleScriptOptions](T_Tessa_Platform_ConsoleApps_IConsoleScriptOptions.htm)
##  __Заметки
Наследники класса могут добавить свойства.
## __Конструкторы
[ConsoleScriptOptions](M_Tessa_Platform_ConsoleApps_ConsoleScriptOptions__ctor.htm)|
Инициализирует новый экземпляр класса ConsoleScriptOptions  
---|---  
##  __Свойства
[Address](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Address.htm)|
Базовый адрес веб-сервисов.  
---|---  
[ConfigurationString](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_ConfigurationString.htm)|
Имя строки подключения к базе данных или null, если используется строка
подключения по умолчанию.  
[DatabaseName](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_DatabaseName.htm)|
Имя базы данных или null, если используется имя базы данных из строки
подключения.  
[Help](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Help.htm)|  Признак
того, что вместо выполнения скрипта должен выполняться вывод справочной
информации.  
[Input](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Input.htm)|
Стандартный ввод.  
[InstanceName](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_InstanceName.htm)|
Имя экземпляра сервиса.  
[Parameters](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Parameters.htm)|
Именованные параметры, которые дополнительно были переданы в скрипт. Поиск
параметров по имени не учитывает регистр символов.  
[Password](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Password.htm)|
Пароль пользователя для логина в веб-сервис.  
[Quiet](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_Quiet.htm)|  Признак
того, что вывод на консоль должен содержать только серьёзные ошибки.  
[StdErr](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_StdErr.htm)|
Стандартный вывод для ошибок.  
[StdOut](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_StdOut.htm)|
Стандартный вывод для сообщений.  
[UserName](P_Tessa_Platform_ConsoleApps_ConsoleScriptOptions_UserName.htm)|
Имя пользователя для логина в веб-сервис.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
##  __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
