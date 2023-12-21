# PluginFactory.FromDictionary - метод
Возвращает информацию для создания плагина из хеш-таблицы.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static PluginRemoteCreationInfo FromDictionary(
    	IDictionary<string, Object> dictionary
    )
VB __Копировать
     Public Shared Function FromDictionary ( 
    	dictionary As IDictionary(Of String, Object)
    ) As PluginRemoteCreationInfo
C++ __Копировать
     public:
    static PluginRemoteCreationInfo^ FromDictionary(
    	IDictionary<String^, Object^>^ dictionary
    )
F# __Копировать
     static member FromDictionary : 
            dictionary : IDictionary<string, Object> -> PluginRemoteCreationInfo 
#### Параметры
dictionary
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хеш-таблица с информацией для создания плагина.
#### Возвращаемое значение
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)  
Информация для создания плагина.
##  __См. также
#### Ссылки
[PluginFactory - ](T_Chronos_Platform_Scheduling_PluginFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
