# ClientOperationContext - класс
Контекст операции для клиентского скрипта
[ClientConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientOperationContext
VB __Копировать
     Public NotInheritable Class ClientOperationContext
C++ __Копировать
     public ref class ClientOperationContext sealed
F# __Копировать
     [<SealedAttribute>]
    type ClientOperationContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientOperationContext
##  __Конструкторы
[ClientOperationContext](M_Tessa_Platform_ConsoleApps_ClientOperationContext__ctor.htm)|
Инициализирует новый экземпляр класса ClientOperationContext  
---|---  
##  __Свойства
[ConfigurationString](P_Tessa_Platform_ConsoleApps_ClientOperationContext_ConfigurationString.htm)|
Имя строки подключения к базе данных из app.json.  
---|---  
[ConnectDbFuncAsync](P_Tessa_Platform_ConsoleApps_ClientOperationContext_ConnectDbFuncAsync.htm)|
Функция, выполняющее подключение к базе данных, или null, если функция не
задана.  
[DatabaseName](P_Tessa_Platform_ConsoleApps_ClientOperationContext_DatabaseName.htm)|
Имя базы данных, переопределяющее то, что указано в строке подключения в
app.json[ConfigurationString](P_Tessa_Platform_ConsoleApps_ClientOperationContext_ConfigurationString.htm).  
[ExecuteAsync](P_Tessa_Platform_ConsoleApps_ClientOperationContext_ExecuteAsync.htm)|
Функция, выполняющая собственную логику скрипта, или null, если функция не
задана, что приведёт к ошибке выполнения скрипта.  
[Input](P_Tessa_Platform_ConsoleApps_ClientOperationContext_Input.htm)|
Объект, используемый для чтения данных из стандартного устройства ввода.  
[Parameters](P_Tessa_Platform_ConsoleApps_ClientOperationContext_Parameters.htm)|
Дополнительные параметры, переданные из командной строки в операцию. Например:
-pp:key=value.  
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
