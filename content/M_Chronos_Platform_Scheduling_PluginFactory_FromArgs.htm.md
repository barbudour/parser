# PluginFactory.FromArgs - метод
Возвращает информацию для создания плагина из параметров командной строки.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static PluginRemoteCreationInfo FromArgs(
    	string[] args
    )
VB __Копировать
     Public Shared Function FromArgs ( 
    	args As String()
    ) As PluginRemoteCreationInfo
C++ __Копировать
     public:
    static PluginRemoteCreationInfo^ FromArgs(
    	array<String^>^ args
    )
F# __Копировать
     static member FromArgs : 
            args : string[] -> PluginRemoteCreationInfo 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Параметры командной строки с информацией для создания плагина.
#### Возвращаемое значение
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)  
Информация для создания плагина.
##  __См. также
#### Ссылки
[PluginFactory - ](T_Chronos_Platform_Scheduling_PluginFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
