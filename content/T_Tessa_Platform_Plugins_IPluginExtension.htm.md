# IPluginExtension - интерфейс
Расширение плагина Chronos.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPluginExtension : IExtension
VB __Копировать
     Public Interface IPluginExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IPluginExtension : IExtension
F# __Копировать
     type IPluginExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Свойства
[Name](P_Tessa_Platform_Plugins_IPluginExtension_Name.htm)|  Основной
выполняемый метод плагина. Переопределите этот метод в первую очередь, чтобы
определить поведение плагина.  
---|---  
## __Методы
[EntryPoint](M_Tessa_Platform_Plugins_IPluginExtension_EntryPoint.htm)|
Основной выполняемый метод плагина. Переопределите этот метод в первую
очередь, чтобы определить поведение плагина.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
