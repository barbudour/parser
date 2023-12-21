# PasswordNotificationsPlugin - класс
Плагин, выполняющий добавление уведомлений о текущих заданиях пользователя.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Chronos.Notices](N_Tessa_Extensions_Default_Chronos_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Chronos (в
Tessa.Extensions.Default.Chronos.dll) Версия: 3.6.0.17
C# __Копировать
    [PluginAttribute(Name = "Password notifications plugin", Description = "Plugin starts at configured time and send emails to users for whom theirs passwords will expire soon.", 
    	Version = 1, ConfigFile = "configuration/PasswordNotifications.xml")]
    public sealed class PasswordNotificationsPlugin : Plugin
VB __Копировать
    <PluginAttribute(Name := "Password notifications plugin", Description := "Plugin starts at configured time and send emails to users for whom theirs passwords will expire soon.", 
    	Version := 1, ConfigFile := "configuration/PasswordNotifications.xml")>
    Public NotInheritable Class PasswordNotificationsPlugin
    	Inherits Plugin
C++ __Копировать
    [PluginAttribute(Name = L"Password notifications plugin", Description = L"Plugin starts at configured time and send emails to users for whom theirs passwords will expire soon.", 
    	Version = 1, ConfigFile = L"configuration/PasswordNotifications.xml")]
    public ref class PasswordNotificationsPlugin sealed : public Plugin
F# __Копировать
     [<SealedAttribute>]
    [<PluginAttribute(Name = "Password notifications plugin", Description = "Plugin starts at configured time and send emails to users for whom theirs passwords will expire soon.", 
    	Version = 1, ConfigFile = "configuration/PasswordNotifications.xml")>]
    type PasswordNotificationsPlugin = 
        class
            inherit Plugin
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Plugin](T_Chronos_Contracts_Plugin.htm) __ PasswordNotificationsPlugin
##  __Конструкторы
[PasswordNotificationsPlugin](M_Tessa_Extensions_Default_Chronos_Notices_PasswordNotificationsPlugin__ctor.htm)|
Инициализирует новый экземпляр класса PasswordNotificationsPlugin  
---|---  
##  __Свойства
[StopRequested](P_Chronos_Contracts_Plugin_StopRequested.htm)|  Признак того,
что запрошена остановка плагина. Значение свойства можно изменить только на
true. Свойство устанавливается равным true сразу при запрошенной остановке
плагина, тогда как
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
переданный в метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm),
отменяется за несколько секунд до таймаута плагина, в соответсвии с настройкой
AwaitCancellationDeltaSeconds в файле app.json.  
(Унаследован от [Plugin](T_Chronos_Contracts_Plugin.htm))  
---|---  
[StopRequestedToken](P_Chronos_Contracts_Plugin_StopRequestedToken.htm)|
Токен отмены плагина, который запрашивается сразу при установке свойства
[StopRequested](P_Chronos_Contracts_Plugin_StopRequested.htm) равным true,
т.е. в момент запроса остановки плагина. Объект
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
переданный в метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm),
отменяется за несколько секунд до таймаута плагина, в соответсвии с настройкой
AwaitCancellationDeltaSeconds в файле app.json.  
(Унаследован от [Plugin](T_Chronos_Contracts_Plugin.htm))  
##  __Методы
[EntryPointAsync](M_Tessa_Extensions_Default_Chronos_Notices_PasswordNotificationsPlugin_EntryPointAsync.htm)|  
(Переопределяет
[Plugin.EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm))  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StopAsync](M_Chronos_Contracts_Plugin_StopAsync.htm)|  Метод, вызываемый
хостом при вежливой остановке плагина. Он должен максимально быстро завершить
выполнение плагина, но не завершать свою работу до тех пор, пока потоки, с
которыми работает плагин, не будут завершены. Реализация по умолчанию
устанавливает свойство
[StopRequested](P_Chronos_Contracts_Plugin_StopRequested.htm), после чего
ожидает завершение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm).  
(Унаследован от [Plugin](T_Chronos_Contracts_Plugin.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[ConfigFilePath](F_Tessa_Extensions_Default_Chronos_Notices_PasswordNotificationsPlugin_ConfigFilePath.htm)|
Относительный путь к конфигурационному файлу плагина.  
---|---  
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
[Tessa.Extensions.Default.Chronos.Notices - пространство
имён](N_Tessa_Extensions_Default_Chronos_Notices.htm)
