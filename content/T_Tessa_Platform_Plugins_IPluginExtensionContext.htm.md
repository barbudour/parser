# IPluginExtensionContext - интерфейс
Контекст расширений плагинов Chronos
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPluginExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IPluginExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IPluginExtensionContext : IExtensionContext
F# __Копировать
     type IPluginExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[DbScope](P_Tessa_Platform_Plugins_IPluginExtensionContext_DbScope.htm)|
Объект, предоставляющий доступ к базе данных.  
[Info](P_Tessa_Platform_Plugins_IPluginExtensionContext_Info.htm)|
Произвольная информация, передаваемая между выполняемыми плагинами по цепочке.  
[SchedulingMode](P_Tessa_Platform_Plugins_IPluginExtensionContext_SchedulingMode.htm)|
Способ диспетчеризации плагина.  
[Session](P_Tessa_Platform_Plugins_IPluginExtensionContext_Session.htm)|
Сессия текущего пользователя, зависит от токена
[Tessa.Platform.Plugins.IPluginExtensionContext.SessionToken].  
[SessionToken](P_Tessa_Platform_Plugins_IPluginExtensionContext_SessionToken.htm)|
Токен для текущей сессии
[Tessa.Platform.Plugins.IPluginExtensionContext.Session], может быть равен
null. Значение можно изменить, указав токен другого пользователя. Также можно
сбросить токен на значение по умолчанию, вызвав метод
[Tessa.Platform.Plugins.IPluginExtensionContext.ResetSessionToken], который
обычно устанавливает серверную сессию пользователя System.  
[StopRequested](P_Tessa_Platform_Plugins_IPluginExtensionContext_StopRequested.htm)|
Признак того, что был инициирован запрос на вежливую остановку плагина, при
этом выполнение метода EntryPoint плагина требуется остановить как можно
скорее, не нарушив согласованность данных.  
[UnityContainer](P_Tessa_Platform_Plugins_IPluginExtensionContext_UnityContainer.htm)|
Контейнер со всеми серверными зависимостями.  
[ValidationResult](P_Tessa_Platform_Plugins_IPluginExtensionContext_ValidationResult.htm)|
Объект, содержащий сообщения валидации при выполнении плагина, который
автоматически записывается в лог после завершения плагина.  
## __Методы
[ResetForNextPlugin](M_Tessa_Platform_Plugins_IPluginExtensionContext_ResetForNextPlugin.htm)|
Сбрасывает состояние контекста для выполнения следующего плагина в цепочке.
Метод вызывается автоматически.  
---|---  
[ResetSessionToken](M_Tessa_Platform_Plugins_IPluginExtensionContext_ResetSessionToken.htm)|
Сбрасывает токен сессии
[Tessa.Platform.Plugins.IPluginExtensionContext.SessionToken] на значение по
умолчанию. Это обычно устанавливает серверную сессию пользователя System.  
[Resolve<T>](M_Tessa_Platform_Plugins_IPluginExtensionContext_Resolve__1.htm)|
Получает сервис или другую зависимость заданного типа из контейнера
[Tessa.Platform.Plugins.IPluginExtensionContext.UnityContainer]. Это
вспомогательный метод, упрощающий получение зависимостей. Если зависимость не
зарегистрирована, то выбрасывается исключение.  
## __См. также
#### Ссылки
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
