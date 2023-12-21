# PluginFinderFactory.CreateWithSubfolders - метод
Возвращает объект, позволяющий осуществлять поиск плагинов в указанной папке и
внутри каждой папки, вложенной в указанную.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IPluginFinder CreateWithSubfolders(
    	string pluginsFolderPath
    )
VB __Копировать
     Public Shared Function CreateWithSubfolders ( 
    	pluginsFolderPath As String
    ) As IPluginFinder
C++ __Копировать
     public:
    static IPluginFinder^ CreateWithSubfolders(
    	String^ pluginsFolderPath
    )
F# __Копировать
     static member CreateWithSubfolders : 
            pluginsFolderPath : string -> IPluginFinder 
#### Параметры
pluginsFolderPath
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Папка, внутри которой объект может осуществлять поиск.
#### Возвращаемое значение
[IPluginFinder](T_Chronos_Platform_Scheduling_IPluginFinder.htm)  
Объект, позволяющий осуществлять поиск плагинов.
##  __См. также
#### Ссылки
[PluginFinderFactory -
](T_Chronos_Platform_Scheduling_PluginFinderFactory.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
