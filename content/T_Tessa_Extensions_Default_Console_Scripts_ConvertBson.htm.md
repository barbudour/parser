# ConvertBson - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Console.Scripts](N_Tessa_Extensions_Default_Console_Scripts.htm)  
 **Сборка:** Tessa.Extensions.Default.Console (в
Tessa.Extensions.Default.Console.dll) Версия: 3.6.0.17
C# __Копировать
    [ConsoleScriptAttribute("ConvertBson")]
    public sealed class ConvertBson : ServerConsoleScriptBase
VB __Копировать
    <ConsoleScriptAttribute("ConvertBson")>
    Public NotInheritable Class ConvertBson
    	Inherits ServerConsoleScriptBase
C++ __Копировать
    [ConsoleScriptAttribute(L"ConvertBson")]
    public ref class ConvertBson sealed : public ServerConsoleScriptBase
F# __Копировать
     [<SealedAttribute>]
    [<ConsoleScriptAttribute("ConvertBson")>]
    type ConvertBson = 
        class
            inherit ServerConsoleScriptBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm) __[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm) __ ConvertBson
##  __Конструкторы
[ConvertBson](M_Tessa_Extensions_Default_Console_Scripts_ConvertBson__ctor.htm)|
Инициализирует новый экземпляр класса ConvertBson  
---|---  
##  __Свойства
[Container](P_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_Container.htm)|
Контейнер Unity, содержащий серверные зависимости.  
(Унаследован от
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm))  
---|---  
[Logger](P_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_Logger.htm)|
Объект, используемый для логирования с использованием консоли.  
(Унаследован от
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm))  
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
[CreateDbManagerAsync](M_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_CreateDbManagerAsync.htm)|
Открывает новое соединение к БД и возвращает объект
[DbManager](T_Tessa_Platform_Data_DbManager.htm). В отличие от обращения к
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm), открытие соединения
выполняется полностью асинхронно. Вызовите new
QueryBuilderFactory(db.GetDbms()) для создание объекта, выполняющего
построение запросов к БД для текущей СУБД.  
(Унаследован от
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_ExecuteAsync.htm)|
Выполняет скрипт.  
(Унаследован от
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm))  
[ExecuteAsync(IConsoleScriptOptions,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ExecuteAsync_1.htm)|
Выполняет скрипт.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[ExecuteCoreAsync](M_Tessa_Extensions_Default_Console_Scripts_ConvertBson_ExecuteCoreAsync.htm)|  
(Переопределяет
[ServerConsoleScriptBase.ExecuteCoreAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_ExecuteCoreAsync.htm))  
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
[ParameterIsNullOrEmpty](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ParameterIsNullOrEmpty.htm)|
Возвращает признак того, что параметр с указанным именем задан и равен null
или пустой строке. Если параметр отсутствует, то возвращается false.  
(Унаследован от
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm))  
[ShowHelpAsync](M_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_ShowHelpAsync.htm)|
Выводит справочную информацию по использованию скрипта.  
(Унаследован от
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm))  
[ShowHelpCoreAsync](M_Tessa_Extensions_Default_Console_Scripts_ConvertBson_ShowHelpCoreAsync.htm)|  
(Переопределяет
[ServerConsoleScriptBase.ShowHelpCoreAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase_ShowHelpCoreAsync.htm))  
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
[Tessa.Extensions.Default.Console.Scripts - пространство
имён](N_Tessa_Extensions_Default_Console_Scripts.htm)
