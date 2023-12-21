# IPluginSchedulingPolicy - интерфейс
Политика, определяющая допустимость способа диспетчеризации плагина
[PluginSchedulingMode](T_Tessa_Platform_Plugins_PluginSchedulingMode.htm) для
выполнения его методов.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPluginSchedulingPolicy : IExtensionPolicy
VB __Копировать
     Public Interface IPluginSchedulingPolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class IPluginSchedulingPolicy : IExtensionPolicy
F# __Копировать
     type IPluginSchedulingPolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Методы
[IsAllowed](M_Tessa_Platform_Plugins_IPluginSchedulingPolicy_IsAllowed.htm)|
Признак того, что заданный способ диспетчеризации плагина был разрешён для
расширения плагина с текущей политикой.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
