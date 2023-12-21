# Chronos.Contracts - пространство имён
Контракты для плагинов Chronos, такие как интерфейсы и атрибуты, которые
используются в сборках с плагинами. Также содержит средства управления
конфигурационными файлами изнутри плагина.
##  __Классы
[Plugin](T_Chronos_Contracts_Plugin.htm)|  Базовый класс для асинхронного
плагина.  
---|---  
[PluginAttribute](T_Chronos_Contracts_PluginAttribute.htm)|  Атрибут,
указывающий метаданные плагина, включая метаданные триггера, на основании
которого планировщик будет вызывать плагин.  
[PluginContractHelper](T_Chronos_Contracts_PluginContractHelper.htm)|
Вспомогательные методы и константы для работы с плагинами, которые могут
использоваться в самом плагине.  
[PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm)|  Методы-
расширения для интерфейса [IPlugin](T_Chronos_Contracts_IPlugin.htm).  
[PluginTriggerAttribute](T_Chronos_Contracts_PluginTriggerAttribute.htm)|
Атрибут, указывающий метаданные дополнительного триггера, на основании
которого планировщик будет вызывать плагин.  
## __Интерфейсы
[IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm)|  Токен,
позволяющий определить состояние плагина из метода его вежливой остановки.  
---|---  
[IPlugin](T_Chronos_Contracts_IPlugin.htm)|  Интерфейс плагина.  
[IPluginMetadata](T_Chronos_Contracts_IPluginMetadata.htm)|  Метаданные
плагина. Содержат метаданные триггера
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm).  
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)|
Метаданные триггера, на основании которого планировщик будет вызывать плагин.  
[ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm)|
Экспортируемые из сборок метаданные, поддерживающие сериализацию. Используется
для сериализации метаданных.  
[ISupportGracefulStop](T_Chronos_Contracts_ISupportGracefulStop.htm)|
Дополнительный интерфейс плагина, поддерживающего вежливую остановку. Плагин,
реализующий данный интерфейс, должен также реализовывать
[IPlugin](T_Chronos_Contracts_IPlugin.htm).
