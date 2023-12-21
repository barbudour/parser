# Tessa.Platform.Plugins - пространство имён
API для разработки расширений-плагинов Chronos.
##  __Классы
[PluginExtension](T_Tessa_Platform_Plugins_PluginExtension.htm)|  Базовый
класс для расширения плагина Chronos.  
---|---  
[PluginExtensionContext](T_Tessa_Platform_Plugins_PluginExtensionContext.htm)|
Контекст расширений плагинов Chronos
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).  
[PluginExtensions](T_Tessa_Platform_Plugins_PluginExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Platform.Plugins.  
[PluginSchedulingFilterPolicy](T_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy.htm)|
Политика фильтрации расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm),
использующая политику
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm)
для того, чтобы не выполнять методы плагинов, для которых в контексте
[IPluginExtensionContext](T_Tessa_Platform_Plugins_IPluginExtensionContext.htm)
использован способ диспетчеризации
[SchedulingMode](P_Tessa_Platform_Plugins_IPluginExtensionContext_SchedulingMode.htm),
запрещённый указанной политикой. Если политика
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm)
не зарегистрирована, то метод расширения не будет выполнен, т.е. указание этой
политики является обязательным для выполнения таких расширений.  
[PluginSchedulingMode](T_Tessa_Platform_Plugins_PluginSchedulingMode.htm)|
Способ диспетчеризации плагина.  
[PluginSchedulingPolicy](T_Tessa_Platform_Plugins_PluginSchedulingPolicy.htm)|
Политика, определяющая допустимость способа диспетчеризации плагина
[PluginSchedulingMode](T_Tessa_Platform_Plugins_PluginSchedulingMode.htm) для
выполнения его методов.  
[PluginTraceListener](T_Tessa_Platform_Plugins_PluginTraceListener.htm)|
Объект, выполняющий отслеживание событий, происходящих с расширениями
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm). Обычно при
этом изменяется идентификатор запроса
[ServerRequestID](P_Tessa_Platform_Runtime_RuntimeHelper_ServerRequestID.htm).  
## __Интерфейсы
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm)|  Расширение
плагина Chronos.  
---|---  
[IPluginExtensionContext](T_Tessa_Platform_Plugins_IPluginExtensionContext.htm)|
Контекст расширений плагинов Chronos
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).  
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm)|
Политика, определяющая допустимость способа диспетчеризации плагина
[PluginSchedulingMode](T_Tessa_Platform_Plugins_PluginSchedulingMode.htm) для
выполнения его методов.
