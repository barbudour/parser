# ConsoleScriptBase - класс
Базовая реализация для скриптов, которые исполняются в консольной утилите.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ConsoleScriptBase : IConsoleScript
VB __Копировать
     Public MustInherit Class ConsoleScriptBase
    	Implements IConsoleScript
C++ __Копировать
     public ref class ConsoleScriptBase abstract : IConsoleScript
F# __Копировать
     [<AbstractClassAttribute>]
    type ConsoleScriptBase = 
        class
            interface IConsoleScript
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleScriptBase
Derived
[Tessa.Platform.ConsoleApps.ClientConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase.htm)
[Tessa.Platform.ConsoleApps.ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm)
Implements
    [IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm)
##  __Конструкторы
[ConsoleScriptBase](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase__ctor.htm)|
Инициализирует новый экземпляр класса ConsoleScriptBase  
---|---  
##  __Свойства
[Options](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_Options.htm)|
Настройки, переданные в скрипт в командной строке.  
---|---  
[Result](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_Result.htm)|
Результат выполнения скрипта, возвращаемый как errorlevel для следующей
выполняемой команды.  
[ScriptName](P_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ScriptName.htm)|
Фактическое имя скрипта.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteAsync(CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ExecuteAsync.htm)|
Выполняет скрипт.  
[ExecuteAsync(IConsoleScriptOptions,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ExecuteAsync_1.htm)|
Выполняет скрипт.  
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
[ShowHelpAsync](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_ShowHelpAsync.htm)|
Выводит справочную информацию по использованию скрипта.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetParameter](M_Tessa_Platform_ConsoleApps_ConsoleScriptBase_TryGetParameter.htm)|
Возвращает значение параметра вида /pp:Name=Value по заданному имени или null,
если получить значение не удалось или если параметр присутствует и равен null.  
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
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
