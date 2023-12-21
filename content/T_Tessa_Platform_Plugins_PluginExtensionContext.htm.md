# PluginExtensionContext - класс
Контекст расширений плагинов Chronos
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginExtensionContext : IPluginExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class PluginExtensionContext
    	Implements IPluginExtensionContext, IExtensionContext
C++ __Копировать
     public ref class PluginExtensionContext sealed : IPluginExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type PluginExtensionContext = 
        class
            interface IPluginExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IPluginExtensionContext](T_Tessa_Platform_Plugins_IPluginExtensionContext.htm)
##  __Конструкторы
[PluginExtensionContext](M_Tessa_Platform_Plugins_PluginExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств и методов.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Platform_Plugins_PluginExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[DbScope](P_Tessa_Platform_Plugins_PluginExtensionContext_DbScope.htm)|
Объект, предоставляющий доступ к базе данных.  
[Info](P_Tessa_Platform_Plugins_PluginExtensionContext_Info.htm)| Произвольная
информация, передаваемая между выполняемыми плагинами по цепочке.  
[SchedulingMode](P_Tessa_Platform_Plugins_PluginExtensionContext_SchedulingMode.htm)|
Способ диспетчеризации плагина.  
[Session](P_Tessa_Platform_Plugins_PluginExtensionContext_Session.htm)|
Сессия текущего пользователя, зависит от токена
[Tessa.Platform.Plugins.IPluginExtensionContext.SessionToken].  
[SessionToken](P_Tessa_Platform_Plugins_PluginExtensionContext_SessionToken.htm)|
Токен для текущей сессии
[Tessa.Platform.Plugins.IPluginExtensionContext.Session], может быть равен
null. Значение можно изменить, указав токен другого пользователя. Также можно
сбросить токен на значение по умолчанию, вызвав метод
[Tessa.Platform.Plugins.IPluginExtensionContext.ResetSessionToken], который
обычно устанавливает серверную сессию пользователя System.  
[StopRequested](P_Tessa_Platform_Plugins_PluginExtensionContext_StopRequested.htm)|
Признак того, что был инициирован запрос на вежливую остановку плагина, при
этом выполнение метода EntryPoint плагина требуется остановить как можно
скорее, не нарушив согласованность данных.  
[UnityContainer](P_Tessa_Platform_Plugins_PluginExtensionContext_UnityContainer.htm)|
Контейнер со всеми серверными зависимостями.  
[ValidationResult](P_Tessa_Platform_Plugins_PluginExtensionContext_ValidationResult.htm)|
Объект, содержащий сообщения валидации при выполнении плагина, который
автоматически записывается в лог после завершения плагина.  
## __Методы
[CreateAsync](M_Tessa_Platform_Plugins_PluginExtensionContext_CreateAsync.htm)|
Создаёт объект контекста вместе с контейнером Unity для плагина по умолчанию.  
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
[ResetForNextPlugin](M_Tessa_Platform_Plugins_PluginExtensionContext_ResetForNextPlugin.htm)|
Сбрасывает состояние контекста для выполнения следующего плагина в цепочке.
Метод вызывается автоматически.  
[ResetSessionToken](M_Tessa_Platform_Plugins_PluginExtensionContext_ResetSessionToken.htm)|
Сбрасывает токен сессии
[Tessa.Platform.Plugins.IPluginExtensionContext.SessionToken] на значение по
умолчанию. Это обычно устанавливает серверную сессию пользователя System.  
[Resolve<T>](M_Tessa_Platform_Plugins_PluginExtensionContext_Resolve__1.htm)|
Получает сервис или другую зависимость заданного типа из контейнера
[Tessa.Platform.Plugins.IPluginExtensionContext.UnityContainer]. Это
вспомогательный метод, упрощающий получение зависимостей. Если зависимость не
зарегистрирована, то выбрасывается исключение.  
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
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
