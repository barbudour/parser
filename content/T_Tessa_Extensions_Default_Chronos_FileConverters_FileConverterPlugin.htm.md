# FileConverterPlugin - класс
Делает преобразование файлов, сохраняет их в карточку кэша
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Chronos.FileConverters](N_Tessa_Extensions_Default_Chronos_FileConverters.htm)  
 **Сборка:** Tessa.Extensions.Default.Chronos (в
Tessa.Extensions.Default.Chronos.dll) Версия: 3.6.0.17
C# __Копировать
    [PluginAttribute(Name = "File converter plugin", Description = "Convert files to specific formats and stores them to the cache card", 
    	Version = 1, ConfigFile = "configuration/FileConverter.xml")]
    public sealed class FileConverterPlugin : Plugin
VB __Копировать
    <PluginAttribute(Name := "File converter plugin", Description := "Convert files to specific formats and stores them to the cache card", 
    	Version := 1, ConfigFile := "configuration/FileConverter.xml")>
    Public NotInheritable Class FileConverterPlugin
    	Inherits Plugin
C++ __Копировать
    [PluginAttribute(Name = L"File converter plugin", Description = L"Convert files to specific formats and stores them to the cache card", 
    	Version = 1, ConfigFile = L"configuration/FileConverter.xml")]
    public ref class FileConverterPlugin sealed : public Plugin
F# __Копировать
     [<SealedAttribute>]
    [<PluginAttribute(Name = "File converter plugin", Description = "Convert files to specific formats and stores them to the cache card", 
    	Version = 1, ConfigFile = "configuration/FileConverter.xml")>]
    type FileConverterPlugin = 
        class
            inherit Plugin
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Plugin](T_Chronos_Contracts_Plugin.htm) __ FileConverterPlugin
##  __Конструкторы
[FileConverterPlugin](M_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterPlugin__ctor.htm)|
Инициализирует новый экземпляр класса FileConverterPlugin  
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
[EntryPointAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterPlugin_EntryPointAsync.htm)|  
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
[StopAsync](M_Tessa_Extensions_Default_Chronos_FileConverters_FileConverterPlugin_StopAsync.htm)|  
(Переопределяет
[Plugin.StopAsync(IGracefulStopToken)](M_Chronos_Contracts_Plugin_StopAsync.htm))  
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
[Tessa.Extensions.Default.Chronos.FileConverters - пространство
имён](N_Tessa_Extensions_Default_Chronos_FileConverters.htm)
