# Plugin - методы
##  __Методы
[EntryPointAsync](M_Chronos_Contracts_Plugin_EntryPointAsync.htm)|
Асинхронный метод, вызываемый хостом при запуске плагина.  
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
[LoadConfig](M_Chronos_Contracts_PluginExtensions_LoadConfig.htm)|  Загружает
первый используемый конфигурационный файл для заданного плагина, и возвращает
загруженный XML-документ.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
[LoadConfig](M_Chronos_Contracts_PluginExtensions_LoadConfig_1.htm)|
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryLoadConfig](M_Chronos_Contracts_PluginExtensions_TryLoadConfig.htm)|
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
[TryLoadConfig](M_Chronos_Contracts_PluginExtensions_TryLoadConfig_1.htm)|
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
##  __См. также
#### Ссылки
[Plugin - ](T_Chronos_Contracts_Plugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
