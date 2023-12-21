# ClientConsoleScriptBase - класс
Базовая реализация для скриптов, которые исполняются в консольной утилите с
логином к веб-сервису и опциональным соединением с БД.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ClientConsoleScriptBase : ConsoleScriptBase
VB __Копировать
     Public MustInherit Class ClientConsoleScriptBase
    	Inherits ConsoleScriptBase
C++ __Копировать
     public ref class ClientConsoleScriptBase abstract : public ConsoleScriptBase
F# __Копировать
     [<AbstractClassAttribute>]
    type ClientConsoleScriptBase = 
        class
            inherit ConsoleScriptBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm) __ ClientConsoleScriptBase
##  __Конструкторы
[ClientConsoleScriptBase](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase__ctor.htm)|
Инициализирует новый экземпляр класса ClientConsoleScriptBase  
---|---  
##  __Свойства
[Container](P_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_Container.htm)|
Контейнер Unity, содержащий клиентские зависимости.  
---|---  
[Logger](P_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_Logger.htm)|
Объект, используемый для логирования с использованием консоли.  
[Options](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_Options.htm)|
Настройки, переданные в скрипт в командной строке.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[Result](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_Result.htm)|
Результат выполнения скрипта, возвращаемый как errorlevel для следующей
выполняемой команды.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[ScriptName](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ScriptName.htm)|
Фактическое имя скрипта.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
##  __Методы
[CloseAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_CloseAsync.htm)|
Выполняет выход из системы (закрытие сессии) и другие операции по очистке
состояния.  
---|---  
[ConnectDbAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_ConnectDbAsync.htm)|
Открывает подключение к базе данных. Возвращённый объект
[DbManager](T_Tessa_Platform_Data_DbManager.htm) требуется освободить в блоке
using или try-finally.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_ExecuteAsync.htm)|
Выполняет скрипт.  
(Переопределяет
[ConsoleScriptBase.ExecuteAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ExecuteAsync.htm))  
[ExecuteAsync(IConsoleScriptOptions,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ExecuteAsync_1.htm)|
Выполняет скрипт.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[ExecuteCoreAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_ExecuteCoreAsync.htm)|
Выполняет клиентский скрипт.  
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
[LoginAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_LoginAsync.htm)|
Выполняет вход в систему (открытие сессии) в соответствии с настройками
подключения
[Options](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_Options.htm).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ParameterIsNullOrEmpty](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ParameterIsNullOrEmpty.htm)|
Возвращает признак того, что параметр с указанным именем задан и равен null
или пустой строке. Если параметр отсутствует, то возвращается false.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[ShowHelpAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_ShowHelpAsync.htm)|
Выводит справочную информацию по использованию скрипта.  
(Переопределяет
[ConsoleScriptBase.ShowHelpAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ShowHelpAsync.htm))  
[ShowHelpCoreAsync](M_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase_ShowHelpCoreAsync.htm)|
Выводит справочную информацию по использованию скрипта.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetParameter](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_TryGetParameter.htm)|
Возвращает значение параметра вида /pp:Name=Value по заданному имени или null,
если получить значение не удалось или если параметр присутствует и равен null.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
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
