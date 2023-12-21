# PluginIncludeConfigHelper.LoadAssemblyLocationList - метод
Возвращает список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, располагающемся в указанной папке.
Конфигурационный файл должен иметь имя, заданное в константе
[PluginFileName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginFileName.htm).
##  __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<string> LoadAssemblyLocationList(
    	string folderPath
    )
VB __Копировать
     Public Shared Function LoadAssemblyLocationList ( 
    	folderPath As String
    ) As IList(Of String)
C++ __Копировать
     public:
    static IList<String^>^ LoadAssemblyLocationList(
    	String^ folderPath
    )
F# __Копировать
     static member LoadAssemblyLocationList : 
            folderPath : string -> IList<string> 
#### Параметры
folderPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь до папки с плагинами.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, или пустой список, если такие указания отсутствовали,
конфигурационный файл отсутствует или возникли проблемы с его разбором
##  __См. также
#### Ссылки
[PluginIncludeConfigHelper -
](T_Chronos_Platform_PluginIncludeConfigHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
